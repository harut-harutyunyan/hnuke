#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Toggle
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob("operation").setValue(int(1-i.knob("operation").getValue()))
