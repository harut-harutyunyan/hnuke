#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# IGNORE CLASSES: 0
#
#----------------------------------------------------------------------------------------------------------

if nuke.selectedNodes():
    ret = nuke.selectedNode().Class() in ["Card", "Card2", "TransformGeo"]
else:
    ret = False
