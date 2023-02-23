import os
from datetime import datetime
from PySide2 import QtCore, QtGui, QtWidgets
import nuke
import nukescripts

ICONPATH = os.path.dirname(__file__)

def format_input(txt):
    if txt:
        txt = txt.replace(" ", "_")
        txt = "".join(l for l in txt if l.isalnum() or l == "_")
    else:
        txt = ""
    return txt

def str_to_datetime(input_string):
    year = int(input_string[:2]) + 2000
    month = int(input_string[2:4])
    day = int(input_string[4:6])
    hour = int(input_string[7:9])
    minute = int(input_string[10:12])

    return datetime(year, month, day, hour, minute)

def parse_qs_name(input_string):
    split = input_string.split("_")
    if len(split)>2:
        prj, usr, leftovers = input_string.split("_", 2)
    else:
        prj = split[0]
        usr, leftovers = split[1].split("-", 1)
        leftovers = "_-"+leftovers


    name, date = leftovers.split("-", 1)
    name = name.replace("_", " ")
    if name == " ":
        name = ""
    date = str_to_datetime(date).strftime("%b %d, %Y %H:%M:%S")

    return[prj, name, usr, date]

def change_qs_name(qs_file, new_name):
    start, end = qs_file.split("-", 1)
    split = start.split("_", 2)
    if len(split) > 2:
        return "{}_{}_{}-{}".format(split[0], split[1], new_name, end)
    else:
        return "{}_{}-{}".format(start, new_name, end)

def autoBackdrop():
    selNodes = nuke.selectedNodes()
    if not selNodes:
        return nuke.nodes.BackdropNode()

    for node in selNodes:
        x = node['xpos'].value()
        y = node['ypos'].value()
        node['xpos'].setValue(x +1000000)
        node['ypos'].setValue(y +1000000)

    bdX = min([node.xpos() for node in selNodes])
    bdY = min([node.ypos() for node in selNodes])
    bdW = max([node.xpos() + node.screenWidth() for node in selNodes]) - bdX
    bdH = max([node.ypos() + node.screenHeight() for node in selNodes]) - bdY

    margin = 300
    left, top, right, bottom = (-margin, -margin, margin, margin)
    bdX += left
    bdY += top
    bdW += (right - left)
    bdH += (bottom - top)

    n = nuke.nodes.BackdropNode(xpos = bdX,
                                bdwidth = bdW,
                                ypos = bdY,
                                bdheight = bdH,
                                tile_color = 1244014335,
                                label = "<center>all the nodes inside will be saved in the preset",
                                note_font = "Arial",
                                note_font_size = 66,
                                z_order = -10 )

    n.knob('name').setValue("__MODIFY_QS__")

    nuke.zoomToFitSelected()

    n['selected'].setValue(False)
    for node in selNodes:
        node['selected'].setValue(True)

    return n

def populate_row(table, path, content=[]):
    row_num = table.rowCount()
    table.insertRow(row_num)
    if content:
        first = content.pop(0)
        item = QtWidgets.QTableWidgetItem(first)
        item.setData(1000, path)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        table.setItem(row_num, 0, item)
        for i, text in enumerate(content):
            item = QtWidgets.QTableWidgetItem(text)
            if i == 0:
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
            else:
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            table.setItem(row_num, i+1, item)

def set_icon(widget, name=None, size=None):
    """
    Sets icon for a widget. Looks in ICONPATH for icon. Olny .png supported
    @args:
        widget: QWidget
        name: string icon name
        size: tuple height width
    @return
    """
    icon = os.path.join(ICONPATH, name)

    widget.setIcon(QtGui.QIcon(icon))
    if size:
        widget.setIconSize(QtCore.QSize(size[0], size[1]))

def unselect_all():
    for node in nuke.selectedNodes():
        node.setSelected(False)

