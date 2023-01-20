#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Despill Blue
# COLOR: #002660
#
#----------------------------------------------------------------------------------------------------------

node = nuke.selectedNode()
node.resetKnobsToDefault()
node["temp_name0"].setValue("limit")
node["temp_expr0"].setValue("1")
node["expr2"].setValue("b>(g+r)/2*limit?(g+r)/2*limit:b")
node["expr3"].setValue("b-(r+g)*limit/2")
node["tile_color"].setValue(2515199)
node.setName("despill_green")
