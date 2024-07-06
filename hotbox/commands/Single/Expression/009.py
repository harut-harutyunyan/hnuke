#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Turn to pNoise
#
#----------------------------------------------------------------------------------------------------------

sel = nuke.selectedNodes()

for node in sel:
    #node = nuke.createNode("Expression")
    node.setName("pNoise1")
    sel = nuke.selectedNodes()
    
    knob = nuke.Tab_Knob('pNoise', 'pNoise')
    node.addKnob(knob)
    
    knob = nuke.Enumeration_Knob('type', 'type', ['turbulence', 'fBm'])
    node.addKnob(knob)
    knob = nuke.Text_Knob('div0', '')
    node.addKnob(knob)
    knob = nuke.XYZ_Knob('scale', 'scale')
    knob.setValue(1)
    node.addKnob(knob)
    knob = nuke.Double_Knob('scale_uni', 'uniform scale')
    knob.setRange(0.1, 100)
    knob.setValue(10)
    node.addKnob(knob)
    knob = nuke.XYZ_Knob('offset', 'offset')
    node.addKnob(knob)
    knob = nuke.Text_Knob('div1', '')
    node.addKnob(knob)
    knob = nuke.Int_Knob('octaves', 'octaves')
    knob.setValue(6)
    node.addKnob(knob)
    knob = nuke.Double_Knob('lacunarity', 'lacunarity')
    knob.setValue(2)
    knob.setRange(1, 10)
    node.addKnob(knob)
    knob = nuke.Double_Knob('gain', 'gain')
    knob.setValue(0.5)
    node.addKnob(knob)
    knob = nuke.Double_Knob('gamma', 'gamma')
    knob.setValue(0.5)
    node.addKnob(knob)
    node.knob("expr3").setValue("clamp(pow([value type]((r+offset.x)/scale.x/scale_uni, (g+offset.y)/scale.y/scale_uni, (b+offset.z)/scale.z/scale_uni, octaves, lacunarity, gain), 1/gamma))")