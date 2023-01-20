#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Turn to Exposure
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    if node.knob("stops"):
        continue
    knob = nuke.Tab_Knob("exposure", "Exposure")
    node.addKnob(knob)
    knob = nuke.Double_Knob("stops", "stops")
    knob.setRange(-4, 4)
    node.addKnob(knob)
    node["value"].setExpression("pow(2, stops)")
    node["channels"].setValue("rgb")
    node.setName("Exposure")
