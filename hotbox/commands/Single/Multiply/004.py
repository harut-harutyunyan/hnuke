#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Switch
#
#----------------------------------------------------------------------------------------------------------

script = """
n = nuke.thisNode()
k = nuke.thisKnob()

col = [4278190335, 536805631]
ss = ["<font size = 5> OFF", "<font size = 5> ON"]
if k.name() == "disable":
    val = 1-n["value"].getValue()
    n["value"].setValue(val)
    n["tile_color"].setValue(col[int(val)])
    n["label"].setValue(ss[int(val)])
    k.setValue(0)
"""

for mm in nuke.selectedNodes():
    mm["knobChanged"].setValue(script)