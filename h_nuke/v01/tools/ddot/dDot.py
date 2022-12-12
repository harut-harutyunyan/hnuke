from PySide2 import QtCore, QtGui, QtWidgets
import nuke
import nukescripts


ICON_SIZE = 130
GRID_SIZE = 138

LABEL_STYLESHEET = """
QLabel {
    color: white;
}
QLabel:hover{
    color: #dddddd;
}
"""


class DDot(object):

    FONT_SIZE = 42
    DISTANCE_FROM_NODE = 150
    UPDATE_UI_ON = True
    UPDATE_UI = "node = nuke.toNode(nuke.thisNode().knob('label').getValue())\nif node:\n    nuke.thisNode().setInput(0, node)"

    @classmethod
    def unselect_all(cls):
        for node in nuke.selectedNodes():
            node.setSelected(False)

    @classmethod
    def get_parent_nodes(cls):
        return [n for n in nuke.allNodes("Dot") if n.knob("parent")]

    @classmethod
    def parent(cls):
        selected = nuke.Root().selectedNode()

        if selected == None:
            nuke.message('Error:Nothing is selected.')

        elif len(nuke.Root().selectedNodes()) > 1:
            nuke.message('Error:Multiple nodes selected')

        if len([n for n in selected.dependent() if n.Class() == 'Dot' and n.knob('parent')])!=0:
            nuke.message('{} is already a parent'.format(selected.name()))
            return

        if selected.knob('parent'):
            nuke.message('This is already a parent')
            return

        parentName = nuke.getInput('ParentName for: {}'.format(selected.name()),'')
        parentKnob = nuke.Text_Knob('parent', 'parent')

        if parentName == None:
            return False

        if parentName == '':
            nuke.message('No parent name given.')
            return False

        elif selected.Class() == 'Dot':
            if selected.knob('child'):
                nuke.message("Error:It's a child.")
            else:
                nuke.selectedNode().knob('label').setValue('[value name]')
                nuke.selectedNode().knob('name').setValue(parentName)
                nuke.selectedNode().knob('tile_color').setValue(0)
                nuke.selectedNode().knob('note_font_size').setValue(cls.FONT_SIZE)
                if nuke.selectedNode().knob('parent'):
                    pass
                else:
                    nuke.selectedNode().addKnob(parentKnob)

        else:
            newDot = nuke.createNode('Dot', inpanel=False)
            newDot.setXpos(selected.xpos()+int(selected.screenWidth()/2-5))
            newDot.setYpos(selected.ypos()+cls.DISTANCE_FROM_NODE)
            newDot.knob('label').setValue('[value name]')
            newDot.knob('name').setValue(parentName)
            newDot.knob('tile_color').setValue(0)
            newDot.knob('note_font_size').setValue(cls.FONT_SIZE)
            newDot.addKnob(parentKnob)

    @classmethod
    def connect(cls, parent):
        dot = nuke.createNode("Dot", inpanel=False)
        dot.connectInput(0, parent)
        dot.knob('label').setValue(parent.name())
        dot.knob('tile_color').setValue(0)
        dot.knob('hide_input').setValue(True)
        dot.knob('note_font').setValue('italic')
        dot.knob('note_font_size').setValue(cls.FONT_SIZE-10)
        if cls.UPDATE_UI_ON:
            dot.knob('updateUI').setValue(cls.UPDATE_UI)
        child_knob = nuke.Text_Knob('child', 'child')
        dot.addKnob(child_knob)
        parent_color = int(parent.knob('note_font_color').getValue())
        dot.knob('note_font_color').setValue(parent_color)

    @classmethod
    def check_input(cls):
        brokenConnections = []
        for d in nuke.allNodes('Dot'):
            if d.input(0) == None:
                d['tile_color'].setValue(4278190335)
                brokenConnections.append(d.knob('name').getValue())
            else:
                if d.knob('child'):
                    childLabel = d.knob('label').getValue()
                    parentName = d.input(0).knob('name').getValue()
                    if childLabel == parentName:
                        d['tile_color'].setValue(0)
                    else:
                        d['tile_color'].setValue(4278190335)
                        brokenConnections.append(d.knob('name').getValue())
                else:
                    d['tile_color'].setValue(0)
        if len(brokenConnections) > 0:
            brokenConnections.sort()
            nuke.message('{} connection(s) broken: \n{}'.format(len(brokenConnections), "\n".join(brokenConnections)))

    @classmethod
    def auto_connect(cls):
        for d in nuke.selectedNodes('Dot'):
            if d.knob('child'):
                childLabel = d.knob('label').getValue()
                parent = nuke.toNode(childLabel)
                try:
                    parentColor = parent.knob('note_font_color').getValue()
                    parentColor = int(parentColor)
                except:
                    parentColor = 4278190335
                if d.input(0) == None:
                    d.connectInput(0, parent)
                    d['tile_color'].setValue(0)
                    d.knob('note_font_size').setValue(cls.FONT_SIZE-10)
                    d.knob('note_font_color').setValue(parentColor)
                else:
                    parentName = d.input(0).knob('name').getValue()
                    if childLabel != parentName:
                        d.connectInput(0, parent)
                        d['tile_color'].setValue(0)
                        d.knob('note_font_size').setValue(cls.FONT_SIZE-10)
                        d.knob('note_font_color').setValue(parentColor)
        cls.check_input()

    @classmethod
    def show_children(cls):
        selectedNode = nuke.selectedNodes()
        if len(selectedNode) < 1:
            return
        selectedNode = selectedNode[0]
        dependentNodes = selectedNode.dependent()
        selectedNode.setSelected(False)
        for depnd in dependentNodes:
            depnd.setSelected(True)

    @classmethod
    def toggle_connection_visibility(cls):
        selectedNode = nuke.selectedNodes()
        if len(selectedNode) < 1:
            return
        selectedNode = selectedNode[0]
        dependentNodes = selectedNode.dependent()
        for depnd in dependentNodes:
            currentState = depnd.knob('hide_input').getValue()
            depnd.knob('hide_input').setValue(not currentState)

    @classmethod
    def name_change(cls):
        selectedNode = nuke.selectedNodes()
        if len(selectedNode) < 1:
            return
        selectedNode = selectedNode[0]
        selectedNodeName = selectedNode.knob('name').getValue()
        parentColor = selectedNode.knob('note_font_color').getValue()
        parentColor = int(parentColor)
        if selectedNode.Class() == 'Dot':
            if selectedNode.knob('parent'):
                dependentNodes = selectedNode.dependent()
                for depnd in dependentNodes:
                    if depnd.knob('child'):
                        depnd.knob('label').setValue(selectedNodeName)
                        depnd.knob('note_font_color').setValue(parentColor)
                cls.check_input()

    @classmethod
    def select_children(cls):
        childName = nuke.getInput('select child nodes labeled:','')
        for n in nuke.allNodes('Dot'):
            if n.knob('child') and n.knob('label'). getValue() == childName:
                n.setSelected(True)


