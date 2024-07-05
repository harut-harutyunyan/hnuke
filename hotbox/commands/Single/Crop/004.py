#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Crop Padded
#
#----------------------------------------------------------------------------------------------------------

sel = nuke.selectedNodes()

for crop in sel:
    crop.setName("CropPadded1")
    
    knob = nuke.Tab_Knob('cropPadded', 'CropPadded')
    crop.addKnob(knob)
    knob = nuke.WH_Knob('padding', 'Padding')
    knob.setValue(100)
    crop.addKnob(knob)
    knob = nuke.Link_Knob('box_01', 'box')
    knob.setLink('this.box')
    crop.addKnob(knob)
    knob = nuke.Boolean_Knob('always_root', 'Root Format')
    crop.addKnob(knob)
    crop.knob("box").setExpression('-padding.w', 0)
    crop.knob("box").setExpression('-padding.h', 1)
    crop.knob("box").setExpression('([exists input0]&&!always_root?input.width:root.width)+padding.w', 2)
    crop.knob("box").setExpression('([exists input0]&&!always_root?input.height:root.height)+padding.h', 3)