#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: minus erode
#
#----------------------------------------------------------------------------------------------------------

er = nuke.createNode("FilterErode", inpanel=False)

er.setInput(0, nuke.selectedNode())
er["size"].setExpression("input.size*-1")