#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Version Up
#
#----------------------------------------------------------------------------------------------------------

import os
import nukescripts

for i in nuke.selectedNodes():
    file_string = i.knob('file').value()

    cur_version = nukescripts.version_get(file_string, 'v')[-1]
    if cur_version:
        new_version = int(cur_version)+1
    new_file_string = file_string.replace(cur_version, format(new_version, '03'))
    if os.path.exists(new_file_string.replace("%04d", str(i['first'].value()))):
        i.knob('file').setValue(new_file_string)
