#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Alpha
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('in1').setValue('alpha')
    i.knob('mappings').setValue([(0, 'rgba.alpha', 'rgba.red'), (0, 'rgba.alpha', 'rgba.green'), (0, 'rgba.alpha', 'rgba.blue'), (0, 'rgba.alpha', 'rgba.alpha')])

    i.knob('tile_color').setValue(4278124287)
