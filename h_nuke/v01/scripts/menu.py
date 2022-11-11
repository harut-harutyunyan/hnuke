import os
import nuke


import W_smartAlign
import W_hotbox, W_hotboxManager
import dDot


# gizmos

h_gizmos = os.path.join(os.path.dirname(os.path.dirname(__file__)), "gizmos")
h_gizmos = h_gizmos.replace('\\', '/')
toolbar = nuke.toolbar("Nodes")
k = toolbar.addMenu("h_gizmos")
for gizmo in os.listdir(h_gizmos):
    name, _ = os.path.splitext(gizmo)
    k.addCommand(name, "nuke.createNode(\"{}\")".format(gizmo))

# W SmartAlign

import W_smartAlign

menuBar = nuke.menu("Nuke")
menuBar.addCommand("Edit/Node/Align/Left", 'W_smartAlign.alignNodes("left")', "Alt+left", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Right", 'W_smartAlign.alignNodes("right")', "Alt+right", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Up", 'W_smartAlign.alignNodes("up")', "Alt+up", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Down", 'W_smartAlign.alignNodes("down")', "Alt+down", shortcutContext=2)
