#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: ViewerInput
#
#----------------------------------------------------------------------------------------------------------




if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
else:
    from PySide2 import QtWidgets

script = r'''set cut_paste_input [stack 0]
version 13.2 v5
push $cut_paste_input
Group {
 name VIEWER_INPUT
 selected true
 xpos 222
 ypos -114
 hide_input true
 addUserKnob {20 User}
 addUserKnob {6 bw l BW +STARTLINE}
 addUserKnob {6 saturate l Saturate +STARTLINE}
 addUserKnob {6 blur l Blur +STARTLINE}
 addUserKnob {6 drk l Darker +STARTLINE}
 addUserKnob {6 brt l Brighter +STARTLINE}
 addUserKnob {26 mirror}
 addUserKnob {41 flip l "vertical (flip)" T Mirror2_1.flip}
 addUserKnob {41 flop l "horizontal (flop)" -STARTLINE T Mirror2_1.flop}
}
 Input {
  inputs 0
  name Input1
  xpos 0
 }
 Saturation {
  saturation 0
  name Saturation1
  xpos 0
  ypos 86
  disable {{1-bw}}
 }
 Saturation {
  saturation 5
  name Saturation2
  xpos 0
  ypos 112
  disable {{1-saturate}}
 }
 Blur {
  size 200
  name Blur1
  xpos 0
  ypos 138
  disable {{1-blur}}
 }
 Multiply {
  channels rgb
  value 0.1
  name Multiply1
  xpos 0
  ypos 180
  disable {{1-drk}}
 }
 Multiply {
  channels rgb
  value 10
  name Multiply2
  xpos 0
  ypos 206
  disable {{1-brt}}
 }
 Mirror2 {
  name Mirror2_1
  xpos 0
  ypos 264
 }
 Output {
  name Output1
  xpos 0
  ypos 300
 }
end_group
'''


clipboard = QtWidgets.QApplication.clipboard()
clipboard.setText(script)
nuke.nodePaste('%clipboard%')
        