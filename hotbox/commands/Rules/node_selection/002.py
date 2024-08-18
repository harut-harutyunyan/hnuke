#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: DOT
# COLOR: #ff9455
# TEXTCOLOR: #111111
#
#----------------------------------------------------------------------------------------------------------

*vars, to_node, from_node = nuke.selectedNodes()


for n in nuke.selectedNodes():
    n["selected"].setValue(False)

from_node["selected"].setValue(True)
dot = nuke.createNode("Dot", inpanel=False)
dot.setXYpos(dot.xpos(), to_node.ypos())