class QuickShare(object):

    URL_PREFIX = "nuke_quick_share"

    _root = None
    _prj = None
    _host = None

    @classmethod
    def get_root(cls):
        if not cls._root:
            nuke.message("QuckShare is not configured properly.\nThe ROOT should point to a path on disk.")
            return None
        return cls._root

    @classmethod
    def set_root(cls, value):
        if not os.path.isdir(value):
            nuke.message("The ROOT should point to a path on disk.")
            return
        cls._root = value

    @classmethod
    def get_prj(cls):
        if not cls._prj:
            return "temp"
        return cls._prj

    @classmethod
    def set_prj(cls, value):
        if isinstance(value, str):
            if cls._root:
                if os.path.isdir(cls._root):
                    cls._prj = value
                    if not value in os.listdir(cls._root):
                        os.mkdir(os.path.join(cls._root, value))

    @classmethod
    def get_host(cls):
        if not cls._host:
            return "unknown"
        return cls._host

    @classmethod
    def set_host(cls, value):
        if isinstance(value, str):
            cls._host = value

    @staticmethod
    def get_date():
        return datetime.now().strftime('%y%m%d-%H-%M-%S')

    @classmethod
    def construct_filename(cls):
        txt = nuke.getInput("QuickShare Name", "")
        txt = format_input(txt)
        return "{0}_{1}-{2}.nk".format(cls.get_host(), txt, cls.get_date())

    @classmethod
    def quick_share(cls):
        root = cls.get_root()
        if not root:
            return

        save_path = os.path.join(root, cls.get_prj())

        if not nuke.selectedNodes():
            nuke.message('No nodes selected.')
            return

        filename = cls.construct_filename()

        filename.replace(" ", "_")
        url = os.path.join(root, cls.get_prj(), "{0}_{1}".format(cls.get_prj(), filename))

        nuke.nodeCopy(url)

        cls.copy_to_clipboard(url)

    @classmethod
    def copy_to_clipboard(cls, text):
        """
        Copies the given text into clipboard

        Args:
            text(str): text to copy

        """
        cb = QtWidgets.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(text, mode=cb.Clipboard)

    @classmethod
    def drop_quick_share(cls, mimeType, text):
        """
        A Nuke dropData callback function to parse a short copy URL.

        Args:
            mimeType(str): dropped data type
            text(str): dropped url

        Returns(bool): True if it succeed, False otherwise

        """
        if text.startswith("{0}://".format(cls.URL_PREFIX)):
            root = cls.get_root()
            if not root:
                return True
            file_path = '{0}/{1}_{2}'.format(os.path.join(root, cls.get_prj()), cls.get_prj(), os.path.basename(text))

            if not os.path.isfile(file_path):
                nuke.message('No file found.\n{0}'.format(file_path))
                return

            QtCore.QTimer.singleShot(0, lambda: nuke.nodePaste(file_path))

            return True

        # return False to let nuke handle other dropped types
        return False


