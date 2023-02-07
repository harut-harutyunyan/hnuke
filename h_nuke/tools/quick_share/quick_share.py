import os
import datetime
from PySide2 import QtCore, QtWidgets
import nuke
import nukescripts

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
        return datetime.datetime.now().strftime('%y%m%d-%H-%M-%S')

    @classmethod
    def construct_filename(cls):
        txt = nuke.getInput("QuickShare Name", "")
        if txt:
            txt = txt.replace(" ", "_")
            txt = "_"+"".join(l for l in txt if l.isalnum() or l == "_")
        else:
            txt = ""
        return "{0}{1}-{2}.nk".format(cls.get_host(), txt, cls.get_date())

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
