#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Blue
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('in1').setValue('rgba')
    i.knob('mappings').setValue([(0, 'rgba.blue', 'rgba.red'), (0, 'rgba.blue', 'rgba.green'), (0, 'rgba.blue', 'rgba.blue'), (0, 'rgba.blue', 'rgba.alpha')])

    i.knob('tile_color').setValue(4177919)
