#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Depth
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('in1').setValue('depth')
    i.knob('mappings').setValue([(0, 'depth.Z', 'rgba.red'), (0, 'depth.Z', 'rgba.green'), (0, 'depth.Z', 'rgba.blue'), (0, 'depth.Z', 'rgba.alpha')])
    i.knob('tile_color').setValue(2130739199)
