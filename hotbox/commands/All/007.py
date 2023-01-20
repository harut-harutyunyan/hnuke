#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Set Color
#
#----------------------------------------------------------------------------------------------------------

sel = nuke.selectedNodes()
if sel:
    col = nuke.getColor()
    for node in sel:
        node["tile_color"].setValue(col)