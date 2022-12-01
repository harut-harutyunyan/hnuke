import os
import nuke


import W_smartAlign
import W_hotbox, W_hotboxManager
import dDot


# gizmos
def add_gizmos(menu, search_path):
    for gizmo in os.listdir(search_path):
        name, ext = os.path.splitext(gizmo)
        if ext in [".gizmo", ".nk"]:
            gizmo = os.path.join(search_path, gizmo)
            gizmo = gizmo.replace("\\", "/")
            menu.addCommand(name, "nuke.createNode(\"{}\")".format(gizmo))

h_gizmos = os.path.join(os.path.dirname(os.path.dirname(__file__)), "gizmos")
h_gizmos = h_gizmos.replace('\\', '/')
toolbar = nuke.toolbar("Nodes")
k = toolbar.addMenu("h_gizmos")

for f in os.listdir(h_gizmos):
  fpath = os.path.join(h_gizmos, f)
  if os.path.isdir(fpath):
    menu = k.addMenu(f)
    add_gizmos(menu, fpath)

# W SmartAlign

import W_smartAlign

menuBar = nuke.menu("Nuke")
menuBar.addCommand("Edit/Node/Align/Left", 'W_smartAlign.alignNodes("left")', "Alt+left", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Right", 'W_smartAlign.alignNodes("right")', "Alt+right", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Up", 'W_smartAlign.alignNodes("up")', "Alt+up", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Down", 'W_smartAlign.alignNodes("down")', "Alt+down", shortcutContext=2)

# knob defaults
nuke.knobDefault("Read.postage_stamp", "False")
nuke.knobDefault("CheckerBoard.postage_stamp", "False")
nuke.knobDefault("Constant.postage_stamp", "False")
nuke.knobDefault("ColorWheel.postage_stamp", "False")
nuke.knobDefault("ColorBars.postage_stamp", "False")
nuke.knobDefault("Views.views_colours true")
nuke.knobDefault("Blur.label", "[value size]")
nuke.knobDefault("Tracker4.zoom_window_behaviour", "0")
