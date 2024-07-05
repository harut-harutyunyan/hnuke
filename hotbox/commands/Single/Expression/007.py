#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Turn to EasyBlacks
#
#----------------------------------------------------------------------------------------------------------

sel = nuke.selectedNodes()

for node in sel:
    
    node.setName("EasyBlacks1")
    node["tile_color"].setValue(2057961471)
    
    knob = nuke.Tab_Knob('blackPoint', 'Black Point')
    node.addKnob(knob)
    knob = nuke.Color_Knob('bp', 'src_blacks')
    node.addKnob(knob)
    knob = nuke.Boolean_Knob('clamp_blacks', 'clamp')
    knob.setValue(1)
    node.addKnob(knob)
    knob = nuke.Text_Knob('div', '')
    node.addKnob(knob)
    knob = nuke.Color_Knob('col', 'blackpoint')
    node.addKnob(knob)
    
    node.knob("temp_name0").setValue("rr")
    node.knob("temp_name1").setValue("gg")
    node.knob("temp_name2").setValue("bb")
    node.knob("temp_expr0").setValue("clamp_blacks?max(((r - bp.r) / (1 - bp.r)), 0):((r - bp.r) / (1 - bp.r))")
    node.knob("temp_expr1").setValue("clamp_blacks?max(((g - bp.g) / (1 - bp.g)), 0):((g - bp.g) / (1 - bp.g))")
    node.knob("temp_expr2").setValue("clamp_blacks?max(((b - bp.b) / (1 - bp.b)), 0):((b - bp.b) / (1 - bp.b))")
    node.knob("expr0").setValue("1 - (1 - col.r) * (1 - rr)")
    node.knob("expr1").setValue("1 - (1 - col.g) * (1 - gg)")
    node.knob("expr2").setValue("1 - (1 - col.b) * (1 - bb)")

    knob = nuke.Text_Knob('div', '')
    node.addKnob(knob)
    knob = nuke.Link_Knob('unpremult_01', 'unpremult')
    knob.setLink('this.unpremult')
    node.addKnob(knob)
    knob = nuke.Link_Knob('mix_01', 'mix')
    knob.setLink('this.mix')
    node.addKnob(knob)