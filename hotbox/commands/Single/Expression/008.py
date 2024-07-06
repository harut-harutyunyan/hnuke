#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Turn to TempTint
#
#----------------------------------------------------------------------------------------------------------

sel = nuke.selectedNodes()

for node in sel:
    #node = nuke.createNode("Expression")
    node.setName("TempTint1")
    node["tile_color"].setValue(2057961471)
    
    knob = nuke.Tab_Knob('tempTint', 'Temp Tint')
    node.addKnob(knob)
    knob = nuke.Double_Knob('temp', 'Temperature <font color=#E6E6A1><sup>◄</sup></font><font color=#A1E6E6><sub>►</sub></font>')
    knob.setRange(-1,1)
    node.addKnob(knob)
    
    knob = nuke.Double_Knob('tint', 'Tint <font color=#A1E6A1><sup>◄</sup></font><font color=#E6A1A1><sub>►</sub></font>')
    knob.setRange(-1,1)
    node.addKnob(knob)
    
    knob = nuke.Double_Knob('intens', 'Intensity <font color=#FFFFFF><sup>◄</sup></font><font color=#AAAAAA><sub>►</sub></font>')
    knob.setRange(0,2)
    knob.setValue(1)
    node.addKnob(knob)
    
    knob = nuke.Boolean_Knob('clamp_blacks', "Clamp Blacks")
    knob.setFlag(nuke.STARTLINE)
    knob.setValue(1)
    node.addKnob(knob)
    
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
    
    
    node.knob("expr0").setValue("clamp_blacks?max(((r*(1-temp/2))*(1+tint/3))*intens, 0):((r*(1-temp/2))*(1+tint/3))*intens")
    node.knob("expr1").setValue("clamp_blacks?max((g*(1-tint*2/3))*intens, 0):(g*(1-tint*2/3))*intens")
    node.knob("expr2").setValue("clamp_blacks?max(((b*(1+temp/2))*(1+tint/3))*intens, 0):((b*(1+temp/2))*(1+tint/3))*intens")