from PySide2 import QtWidgets, QtGui, QtCore


def get_pos():
    v = nuke.toNode('Viewer1')
    bbox = v['colour_sample_bbox']
    n = v.input(0)
    w = n.width()
    h = n.height()
    ratio = float(w)/float(h)
    bboxX = bbox.x()
    bboxY = bbox.y()*ratio
    wd = w / 2
    hd = h / 2
    x = int(round(bboxX * wd + wd))
    y = int(round(bboxY * hd + hd))
    return [x, y]


def sample_avg(node, lyr, pp):
    val = 0
    for c in [".red", ".green", ".blue"]:
        val += nuke.sample(node, lyr+c, pp[0], pp[1])
    return val/3

def get_editable_layer():
    mixer = nuke.toNode("Light_Mixer")

    lgt_layers = list(set([c.split(".")[0] for c in mixer.channels() if c.startswith("lgt_")]))

    dd = {}
    for lgt in lgt_layers:
        sample = sample_avg(nuke.toNode("Read2"), lgt, get_pos())
        dd[lgt] = sample

    return max(dd, key=dd.get)

def edit_value(lyr, inc=.1):
    mixer = nuke.toNode("Light_Mixer")
    knob = mixer[lyr+"_exp"]
    knob.setValue(knob.getValue()+inc)


def findviewer():
    stack = QtWidgets.QApplication.topLevelWidgets()
    viewers = []
    while stack:
        widget = stack.pop()
        if widget.windowTitle().startswith('Viewer'):
            # TODO: More robust detection of viewer widget (verify some of the child widgets or something..?)
            viewers.append(widget)
        stack.extend(c for c in widget.children() if c.isWidgetType())

    return viewers

class KeyIntercepter(QtCore.QObject):
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Type.KeyPress:
            if event.key() == QtCore.Qt.Key_U:
                lyr=get_editable_layer()
                edit_value(lyr)
                # Event was handled..
                return True
            if event.key() == QtCore.Qt.Key_Y:
                lyr=get_editable_layer()
                edit_value(lyr, -.1)
                # Event was handled..
                return True
        return QtCore.QObject.eventFilter(obj, obj, event)


viewers = findviewer()

# Remove old event filter
# FIXME: Debugging thing, for iteration in script editor
try: dag.removeEventFilter(thing)
except: pass

# Install event filter
thing=KeyIntercepter()
for v in viewers:
    v.installEventFilter(thing)
