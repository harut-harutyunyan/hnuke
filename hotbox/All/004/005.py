#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Keylight
#
#----------------------------------------------------------------------------------------------------------

kl = nuke.createNode("Keylight", inpanel=False)
gr = nuke.createNode("Grade", inpanel=False)
gr["channels"].setValue("alpha")
gr["white_clamp"].setValue(1)
gr.setInput(0, kl)
gr.setXYpos(kl.xpos(), kl.ypos()+kl.screenHeight()+25)