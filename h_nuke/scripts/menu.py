import os
import nuke


import W_smartAlign
import W_hotbox, W_hotboxManager
import dDot
import gizmo_loader
import W_smartAlign

# knob defaults
nuke.knobDefault("Read.postage_stamp", "False")
nuke.knobDefault("CheckerBoard.postage_stamp", "False")
nuke.knobDefault("Constant.postage_stamp", "False")
nuke.knobDefault("ColorWheel.postage_stamp", "False")
nuke.knobDefault("ColorBars.postage_stamp", "False")
nuke.knobDefault("Views.views_colours true")
nuke.knobDefault("Tracker4.zoom_window_behaviour", "0")
nuke.knobDefault("Colorspace.label", "[value colorspace_in] -> [value colorspace_out]")
