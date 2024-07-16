#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Backdrop
# COLOR: #522531
#
#----------------------------------------------------------------------------------------------------------

import nukescripts

def create_backdrop_with_margins(margin=100):
    # Create the backdrop
    bd = nukescripts.autobackdrop.autoBackdrop()

    # Get the position and size of the backdrop
    x = bd['bdwidth'].value()
    y = bd['bdheight'].value()

    # Apply margins
    bd['bdwidth'].setValue(x + 2 * margin)
    bd['bdheight'].setValue(y + 2 * margin)
    bd['xpos'].setValue(bd['xpos'].value() - margin)
    bd['ypos'].setValue(bd['ypos'].value() - margin)
    
    return bd

bd = create_backdrop_with_margins()
col = 3149642751
bd["tile_color"].setValue(col)
bd["appearance"].setValue(1)
bd["border_width"].setValue(4)
txt = nuke.getInput("Change label", "")
if txt:
    bd["label"].setValue("<center><font size=5 color=white><b>"+txt)
    bd["note_font"].setValue("Arial")