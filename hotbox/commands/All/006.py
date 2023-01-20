#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Add to Hotbox
#
#----------------------------------------------------------------------------------------------------------


import os
import nukescripts

if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
else:
    from PySide2 import QtWidgets


TOOL_FOLDER_LIST = [
"ToolSets",
]

HOTBOX_LOCATION = nuke.toNode('preferences')["hotboxLocation"]

def interface2rgb(hexValue, normalize = True):
    '''
    Convert a color stored as a 32 bit value as used by nuke for interface colors to normalized rgb values.

    '''
    return [(0xFF & hexValue >>  i) / 255.0 for i in [24,16,8]]

def rgb2hex(rgbaValues):
    '''
    Convert a color stored as normalized rgb values to a hex.
    '''

    rgbaValues = [int(i * 255) for i in rgbaValues]

    if len(rgbaValues) < 3:
        return

    return '#%02x%02x%02x' % (rgbaValues[0],rgbaValues[1],rgbaValues[2])

def read_file(file):
    with open(file, "r") as f:
        return f.read()

def write_file(file, text):
    with open(file, "w") as f:
        f.write(text)

def copy_script():
    nuke.nodeCopy('%clipboard%')
    clipboard = QtWidgets.QApplication.clipboard()
    script = clipboard.text()
    return script

def get_next_num(location):
    nums = [int(i.split(".")[0]) for i in os.listdir(location) if i.split(".")[0].isdigit()]
    if not nums:
        return 1
    else:
        return max(nums)+1

def get_gizmo_folder(location, folder_name):
    if folder_name == "root":
        return location

    names = [(read_file("{}/{}/_name.json".format(location, f)), f) for f in os.listdir(location) if f.isdigit()]

    gizmo_number = None
    for n in names:
        if folder_name in n[0]:
            gizmo_number = n[1]
            return "{}/{}".format(location, gizmo_number)
    if not gizmo_number:
        gizmo_number = format(get_next_num(location), "03")
        gizmo_folder = "{}/{}".format(location, gizmo_number)
        if not os.path.isdir(gizmo_folder):
            os.mkdir(gizmo_folder)
        write_file(os.path.join(gizmo_folder, "_name.json"), folder_name)
        return gizmo_folder

class ToHotbox(nukescripts.PythonPanel):
    def __init__(self):
        super(ToHotbox, self).__init__('Add to Hotbox')

        self.folder = nuke.Enumeration_Knob("folder", "folder: ", ["root"] + TOOL_FOLDER_LIST)
        self.name = nuke.String_Knob("name", 'name: ')
        self.color = nuke.ColorChip_Knob('color', '', 0)
        self.color.clearFlag(nuke.STARTLINE)
        self.addKnob(self.folder)
        self.addKnob(self.name)
        self.addKnob(self.color)

def main():
    panel = ToHotbox()
    if panel.showModalDialog():
        col = panel.color.value()
        name = panel.name.value()
        folder = panel.folder.value()
        if not name:
            name = nuke.selectedNode().name()
        if col != 0:
            col_hex = "\n# COLOR: "+rgb2hex(interface2rgb(col))
        else:
            col_hex = ""

        if HOTBOX_LOCATION:
            if not isinstance(HOTBOX_LOCATION, str):
                loc = os.path.join(HOTBOX_LOCATION.value(), "All")
            else:
                loc = os.path.join(HOTBOX_LOCATION, "All")

            gizmo_folder = get_gizmo_folder(loc, folder)
            gizmo_file = "{}/{}.py".format(gizmo_folder, format(get_next_num(gizmo_folder), "03"))

            contents = """#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: {}{}
#
#----------------------------------------------------------------------------------------------------------




if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
else:
    from PySide2 import QtWidgets

script = r'''{}'''


clipboard = QtWidgets.QApplication.clipboard()
clipboard.setText(script)
nuke.nodePaste('%clipboard%')
            """.format(name, col_hex, copy_script())

            write_file(gizmo_file, contents)


if nuke.selectedNodes():
    main()

