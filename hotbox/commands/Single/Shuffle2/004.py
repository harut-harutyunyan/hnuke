#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Solid Alpha
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('in1').setValue('rgba')
    i.knob('mappings').setValue([(0, 'rgba.red', 'rgba.red'), (0, 'rgba.green', 'rgba.green'), (0, 'rgba.blue', 'rgba.blue'), (-1, 'white', 'rgba.alpha')])

    i.knob('tile_color').setValue(4278124287)
