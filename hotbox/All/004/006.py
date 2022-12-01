#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Split RGB
#
#----------------------------------------------------------------------------------------------------------

sel = nuke.selectedNodes()
if sel:
    sel = sel[0]
    chs = ["red", "green", "blue", "alpha"]
    shuffles = [nuke.createNode("Shuffle", inpanel=False) for s in range(3)]
    cc = [3422552319, 13369599, 52479]
    xpos = 0
    for i, sh in enumerate(shuffles):
        for ch in chs:
            sh[ch].setValue(chs[i])
        sh["label"].setValue(chs[i][0].upper()*6)
        sh["tile_color"].setValue(cc[i])
        sh.setInput(0, sel)
        sh.setXYpos(sel.xpos()+xpos, sel.ypos()+75)
        xpos += 120