class QuickShareManager(QtWidgets.QDialog):
    """QuickShareManager dialog"""

    dlg_instance = None

    @classmethod
    def display(cls):
        """
        Creates instance of the dialog if not existing and displays it.
        Moves dialog under mouse cursor
        """
        if not cls.dlg_instance:
            cls.dlg_instance = QuickShareManager()

        if cls.dlg_instance.isHidden():
            cls.dlg_instance.show()
        else:
            cls.dlg_instance.raise_()
            cls.dlg_instance.activateWindow()

    @staticmethod
    def spacer(type='horizontal'):
        """Makes horizontal or vertical QtWidgets.QSpacerItem."""
        if type == 'vertical':
            return QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        elif type == 'horizontal':
            return QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        else:
            return None

    def __init__(self):
        super(QuickShareManager, self).__init__()

        # gui creation
        self.configure_window()

        self.create_widgets()
        self.create_layout()
        self.create_connections()

        self.populate_prj()

    def configure_window(self):
        self.setWindowTitle("Quick Share Manager")
        self.setFixedSize(700, 500)

    def create_widgets(self):
        self.prj_combo = QtWidgets.QComboBox()

        self.refresh_btn = QtWidgets.QPushButton()
        set_icon(self.refresh_btn, "refresh.svg", (16, 16))
        self.refresh_btn.setToolTip("Refresh QuickShare list")

        self.copy_btn = QtWidgets.QPushButton()
        set_icon(self.copy_btn, "copy.svg", (16, 16))
        self.copy_btn.setToolTip("Copy QuickShare preset")

        self.import_btn = QtWidgets.QPushButton()
        set_icon(self.import_btn, "import.svg", (16, 16))
        self.import_btn.setToolTip("Load QuickShare preset")

        self.edit_btn = QtWidgets.QPushButton()
        set_icon(self.edit_btn, "edit.svg", (16, 16))
        self.edit_btn.setCheckable(True)
        self.edit_btn.setToolTip("Edit QuickShare preset")

        self.delete_btn = QtWidgets.QPushButton()
        set_icon(self.delete_btn, "delete.svg", (16, 16))
        self.delete_btn.setToolTip("Delete QuickShare preset")

        self.close_btn = QtWidgets.QPushButton("Close")

        self.table = QtWidgets.QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["project", "name", "user", "date"])
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setColumnWidth(0, 70)
        self.table.setColumnWidth(1, 340)
        self.table.setColumnWidth(2, 120)
        self.table.setColumnWidth(3, 130)

    def create_layout(self):
        self.manager_layout = QtWidgets.QVBoxLayout(self)
        self.upper_row_lyt = QtWidgets.QHBoxLayout()

        self.upper_row_lyt.addWidget(QtWidgets.QLabel("Project: "))
        self.upper_row_lyt.addWidget(self.prj_combo)
        self.upper_row_lyt.addWidget(self.refresh_btn)
        self.upper_row_lyt.addItem(self.spacer())
        self.upper_row_lyt.addWidget(self.copy_btn)
        self.upper_row_lyt.addWidget(self.import_btn)
        self.upper_row_lyt.addWidget(self.edit_btn)
        self.upper_row_lyt.addWidget(self.delete_btn)


        self.manager_layout.addLayout(self.upper_row_lyt)
        self.manager_layout.addWidget(self.table)
        self.manager_layout.addWidget(self.close_btn)

    def create_connections(self):
        self.prj_combo.currentIndexChanged.connect(self.populate)

        self.copy_btn.clicked.connect(self.to_clipboard)
        self.import_btn.clicked.connect(self.import_qs)
        self.edit_btn.clicked.connect(self.edit_qs)
        self.delete_btn.clicked.connect(self.delete_qs)

        self.table.itemDoubleClicked.connect(self.to_clipboard)
        self.table.itemChanged.connect(self.rename_qs)

        self.refresh_btn.clicked.connect(self.populate)

        self.close_btn.clicked.connect(self.close)

    def populate_prj(self):
        self.prj_combo.clear()
        self.prj_combo.addItems(os.listdir(QuickShare.get_root()))

        index = self.prj_combo.findText(QuickShare.get_prj(), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.prj_combo.setCurrentIndex(index)

    def populate(self):
        self.table.setRowCount(0)
        prj_path = os.path.join(QuickShare.get_root(), self.prj_combo.currentText())
        items = [i for i in os.listdir(prj_path) if i.endswith(".nk")]
        for item in items:
            populate_row(self.table, os.path.join(prj_path, item), parse_qs_name(item))

    def to_clipboard(self):
        row = self.table.currentRow()
        if row >= 0:
            file_path = self.table.item(row, 0).data(1000)
            QuickShare.copy_to_clipboard(file_path)

    def import_qs(self):
        row = self.table.currentRow()
        if row >= 0:
            file_path = self.table.item(row, 0).data(1000)
            unselect_all()
            nuke.nodePaste(file_path)

    def edit_qs(self):
        row = self.table.currentRow()
        if row >= 0:
            state = self.edit_btn.isChecked()
            self.edit_mode(state)
            if state:
                self.import_qs()
                autoBackdrop()
            if not state:
                backdrop = nuke.toNode("__MODIFY_QS__")
                backdrop.selectNodes(True)

                file_path = self.table.item(row, 0).data(1000)
                nuke.nodeCopy(file_path)

                nuke.delete(backdrop)
                for node in nuke.selectedNodes():
                    nuke.delete(node)
        else:
            self.edit_btn.setChecked(False)

    def delete_qs(self):
        row = self.table.currentRow()
        if row >= 0:
            file_path = self.table.item(row, 0).data(1000)
            os.remove(file_path)
            self.populate()

    def rename_qs(self, item):
        row = self.table.currentRow()
        if row >= 0:
            file_path = self.table.item(row, 0).data(1000)
            file_dir, file_name = os.path.split(file_path)
            new_name = item.text()
            new_name = os.path.join(file_dir, change_qs_name(file_name, format_input(new_name)))
            os.rename(file_path, new_name)
            self.populate()

    def edit_mode(self, state):
        if state:
            self.edit_btn.setStyleSheet('background-color: orange')
            self.copy_btn.setEnabled(False)
            self.import_btn.setEnabled(False)
            self.delete_btn.setEnabled(False)
            self.table.setEnabled(False)
            self.refresh_btn.setEnabled(False)
            self.prj_combo.setEnabled(False)
        if not state:
            self.edit_btn.setStyleSheet('background-color: ')
            self.copy_btn.setEnabled(True)
            self.import_btn.setEnabled(True)
            self.delete_btn.setEnabled(True)
            self.table.setEnabled(True)
            self.refresh_btn.setEnabled(True)
            self.prj_combo.setEnabled(True)


    def closeEvent(self, event):
        if self.edit_btn.isChecked():
            self.edit_btn.setChecked(False)
            self.edit_qs()
        super(QuickShareManager, self).closeEvent(event)
