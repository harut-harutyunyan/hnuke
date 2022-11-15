#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: New Look
# COLOR: #222222
# TEXTCOLOR: #ff5555
#
#----------------------------------------------------------------------------------------------------------

from look_manager import LookManagerUtil


look_name = nuke.getInput('Look Name','')
if look_name != None:
    look_name=look_name.replace("`", "")
    for node in nuke.selectedNodes():
        LookManagerUtil.add_look(node, tooltip=look_name)