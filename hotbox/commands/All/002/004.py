#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Double Erode
#
#----------------------------------------------------------------------------------------------------------

e1 = nuke.createNode("FilterErode", inpanel=False)
e1.setName("FilterErode_Shrink")
e1["size"].setValue(3)
e2 = nuke.createNode("FilterErode", inpanel=False)
e2.setName("FilterErode_Grow")
e2["size"].setExpression("input.size*-1")
e2.setInput(0, e1)
e2.setXYpos(e1.xpos(), e1.ypos()+e1.screenHeight()+25)
cl = nuke.createNode("Clamp", inpanel=False)
cl.setInput(0, e2)
cl.setXYpos(e2.xpos(), e2.ypos()+e2.screenHeight()+45)
cl["channels"].setValue("alpha")
