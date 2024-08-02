#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: EasyWrite
#
#----------------------------------------------------------------------------------------------------------




if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
else:
    from PySide2 import QtWidgets

script = r'''set cut_paste_input [stack 0]
version 13.2 v5
push $cut_paste_input
Write {
 file "\[regsub -all \"/\[lrange \[split \[knob \[topnode].file] .] end 2]/\" \[join \[lrange \[split \[value \[topnode].file] .] 0 end-2] .] \"/mov/\"].mov"
 colorspace "Output - Rec.709"
 file_type mov
 mov64_format "mov (QuickTime / MOV)"
 mov64_codec appr
 mov_prores_codec_profile "ProRes 4:2:2 Proxy 10-bit"
 mov_h264_codec_profile "High 4:2:0 8-bit"
 mov64_pixel_format {{0}}
 mov64_quality High
 mov64_fast_start true
 mov64_write_timecode true
 mov64_gop_size 12
 mov64_b_frames 0
 mov64_bitrate 20000
 mov64_bitrate_tolerance 4000000
 mov64_quality_min 1
 mov64_quality_max 3
 create_directories true
 checkHashOnRead false
 version 38
 name Write2
 selected true
 xpos 288
 ypos -901
}
'''


clipboard = QtWidgets.QApplication.clipboard()
clipboard.setText(script)
nuke.nodePaste('%clipboard%')
        