#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Turn to Monochrome
#
#----------------------------------------------------------------------------------------------------------

node = nuke.selectedNode()
if not node.knob("weight"):
    node.resetKnobsToDefault()
    knob = nuke.Tab_Knob("monochrome", "Monochrome")
    node.addKnob(knob)
    knob = nuke.Color_Knob("weight", "weight")
    knob.setValue([0.3, 0.59, 0.11])
    node.addKnob(knob)
    node["channel0"].setValue("rgb")
    node["expr0"].setValue("(r*weight.r)+(g*weight.g)+(b*weight.b)")
    node["channel1"].setValue("none")
    node["channel2"].setValue("none")
    node.setName("Monochrome")
