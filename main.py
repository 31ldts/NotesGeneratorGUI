import sys
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller.

    :param relative_path: the relative path to the file.
    :return: the full path to the file.
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MainWindow(QMainWindow):
    """
    Class representing the main window of the app, which will allow the user to create a new tree.
    Also, it has a menu in which the user can operate with the tree and its nodes and also look for
    help.
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #loadUi(resource_path("ui" + os.sep + "mainscreen.ui"), self)
        #self.icon = QIcon("icon.ico")
        #self.setWindowIcon(self.icon)
        self.titleLable = QLabel("Notes Generator", self)
        self.mainGrid = QGridLayout()
        self.setLayout(self.mainGrid)
        self.mainGrid.addWidget(self.titleLable, 0, 0, 1, 1)
        self.setWindowTitle("title")
        self.show()

        # MENU ACTIONS
        #self.actionImport.setShortcut(QKeySequence("Ctrl+I"))
        #self.actionImport.triggered.connect(self.importTree)


class MyWidget(QStackedWidget):
    def __init__(self, mainWindow=None):
        super(MyWidget, self).__init__()
        self.mainWindow = mainWindow

    def setMainWindow(self, mW):
        self.mainWindow = mW


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyleSheet("QLabel { color: #FFFF; font-family: Arial; font-size: 20px;}"
                      )


    m_window = MainWindow()

    widget = MyWidget(m_window)
    QLocale.setDefault(QLocale(QLocale.English))
    widget.setLocale(QLocale(QLocale.English))
    widget.setWindowTitle("Notes generator")
    # icon = QIcon(resource_path("icon.ico"))
    # widget.setWindowIcon(icon)
    widget.addWidget(m_window)

    min_width = 900
    min_height = 750

    widget.setMinimumWidth(min_width)
    widget.setMinimumHeight(min_height)
    widget.update()
    widget.show()
    app.exec_()
