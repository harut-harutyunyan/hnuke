#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Union
#
#----------------------------------------------------------------------------------------------------------

cm = nuke.createNode("ChannelMerge", inpanel=False)
cm["operation"].setValue("union")