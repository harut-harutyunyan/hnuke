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


HOTBOX_LOCATION = nuke.toNode('preferences')["hotboxLocation"]

if not isinstance(HOTBOX_LOCATION, str):
    HOTBOX_LOCATION = os.path.join(HOTBOX_LOCATION.value(), "All")
else:
    HOTBOX_LOCATION = os.path.join(HOTBOX_LOCATION, "All")

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

def get_folder_names():
    return [(read_file("{}/{}/_name.json".format(HOTBOX_LOCATION, f)), f) for f in os.listdir(HOTBOX_LOCATION) if f.isdigit()]

def get_gizmo_folder(location, folder_name):
    if folder_name == "root":
        return location

    names = get_folder_names()

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
        self.setMinimumSize(300, 50)
        self.folder = nuke.Enumeration_Knob("folder", "folder: ", ["root"] + [i[0] for i in get_folder_names()]+["custom"])
        self.custom_folder = nuke.String_Knob("custom", 'custom: ')
        self.custom_folder.clearFlag(nuke.STARTLINE)
        self.custom_folder.setVisible(False)
        self.name = nuke.String_Knob("name", 'name: ')
        self.color = nuke.ColorChip_Knob('color', '', 0)
        self.color.clearFlag(nuke.STARTLINE)
        self.addKnob(self.folder)
        self.addKnob(self.custom_folder)
        self.addKnob(self.name)
        self.addKnob(self.color)

    def knobChanged(self, knob):
            if knob == self.folder:
                if knob.value() == "custom":
                    self.custom_folder.setVisible(True)
                else:
                    self.custom_folder.setVisible(False)

def main():
    panel = ToHotbox()
    if panel.showModalDialog():
        col = panel.color.value()
        name = panel.name.value()
        folder = panel.folder.value()
        if folder == "custom":
            custom_folder = panel.custom_folder.value()
            if custom_folder:
                folder=custom_folder
            else:
                folder = "root"

        if not name:
            name = nuke.selectedNode().name()
        if col != 0:
            col_hex = "\n# COLOR: "+rgb2hex(interface2rgb(col))
        else:
            col_hex = ""

        gizmo_folder = get_gizmo_folder(HOTBOX_LOCATION, folder)
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

