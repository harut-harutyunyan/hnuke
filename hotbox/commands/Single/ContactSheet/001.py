#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: AutoContactSheet
# COLOR: #822f8e
# TEXTCOLOR: #111111
#
#----------------------------------------------------------------------------------------------------------

node = nuke.selectedNode()
if not node.knob("res_scale"):
    node.resetKnobsToDefault()
    knob = nuke.Tab_Knob("auto", "AutoContactSheet")
    node.addKnob(knob)
    knob = nuke.Double_Knob("res_scale", "resolution scale")
    knob.setRange(.2, 1)
    knob.setValue(.5)
    node.addKnob(knob)
    knob = nuke.Enumeration_Knob("widetall", "wide/tall", ["wide", "tall"])
    node.addKnob(knob)
    node["width"].setExpression("width*columns*res_scale")
    node["height"].setExpression("height*rows*res_scale")
    node["rows"].setExpression("widetall == 0 ?  rint(inputs**.5) : ceil(inputs**.5)")
    node["columns"].setExpression("widetall == 0 ? ceil(inputs**.5) : rint(inputs**.5)")
    node.setName("autoContactSheet")
    node["tile_color"].setValue(4278255615)
