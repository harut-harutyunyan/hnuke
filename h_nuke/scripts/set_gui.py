import nuke
import nukescripts


class SetGuiValue(nukescripts.PythonPanel):
    def __init__(self):
        super(SetGuiValue, self).__init__('UI/Render Values')
        self.setMinimumSize(300, 50)
        self.work_num = nuke.Double_Knob('working')
        self.render_num = nuke.Double_Knob('rendering')
        self.render_num.clearFlag(nuke.STARTLINE)
        self.render_num.setValue(1)
        self.addKnob(self.work_num)
        self.addKnob(self.render_num)

    def knobChanged(self, knob):
        if knob.name() == "split_nodes":
            value = knob.value() == 0
            self.work_num.setVisible(value)
            self.render_num.setVisible(value)

def gui_val():
    k = nuke.thisKnob()
    panel = SetGuiValue()
    val = k.value()
    if val == 1:
        panel.work_num.setValue(1)
        panel.render_num.setValue(1)
    if val > 1:
        panel.work_num.setValue(val)
        panel.render_num.setValue(val*2)
    if k.name() == "disable":
        panel.work_num.setValue(1)
        panel.render_num.setValue(0)
    if panel.showModalDialog():
        work_num = panel.work_num.getValue()
        render_num = panel.render_num.getValue()
        expression = "[python {} if nuke.executing() else {}]".format(render_num, work_num)
        k.setExpression(expression)
