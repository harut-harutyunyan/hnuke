#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Red
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('in1').setValue('rgba')
    i.knob('mappings').setValue([(0, 'rgba.red', 'rgba.red'), (0, 'rgba.red', 'rgba.green'), (0, 'rgba.red', 'rgba.blue'), (0, 'rgba.red', 'rgba.alpha')])

    i.knob('tile_color').setValue(3204448511)
