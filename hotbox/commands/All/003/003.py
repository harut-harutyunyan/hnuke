#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Unpremult/Premult
# COLOR: #744984
#
#----------------------------------------------------------------------------------------------------------

nn = nuke.selectedNode()
p = nuke.createNode("Unpremult", inpanel=False)
p.setInput(0, nn)
p.setXYpos(nn.xpos(), nn.ypos()+60)
u = nuke.createNode("Premult", inpanel=False)
u.setXYpos(p.xpos(), p.ypos()+150)
u.setInput(0, p)