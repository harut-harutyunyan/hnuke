#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Stencil
#
#----------------------------------------------------------------------------------------------------------

sel = nuke.selectedNodes()
if len(sel) == 1:
    if sel[0].Class()=="ChannelMerge":
        cm = sel[0]
    else:
        cm = nuke.createNode("ChannelMerge", inpanel=False)
else:
    cm = nuke.createNode("ChannelMerge", inpanel=False)
cm["operation"].setValue("stencil")
