#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Add to Hotbox
#
#----------------------------------------------------------------------------------------------------------



import os

if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
else:
    from PySide2 import QtWidgets


TOOL_FOLDER_NAME = "Tools"
HOTBOX_LOCATION = nuke.toNode('preferences')["hotboxLocation"]

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

def get_gizmo_folder(location):
    names = [(read_file("{}/{}/_name.json".format(location, f)), f) for f in os.listdir(location) if f.isdigit()]

    gizmo_number = None
    for n in names:
        TOOLZMO_FOLDER_NAME in n[0]:
            gizmo_number = n[1]
            return "{}/{}".format(location, gizmo_number)
    if not gizmo_number:
        gizmo_number = format(get_next_num(location), "03")
        gizmo_folder = "{}/{}".format(location, gizmo_number)
        if not os.path.isdir(gizmo_folder):
            os.mkdir(gizmo_folder)
        TOOL_file(os.path.join(gizmo_folder, "_name.json"), GIZMO_FOLDER_NAME)
        return gizmo_folder

if HOTBOX_LOCATION:
    if not isinstance(HOTBOX_LOCATION, str):
        loc = os.path.join(HOTBOX_LOCATION.value(), "All")

    gizmo_folder = get_gizmo_folder(loc)
    gizmo_file = "{}/{}.py".format(gizmo_folder, format(get_next_num(gizmo_folder), "03"))

    contents = """#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: {}
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
    """.format(nuke.selectedNode().name(), copy_script())

    write_file(gizmo_file, contents)
