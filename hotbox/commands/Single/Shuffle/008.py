#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Value In
#
#----------------------------------------------------------------------------------------------------------

sel = nuke.selectedNodes()

for node in sel:
    node["label"].setValue("<font size=5 color='orange'><b>[value in]</b></font>")