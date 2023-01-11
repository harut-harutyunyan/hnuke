#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Card3D linked
# COLOR: #527c52
# TEXTCOLOR: #111111
#
#----------------------------------------------------------------------------------------------------------

card = nuke.selectedNode()
card3d = nuke.createNode("Card3D", inpanel=False)
card3d.setName("{}_to_Card3D".format(card.name()))
card3d["useMatrix"].setValue(1)
card3d["matrix"].setExpression("parent.{}.matrix".format(card.name()))
card3d.setXYpos(card.xpos()+120, card.ypos())
card3d.setInput(0, card.input(0))
