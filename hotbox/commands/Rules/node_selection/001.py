#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Backdrop
# COLOR: #522531
#
#----------------------------------------------------------------------------------------------------------

import nukescripts

col = nuke.getColor(858993663)
bd = nukescripts.autobackdrop.autoBackdrop()
bd["tile_color"].setValue(col)
bd["appearance"].setValue(1)
txt = nuke.getInput("Change label", "")
if txt:
    bd["label"].setValue("<center>"+txt)
    bd["note_font"].setValue("Arial")