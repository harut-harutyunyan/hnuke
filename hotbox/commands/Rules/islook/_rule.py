#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# IGNORE CLASSES: 0
#
#----------------------------------------------------------------------------------------------------------

sel = nuke.selectedNodes()
if sel:
    ret = sel[0].knob("__look_n_1")
else:
    ret = False