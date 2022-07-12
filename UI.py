from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QHBoxLayout, QVBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QStackedWidget, QLabel, QSpacerItem, QLineEdit, QTableWidget,
    QSizePolicy
)
from mainwindow_ui import Ui_MainWindow

import sys
import pyautogui

# ********************* Main Window Variables *********************

ScreenWidth, ScreenHeight = pyautogui.size()
MainWindowWidth, MainWindowHeight = 800, 600

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def ShowWindows():
    app = QApplication(sys.argv)
    mainWin = MainWindow()

    mainWin.show()

    sys.exit(app.exec_())