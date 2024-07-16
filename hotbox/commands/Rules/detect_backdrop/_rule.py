#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# IGNORE CLASSES: 0
#
#----------------------------------------------------------------------------------------------------------

if len(nuke.selectedNodes()) > 1:
    ret = bool([n for n in nuke.selectedNodes() if n.Class()=="BackdropNode"])