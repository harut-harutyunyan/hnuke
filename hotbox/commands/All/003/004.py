#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: GUI Switch
#
#----------------------------------------------------------------------------------------------------------

def create_switch():
    grp = nuke.nodes.Group(tile_color = 4283782655)
    grp.setName("gui_switch")
    grp.begin()
    inpt1 = nuke.nodes.Input(name="render")
    inpt2 = nuke.nodes.Input(name="work")
    sw = nuke.nodes.Switch()
    sw["which"].setExpression("[python not nuke.executing()]")
    sw.setInput(0, inpt1)
    sw.setInput(1, inpt2)
    output = nuke.nodes.Output()
    output.setInput(0, sw)
    grp.end()

    return grp


node = nuke.selectedNode()

dot = nuke.nodes.Dot()
sw = create_switch()
sw.setXYpos(node.xpos(), node.ypos()+node.screenHeight()*2)
dot.setInput(0, node.input(0))
dot.setXYpos(node.xpos()-5+int(node.screenWidth()/2), node.ypos()-node.screenHeight())
node.setXpos(node.xpos()+node.screenWidth())
node.setInput(0, dot)
sw.setInput(0, node)
sw.setInput(1, dot)



dependent = nuke.dependentNodes(nuke.INPUTS | nuke.HIDDEN_INPUTS, node)
for n in dependent:
    for i in range(n.inputs()):
        if n.input(i) == node:
            n.setInput(i, sw)
            continue
