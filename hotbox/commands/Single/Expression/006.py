#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Turn to Unpremult
#
#----------------------------------------------------------------------------------------------------------

node = nuke.selectedNode()
node.resetKnobsToDefault()
node["expr0"].setValue("r>0?r/a:0")
node["expr1"].setValue("g>0?g/a:0")
node["expr2"].setValue("b>0?b/a:0")
node["expr3"].setValue("a>0?1:0")
node.setName("Unpremult")