import os
import nuke


GIZMO_ROOT = os.path.dirname(__file__)


def find_gizmo_files(root_dir):
    gizmo_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.gizmo'):
                gizmo_files.append(os.path.join(root, file))
    return gizmo_files

def get_menu_location(gizmo_filepath):
    location = gizmo_filepath.replace(GIZMO_ROOT, "")
    location = location.replace("\\", "/")
    location = location[1:] if location.startswith("/") else location
    location = os.path.splitext(location)[0]
    menu, location = location.split("/", 1)
    return (menu, location)

def main():
    gizmo_files = find_gizmo_files(GIZMO_ROOT)
    toolbar = nuke.toolbar("Nodes")
    for gizmo_filepath in gizmo_files:
        menu, location = get_menu_location(gizmo_filepath)
        tool_menu = toolbar.findItem(menu)
        if not tool_menu:
            tool_menu= toolbar.addMenu(menu)

        tool_menu.addCommand(location, "nuke.createNode(\"{}\")".format(gizmo_filepath.replace("\\", "/")))

main()
