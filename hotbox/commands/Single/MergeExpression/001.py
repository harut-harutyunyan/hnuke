#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: DifferenceClamped
#
#----------------------------------------------------------------------------------------------------------


sel = nuke.selectedNodes()
for node in sel:
    #node = nuke.createNode("MergeExpression")
    node.setName("DifferenceClamped1")
    
    knob = nuke.Tab_Knob('diffclamp', 'Difference')
    node.addKnob(knob)
    knob = nuke.Double_Knob('threshold', 'threshold')
    node.addKnob(knob)
    node.knob("temp_name0").setValue("trsh")
    node.knob("temp_expr0").setValue("max(threshold/10, 0)")
    node.knob("expr3").setValue("(abs(Ar - Br) > trsh || abs(Ag - Bg) > trsh || abs(Ab - Bb) > trsh) ? 1 : 0")