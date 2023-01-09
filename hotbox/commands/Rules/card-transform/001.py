#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Card 3D
# COLOR: #9c0000
# TEXTCOLOR: #111111
#
#----------------------------------------------------------------------------------------------------------



import math


def list_chain(node, chain):
    if node.Class() in ["Card", "Card2"]:
        chain.append(node)
        return chain
    if node.Class() == "TransformGeo":
        if not node.input(0):
            del ch[:]
            return
        if node.input(1):
            chain.append(node.input(1))
        chain.append(node)
        return list_chain(node.input(0), chain)

def get_matrix(node, world=""):
    matrix = nuke.math.Matrix4()
    for i in range(0, 16):
        matrix[i] = node['{}matrix'.format(world)].valueAt(nuke.frame())[i]
    return matrix

sel = nuke.selectedNode()
ch = []
list_chain(sel, ch)

if ch:
    ch.reverse()

    card = ch.pop(0)

    matrix = get_matrix(card)

    for node in ch:
        if node.Class() in ["Axis", "Axis1", "Axis2"]:
            node_matrix = get_matrix(node, "world_")
        else:
            node_matrix = get_matrix(node)

        matrix *= node_matrix


    axis_result = nuke.createNode("Axis", inpanel=False)
    axis_result["useMatrix"].setValue(True)
    axis_result.setXYpos(sel.xpos()+150, sel.ypos())
    card3d = nuke.createNode("Card3D", inpanel=False)
    card3d["translate"].setValue(0)
    card3d.setXYpos(sel.xpos()+150, sel.ypos()+100)
    card3d.setInput(0, card.input(0))
    card3d.setInput(2, axis_result)
    for i in range(0, 16):
        axis_result['matrix'].setValueAt(matrix[i], nuke.frame(), i)
