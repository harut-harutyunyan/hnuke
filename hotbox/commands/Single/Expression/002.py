#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Despill Green
# COLOR: #006000
#
#----------------------------------------------------------------------------------------------------------

node = nuke.selectedNode()
node.resetKnobsToDefault()
node["temp_name0"].setValue("limit")
node["temp_expr0"].setValue("1")
node["expr1"].setValue("g>(b+r)/2*limit?(b+r)/2*limit:g")
node["expr3"].setValue("g-(r+b)*limit/2")
node["tile_color"].setValue(6291711)
node.setName("despill_green")