class DDotManager(QtWidgets.QDialog):
    """DDotManager dialog"""

    dlg_instance = None
    nodes_3d = ['Scene', 'Camera2', 'Camera3', 'Axis2', 'Axis3', 'Card2',
                'ReadGeo2', 'TransformGeo', 'Camera', 'Axis', 'Card']

    @classmethod
    def display(cls):
        """
        Creates instance of the dialog if not existing and displays it.
        Moves dialog under mouse cursor
        """
        if not cls.dlg_instance:
            cls.dlg_instance = DDotManager()

        cls.dlg_instance.move(
            QtGui.QCursor().pos() - QtCore.QPoint((cls.dlg_instance.width() / 2),
                                                  (cls.dlg_instance.height() / 2)))  # move dlg under cursor
        if cls.dlg_instance.isHidden():
            cls.dlg_instance.show()
        else:
            cls.dlg_instance.raise_()
            cls.dlg_instance.activateWindow()

    def __init__(self):
        super(DDotManager, self).__init__()
        # parent to main nuke interface
        self.setParent(QtWidgets.QApplication.instance().activeWindow())

        # gui creation
        self.configure_window()

        self.create_widgets()
        self.create_layout()
        self.create_connections()

        # configure existing shortcuts
        self.populate()

    def configure_window(self):
        # window flags
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.Popup)  # popup window

        self.setFixedSize(674, 260)
        self.setWindowOpacity(0.9)

    def create_widgets(self):
        self.shortcuts_list = ShortcutList()
        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):
        self.manager_layout = QtWidgets.QVBoxLayout(self)

        self.manager_layout.addWidget(self.shortcuts_list)
        self.manager_layout.addWidget(self.close_btn)

    def create_connections(self):
        self.close_btn.clicked.connect(self.close)

    def populate(self):
        self.shortcuts_list.clear()
        parents = DDot.get_parent_nodes()
        print(parents)
        for parent in parents:
            parent_item = QtWidgets.QListWidgetItem()
            parent_item.setSizeHint(QtCore.QSize(ICON_SIZE, ICON_SIZE))
            parent_item.setData(QtCore.Qt.UserRole, parent.name())
            klass = parent.input(0).Class()
            custom_item = NodeShape(parent.name(), circle=klass in self.nodes_3d)
            self.shortcuts_list.addItem(parent_item)
            self.shortcuts_list.setItemWidget(parent_item, custom_item)

    def showEvent(self, event):
        """populate shortcuts after showing the dialog window"""
        super(DDotManager, self).showEvent(event)
        self.populate()


