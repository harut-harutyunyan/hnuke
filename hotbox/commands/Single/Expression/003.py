#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Despill Blue
# COLOR: #002660
#
#----------------------------------------------------------------------------------------------------------

node = nuke.selectedNode()
if not node.knob("lm"):
    node.resetKnobsToDefault()
    knob = nuke.Tab_Knob("despill", "Despill")
    node.addKnob(knob)
    knob = nuke.Boolean_Knob("lm", "luma compensate")
    knob.setValue(1)
    node.addKnob(knob)
    knob = nuke.Double_Knob("limit", "fine tune")
    knob.setValue(.95)
    node.addKnob(knob)
    node["temp_name0"].setValue("desp")
    node["temp_expr0"].setValue("b>(g+r)/2*limit?(g+r)/2*limit:b")
    node["temp_name1"].setValue("mono")
    node["temp_expr1"].setValue("(b-desp)*.11")
    node["expr0"].setValue("lm==1?mono+r:r")
    node["expr1"].setValue("lm==1?mono+g:g")
    node["expr2"].setValue("lm==1?mono+desp:desp")
    node["expr3"].setValue("g-(r+b)*limit/2")
    node["tile_color"].setValue(745727)
    node.setName("despill_blue")
