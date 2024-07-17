#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Frequency Separation
#
#----------------------------------------------------------------------------------------------------------


if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
else:
    from PySide2 import QtWidgets

script = r'''set cut_paste_input [stack 0]
version 13.2 v5
BackdropNode {
 inputs 0
 name BackdropNode1
 tile_color 0xaaaaaaff
 label "<center><font size=5 color=white><b>FREQUENCY SEPARATION"
 note_font Arial
 note_font_size 42
 selected true
 xpos -562
 ypos -553
 appearance Border
 border_width 4
 bdwidth 812
 bdheight 1028
}
push $cut_paste_input
NoOp {
 name image_in
 selected true
 xpos 60
 ypos -421
}
Dot {
 name Dot1
 selected true
 xpos 94
 ypos -323
}
set N88b6e000 [stack 0]
Dot {
 name Dot2
 selected true
 xpos -418
 ypos -323
}
push $N88b6e000
Blur {
 channels rgb
 size 5
 name Blur1
 label "\[value channels]-size \[value size]"
 selected true
 xpos 60
 ypos -223
}
set Nc3661800 [stack 0]
Merge2 {
 inputs 2
 operation divide
 output {rgba.red rgba.green rgba.blue -rgba.alpha}
 name Merge1
 selected true
 xpos -452
 ypos -217
}
Dot {
 name Dot4
 label "high frq"
 selected true
 xpos -418
 ypos 36
}
Dot {
 name Dot3
 selected true
 xpos -418
 ypos 299
}
push $Nc3661800
Dot {
 name Dot5
 label "low frq"
 selected true
 xpos 94
 ypos 36
}
Merge2 {
 inputs 2
 operation multiply
 output {rgba.red rgba.green rgba.blue -rgba.alpha}
 name Merge2
 selected true
 xpos 60
 ypos 295
}
NoOp {
 name image_out
 selected true
 xpos 60
 ypos 391
}
'''


clipboard = QtWidgets.QApplication.clipboard()
clipboard.setText(script)
nuke.nodePaste('%clipboard%')
        