#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: DiffClamped
#
#----------------------------------------------------------------------------------------------------------




if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
else:
    from PySide2 import QtWidgets

script = r'''set cut_paste_input [stack 0]
push $cut_paste_input
push 0
Group {
 inputs 2
 name DifferenceClamped
 selected true
 xpos 700
 ypos -206
 addUserKnob {20 User}
 addUserKnob {41 thresh l threshhold T Expression1.thresh}
}
 Input {
  inputs 0
  name A
  xpos 503
  ypos -295
  number 1
 }
 Input {
  inputs 0
  name B
  selected true
  xpos 659
  ypos -353
 }
 Difference {
  inputs 2
  name Difference1
  xpos 659
  ypos -301
 }
 Expression {
  expr3 a>thresh/10000?1:0
  name Expression1
  xpos 659
  ypos -263
  addUserKnob {20 User}
  addUserKnob {7 thresh}
  thresh 0.1
 }
 Grade {
  white {1 0.3333333433 0.3333333433 1}
  multiply 1.25
  maskChannelInput rgba.alpha
  name Grade3
  xpos 659
  ypos -208
 }
 Output {
  name Output1
  xpos 663
  ypos -144
 }
end_group
'''


clipboard = QtWidgets.QApplication.clipboard()
clipboard.setText(script)
nuke.nodePaste('%clipboard%')
