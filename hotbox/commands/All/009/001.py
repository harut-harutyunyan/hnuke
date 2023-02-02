#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Soft Key
# COLOR: #213221
#
#----------------------------------------------------------------------------------------------------------




if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
else:
    from PySide2 import QtWidgets

script = r'''set cut_paste_input [stack 0]
version 12.1 v5
BackdropNode {
 inputs 0
 name BackdropNode11
 tile_color 0x5a5b44ff
 label "soft key"
 note_font_size 42
 selected true
 xpos -1377
 ypos -762
 bdwidth 1954
 bdheight 1406
}
push $cut_paste_input
Dot {
 name Dot1
 label plate
 note_font_size 41
 selected true
 xpos -858
 ypos -609
}
set N14a8edb0 [stack 0]
Dot {
 name Dot42
 selected true
 xpos -1119
 ypos -609
}
clone node11d970d0|Expression|17560 Expression {
 temp_name0 limit
 temp_expr0 1
 expr1 g>(b+r)/2*limit?(b+r)/2*limit:g
 expr3 g-(r+b)*limit/2
 name despill_green1
 tile_color 0x6000ff
 selected true
 xpos -1153
 ypos -462
}
set C11d970d0 [stack 0]
Dot {
 name Dot25
 selected true
 xpos -1119
 ypos -137
}
set N11970020 [stack 0]
push $N14a8edb0
Merge2 {
 inputs 2
 operation from
 name Merge6
 selected true
 xpos -892
 ypos -141
}
Expression {
 channel0 rgb
 expr0 (r*weight.r)+(g*weight.g)+(b*weight.b)
 channel1 none
 channel2 none
 name Monochrome
 selected true
 xpos -892
 ypos -94
 addUserKnob {20 monochrome l Monochrome}
 addUserKnob {18 weight}
 weight {0.3 0.59 0.11}
}
Dot {
 name Dot4
 selected true
 xpos -858
 ypos 85
}
Constant {
 inputs 0
 channels rgb
 color {0.06191957369 0.1950115561 0.05874586105 1}
 name Constant1
 selected true
 xpos -673
 ypos -543
 postage_stamp false
}
Dot {
 inputs 0
 name Dot2
 label cleanplate
 note_font_size 41
 selected true
 xpos -529
 ypos -609
}
Switch {
 inputs 2
 name Switch4
 selected true
 xpos -563
 ypos -543
}
clone $C11d970d0 {
 xpos -563
 ypos -462
 selected true
}
Expression {
 channel0 rgb
 expr0 (r*weight.r)+(g*weight.g)+(b*weight.b)
 channel1 none
 channel2 none
 name Monochrome1
 selected true
 xpos -563
 ypos -146
 addUserKnob {20 monochrome l Monochrome}
 addUserKnob {18 weight}
 weight {0.3 0.59 0.11}
 addUserKnob {6 weight_panelDropped l "panel dropped state" -STARTLINE +HIDDEN}
}
set N11f32700 [stack 0]
Merge2 {
 inputs 2
 operation divide
 name Merge7
 selected true
 xpos -563
 ypos 81
}
Grade {
 whitepoint {0.7300000191 0.7300000191 0.7300000191 -1}
 name Grade10
 selected true
 xpos -563
 ypos 153
}
Dot {
 name Dot5
 selected true
 xpos -529
 ypos 300
}
push $N11f32700
Dot {
 name Dot7
 selected true
 xpos -367
 ypos -142
}
Grade {
 name Grade12
 selected true
 xpos -401
 ypos -96
}
Dot {
 name Dot6
 selected true
 xpos -367
 ypos -31
}
Dot {
 inputs 0
 name Dot3
 label bg
 note_font_size 41
 selected true
 xpos -135
 ypos -609
}
Merge2 {
 inputs 2
 operation from
 name Merge8
 selected true
 xpos -169
 ypos -35
}
Merge2 {
 inputs 2
 operation multiply
 name Merge14
 selected true
 xpos -169
 ypos 296
}
Dot {
 name Dot38
 selected true
 xpos -135
 ypos 448
}
push $N11970020
Dot {
 name Dot39
 selected true
 xpos -1119
 ypos 26
}
Dot {
 name Dot43
 selected true
 xpos 363
 ypos 26
}
Merge2 {
 inputs 2
 operation plus
 output rgb
 name Merge15
 selected true
 xpos 329
 ypos 444
}
Shuffle2 {
 fromInput1 {{0} B}
 fromInput2 {{0} B}
 mappings "4 rgba.red 0 0 rgba.red 0 0 rgba.green 0 1 rgba.green 0 1 rgba.blue 0 2 rgba.blue 0 2 white -1 -1 rgba.alpha 0 3"
 name Shuffle5
 selected true
 xpos 329
 ypos 568
}
StickyNote {
 inputs 0
 name StickyNote1
 tile_color 0xffbf00ff
 label "despill need to be cloned \nto cleanplate despill"
 note_font_size 14
 selected true
 xpos -1063
 ypos -471
}
StickyNote {
 inputs 0
 name StickyNote2
 tile_color 0xffbf00ff
 label "sample with whitepoint to make screen white\ntweak further to match bg"
 selected true
 xpos -464
 ypos 153
}
StickyNote {
 inputs 0
 name StickyNote3
 tile_color 0xffbf00ff
 label "tweak to match bg"
 selected true
 xpos -308
 ypos -96
}
'''


clipboard = QtWidgets.QApplication.clipboard()
clipboard.setText(script)
nuke.nodePaste('%clipboard%')
