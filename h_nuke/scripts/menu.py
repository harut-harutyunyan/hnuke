import os
import nuke

import nukescripts
import W_smartAlign
import W_hotbox, W_hotboxManager
# import dDot
import gizmo_loader
import tracker_to_node
import set_gui


## commands

# close open property panels
menu = nuke.menu("Nuke")
menu.addCommand('Edit/hscripts/ClosePanels', lambda: [node.hideControlPanel() for node in nuke.allNodes(recurseGroups=True)], 'shift+C')

# tab menu scripts
toolbar = nuke.toolbar("Nodes")
toolbar.addCommand("nukepedia/scripts/TrackerToRoto", "tracker_to_node.main()")

# setup QUICK SHARE
if "QS_ROOT_PATH" in os.environ:
    import quick_share

    quick_share.QuickShare.set_root(os.getenv("QS_ROOT_PATH"))
    quick_share.QuickShare.set_prj(os.getenv("QS_PRJ_NAME"))
    quick_share.QuickShare.set_host(os.getenv("QS_HOST_NAME"))
    menubar = nuke.menu ('Nuke')
    menubar.addCommand ('Edit/hscripts/Quick Share',  'quick_share.QuickShare.quick_share()', 'Ctrl+Alt+C')
    menubar.addCommand ('Edit/hscripts/Quick Share Manager',  'quick_share.QuickShareManager().display()')

#___________________________________________________________________________________________________________________

# animation menu

m = nuke.menu("Animation")
m.addSeparator()
m.addCommand("$GUI", 'set_gui.gui_val()')

## knob defaults

nuke.knobDefault("Read.postage_stamp", "False")
nuke.knobDefault("CheckerBoard.postage_stamp", "False")
nuke.knobDefault("Constant.postage_stamp", "False")
nuke.knobDefault("ColorWheel.postage_stamp", "False")
nuke.knobDefault("ColorBars.postage_stamp", "False")
nuke.knobDefault("Views.views_colours true")
nuke.knobDefault("Tracker4.zoom_window_behaviour", "0")
nuke.knobDefault("Colorspace.label", "[value colorspace_in] -> [value colorspace_out]")
nuke.knobDefault("Write.channels", "rgba")
nuke.knobDefault("Roto.cliptype", "0")
nuke.knobDefault("RotoPaint.cliptype", "0")
nuke.knobDefault("Project3D2.crop", "0")

#___________________________________________________________________________________________________________________

nuke.menu("Nodes").addCommand("Channel/Shuffle(old)", "nuke.createNode('Shuffle')", icon="Shuffle.png")
nuke.menu("Nodes").addCommand("Channel/ShuffleCopy(old)", "nuke.createNode('ShuffleCopy')", icon="ShuffleCopy.png")
