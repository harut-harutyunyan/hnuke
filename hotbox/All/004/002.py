#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Stencil
#
#----------------------------------------------------------------------------------------------------------

cm = nuke.createNode("ChannelMerge", inpanel=False)
cm["operation"].setValue("stencil")