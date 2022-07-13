from tkinter import Menubutton
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QHBoxLayout, QVBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QStackedWidget, QLabel, QSpacerItem, QLineEdit, QTableWidget,
    QSizePolicy
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, QPropertyAnimation

from mainwindow_ui import Ui_MainWindow
from Resources_init import *

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
        
        self.clickedButtons_init()
        self.icons_init()
        
    
    # ********************* Initializers *********************
    def clickedButtons_init(self):
        # - for Menu Buttons
        self.ui.ToMemebersPageButton.clicked.connect(self.gotoMembersPage)
        self.ui.ToBooksPageButton.clicked.connect(self.gotoBooksPage)
        self.ui.ToBorrowPageButton.clicked.connect(self.gotoBorrowsPage)
        
    def icons_init(self):
        # - for Menu Buttons
        self.ui.MenuButton.setIcon(QIcon(MENU_ICON_LOCATION))
        self.ui.ToMemebersPageButton.setIcon(QIcon(MEMBERS_ICON_LOCATION))
        self.ui.ToBooksPageButton.setIcon(QIcon(BOOKS_ICON_LOCATION))
        self.ui.ToBorrowPageButton.setIcon(QIcon(BORROWS_ICON_LOCATION))
        self.ui.SettingButton.setIcon(QIcon(SETTING_ICON_LOCATION))
        
        # - for Pages
        self.ui.MembersImage.setPixmap(QPixmap(MEMBERS_ICON_LOCATION))
        self.ui.BooksImage.setPixmap(QPixmap(BOOKS_ICON_LOCATION))
    
    
    # ********************* Signals *********************
    # - for Menu Buttons
    def gotoMembersPage(self):
        self.ui.Pages.setCurrentIndex(0)
    def gotoBooksPage(self):
        self.ui.Pages.setCurrentIndex(1)
    def gotoBorrowsPage(self):
        self.ui.Pages.setCurrentIndex(2)
        

def ShowWindows():
    app = QApplication(sys.argv)
    mainWin = MainWindow()

    mainWin.show()

    sys.exit(app.exec_())