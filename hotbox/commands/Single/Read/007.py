#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: DMP Layers
#
#----------------------------------------------------------------------------------------------------------

n=nuke.selectedNode()

inc = 0
mrg = None
last = None
for f in range (n.frameRange().first(), n.frameRange().last()+1):
    fh = nuke.nodes.FrameHold(first_frame=f)
    fh.setInput(0, n)
    fh["postage_stamp"].setValue(1)
    fh.setXYpos(n.xpos()+inc, n.ypos()+100)

    inc+=100
    if not mrg:
        if not last:
            last = fh
            continue
        mrg = nuke.nodes.Merge2(operation="under")
        mrg.setInput(1, last)
    if mrg:
        mrg.setInput(0, fh)
        last = mrg
        mrg = None
