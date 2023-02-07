import os
import nuke

load = [
    "gizmos",
    "scripts",
    "tools/look_manager",
    "tools/w_hotbox",
    "tools/ddot",
    "tools/quick_share",
    ]

current_dir = os.path.dirname(__file__)
for ppath in load:
    nuke.pluginAddPath("{}/{}".format(current_dir, ppath))
