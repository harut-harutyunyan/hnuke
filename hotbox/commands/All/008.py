#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Set to Alpha
# COLOR: #593d52
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    knob = node.knob("channels")
    if knob:
        knob.setValue("alpha")
    if node.Class() == "Grade":
        node["white_clamp"].setValue(1)
        node["black_clamp"].setValue(1)