class ShortcutList(QtWidgets.QListWidget):


    def __init__(self):
        super(ShortcutList, self).__init__()
        self.configure_widget()

    def configure_widget(self):
        self.setFixedSize(650, 155)
        self.setViewMode(QtWidgets.QListWidget.IconMode)
        self.setResizeMode(QtWidgets.QListWidget.Adjust)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setFlow(QtWidgets.QListView.TopToBottom)
        self.setIconSize(QtCore.QSize(ICON_SIZE, ICON_SIZE))
        self.setGridSize(QtCore.QSize(GRID_SIZE, GRID_SIZE))

    def mouseMoveEvent(self, e):
        mime_data = QtCore.QMimeData()
        item = self.currentItem()
        if item:
            ss = '__sm ' + str(item.data(QtCore.Qt.UserRole))
            mime_data.setData(u'text/plain', QtCore.QByteArray(ss.encode()))
        else:
            mime_data.setData(u'html', None)
        drag = QtGui.QDrag(self)
        drag.setMimeData(mime_data)
        drag.start(QtCore.Qt.MoveAction)


class NodeShape(QtWidgets.QWidget):
    def __init__(self, text, color=[0.5, 0.5, 0.5], circle=False):
        super(NodeShape, self).__init__()
        self.setGeometry(ICON_SIZE, ICON_SIZE, ICON_SIZE, ICON_SIZE)

        self.text = text
        self.is_circle = circle

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setup_label()

        # geometry properties
        self.offset = 5
        self.radius = ICON_SIZE - self.offset
        self.sel_edge = 10

        self.color = self.qcolor(color)
        self.highlight_color = QtGui.QColor('#ce9954')
        # self.highlight_color = QtGui.QColor('#68a591')
        self.selected = False
        self.paint = QtGui.QPainter()

    @staticmethod
    def qcolor(rgb):
        return QtGui.QColor(rgb[0]*255, rgb[1]*255, rgb[2]*255)

    def setup_label(self):
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        font.setStyle(QtGui.QFont.StyleOblique)

        self.label = QtWidgets.QLabel(self.text)
        self.label.setStyleSheet(LABEL_STYLESHEET)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter |
                                QtCore.Qt.AlignVCenter)
        self.layout.addWidget(self.label)

    def paintEvent(self, event):
        self.paint.begin(self)
        self.paint.setRenderHint(QtGui.QPainter.Antialiasing)

        self.draw_shape()

        self.paint.end()

    def shape(self, pen_color, brush_color, center, radius):
        # draw shape outline
        self.paint.setPen(pen_color)
        # fill shape
        self.paint.setBrush(brush_color)

        if self.is_circle:
            self.paint.drawEllipse(center, center, radius, radius)
        else:
            self.paint.drawRect(center+5, center, radius-10, radius)

    def draw_shape(self):
        if self.selected:
            self.shape(pen_color=QtCore.Qt.black,
                       brush_color=self.color,
                       center=self.offset/2,
                       radius=self.radius)  # node shape
            self.shape(pen_color=self.highlight_color,
                       brush_color=self.highlight_color,
                       center=self.offset/2+self.sel_edge/2,
                       radius=self.radius-self.sel_edge)  # node highlight shape
        else:
            self.shape(pen_color=QtCore.Qt.black,
                       brush_color=self.color,
                       center=self.offset/2,
                       radius=self.radius)  # node shape

    def enterEvent(self, event):
        self.selected = True
        self.update()
        return super(NodeShape, self).enterEvent(event)

    def leaveEvent(self, event):
        self.selected = False
        self.update()
        return super(NodeShape, self).enterEvent(event)


def ddot_start():
    sel_list = nuke.selectedNodes()
    if len(sel_list) == 0:
        DDotManager.display()
    elif sel_list[0].knob('child'):
        DDot.auto_connect()
    else:
        for node in sel_list:
            DDot.unselect_all()
            node.setSelected(True)
            DDot.parent()

def drop_shortcut(mimeType, text):
    """
    used with nukescripts.addDropDataCallback()
    triggered on if text is dropped to DAG

    @args
    @return
    """
    if not mimeType == 'text/plain' or not text.startswith('__sm'):
        return False

    link_name = text.replace('__sm ', '')
    if not link_name:
        return False

    [n.setSelected(False) for n in nuke.selectedNodes()]
    link_node = nuke.toNode(link_name)
    DDot.connect(link_node)
    return True

def initialize():
    # add Shortcut Manager to nuke edit menu
    edit_menu = nuke.menu("Nuke").findItem("Edit")
    edit_menu.addSeparator()
    ddot_menu = edit_menu.addMenu("dDot")
    ddot_menu.addCommand("dDot", "dDot.ddot_start()", "shift+D")
    ddot_menu.addSeparator()
    ddot_menu.addCommand("dDotCheckInput", "dDot.DDot.check_input()")
    ddot_menu.addCommand("dDotAutoConnect", "dDot.DDot.auto_connect()")
    ddot_menu.addCommand("dDotShowChildren", "dDot.DDot.show_children()")
    ddot_menu.addCommand("dDotToggleConnectionsVisibility", "dDot.DDot.toggle_connection_visibility()")
    ddot_menu.addCommand("dDotRollDownNameChange", "dDot.DDot.name_change()")
    ddot_menu.addCommand("dDotSelectChildren", "dDot.DDot.select_children()")

    nukescripts.addDropDataCallback(drop_shortcut)

initialize()
