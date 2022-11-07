import os
import nuke

current_dir = os.path.dirname(__file__)
latest_version = max([int(v[1:]) for v in os.listdir(current_dir) if v.startswith("v") and os.path.isdir(os.path.join(current_dir, v))])
latest_version = "v{}".format(format(latest_version, '02'))

plugin_dir = os.path.join(os.path.dirname(__file__), latest_version)
# nuke.pluginAddPath(plugin_dir.replace('\\', '/'))

load = [
    "tools/light_mixer",
    "tools/look_manager",
    ]

for ppath in load:
    nuke.pluginAddPath("{}/{}".format(plugin_dir, ppath))

print("Successfully loaded h_nuke {}".format(latest_version))
