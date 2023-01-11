#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Log-Lin
# COLOR: #d1d1ee
# TEXTCOLOR: #111111
#
#----------------------------------------------------------------------------------------------------------

sel = nuke.selectedNodes()
if sel:
    sel = sel[0]
    dependent = nuke.dependentNodes(nuke.INPUTS | nuke.HIDDEN_INPUTS, sel)

    if nuke.Root()["colorManagement"].getValue() > 0:
        node_class = "OCIOLogConvert"
    else:
        node_class = "Log2Lin"
    
    lin_log = nuke.createNode(node_class, inpanel=False)
    lin_log["operation"].setValue(1)
    lin_log.setName(node_class+"_to_LOG")
    log_lin = nuke.createNode(node_class, inpanel=False)
    log_lin.setName(node_class+"_to_LIN")
    
    for n in dependent:
        for i in range(n.inputs()):
            if n.input(i) == sel:
                n.setInput(n, log_lin)
                continue
    lin_log.setInput(0, sel.input(0))
    sel.setInput(0, lin_log)
    log_lin.setInput(0, sel)
    lin_log.setXYpos(sel.xpos(), sel.ypos()-(15+sel.screenHeight()))
    log_lin.setXYpos(sel.xpos(), sel.ypos()+(15+sel.screenHeight()))
    