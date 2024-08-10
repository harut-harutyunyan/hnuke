#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: chromatic
# COLOR: #590058
#
#----------------------------------------------------------------------------------------------------------




if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
else:
    from PySide2 import QtWidgets

script = r'''set cut_paste_input [stack 0]
version 13.2 v5
push 0
add_layer {chroma_alpha chroma_alpha.red chroma_alpha.green chroma_alpha.blue}
Shuffle {
 in alpha
 in2 rgb
 green red
 blue red
 out chroma_alpha
 name Shuffle2
 label "<font size=5 color='orange'><b>\[value out]</b></font>"
 selected true
 xpos -250
 ypos -72
}
GodRays {
 channels {rgba.red -rgba.green -rgba.blue chroma_alpha.red}
 scale 1.02
 center {{input.width/2} {input.height/2}}
 name GodRays1
 tile_color 0xff5555ff
 selected true
 xpos -250
 ypos 4
}
GodRays {
 channels {-rgba.red rgba.green -rgba.blue chroma_alpha.green}
 center {{input.width/2} {input.height/2}}
 name GodRays3
 tile_color 0x6aff55ff
 selected true
 xpos -250
 ypos 53
}
GodRays {
 channels {-rgba.red -rgba.green rgba.blue chroma_alpha.blue}
 scale 0.98
 center {{input.width/2} {input.height/2}}
 name GodRays2
 tile_color 0x9fffff
 selected true
 xpos -250
 ypos 103
}
Dot {
 name Dot2
 selected true
 xpos -216
 ypos 165
}
push $cut_paste_input
Dot {
 name Dot1
 selected true
 xpos -23
 ypos -72
}
MergeExpression {
 inputs 2
 expr0 Br*(1-A.chroma_alpha.red)+Ar
 expr1 Bg*(1-A.chroma_alpha.green)+Ag
 expr2 Bb*(1-A.chroma_alpha.blue)+Ab
 name ChromaMerge
 note_font Arial
 selected true
 xpos -57
 ypos 161
}
'''


clipboard = QtWidgets.QApplication.clipboard()
clipboard.setText(script)
nuke.nodePaste('%clipboard%')
        