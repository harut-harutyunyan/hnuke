from PySide2 import QtWidgets, QtGui, QtCore
import nuke


def mirror_view():
    av = nuke.activeViewer()

    av_node = av.node()
    ainpt = av.activeInput()
    node = av_node.input(ainpt)

    if node.name() == "__temp_mirror__":
        nuke.delete(node)
    else:
        mirror = nuke.nodes.Mirror2(name="__temp_mirror__", flop=1)
        mirror.setInput(0, node)
        av_node.setInput(ainpt, mirror)


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
                mirror_view()
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
