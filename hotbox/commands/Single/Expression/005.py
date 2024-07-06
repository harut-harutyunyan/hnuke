#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Turn to Contrast
#
#----------------------------------------------------------------------------------------------------------


node = nuke.selectedNode()
if not node.knob("contrast"):
    node.resetKnobsToDefault()
    knob = nuke.Tab_Knob("cont_tab", "Contrast")
    node.addKnob(knob)
    knob = nuke.Double_Knob("contrast", "contrast")
    knob.setRange(.001, 3)
    knob.setValue(1)
    node.addKnob(knob)
    knob = nuke.Double_Knob("pivot", "pivot")
    knob.setValue(.18)
    node.addKnob(knob)
    node["temp_name0"].setValue("gamma")
    node["temp_expr0"].setValue("1/contrast")
    node["temp_name1"].setValue("mult")
    node["temp_expr1"].setValue("pow(pivot, 1-contrast)")
    node["expr0"].setValue("pow(r, 1/gamma) * mult")
    node["expr1"].setValue("pow(g, 1/gamma) * mult")
    node["expr2"].setValue("pow(b, 1/gamma) * mult")
    node.setName("Contrast")
    node["tile_color"].setValue(2057961471)
    knob = nuke.Text_Knob('div', '')
    node.addKnob(knob)
    knob = nuke.Link_Knob('maskChannelInput_01', 'mask')
    knob.setLink('this.maskChannelInput')
    node.addKnob(knob)
    knob = nuke.Link_Knob('unpremult_01', 'unpremult')
    knob.setLink('this.unpremult')
    node.addKnob(knob)
    knob = nuke.Link_Knob('mix_01', 'mix')
    knob.setLink('this.mix')
    node.addKnob(knob)