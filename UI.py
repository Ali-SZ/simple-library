from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QHBoxLayout, QVBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QStackedWidget
)

import sys
import pyautogui

# ********************* Main Window Variables *********************

ScreenWidth, ScreenHeight = pyautogui.size()
MainWindowWidth, MainWindowHeight = 800, 600

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.MainWindowInit()

    # ********************* Main Window Objects *********************

    def MainWindowInit(self):
        self.setGeometry(ScreenWidth/2 - MainWindowWidth/2, ScreenHeight/2 - MainWindowHeight/2, MainWindowWidth, MainWindowHeight)
        self.setMinimumSize(MainWindowWidth, MainWindowHeight)

        self.MainMenu = QListWidget(self)
        self.MainMenu.setFixedWidth(MainWindowWidth/5)
        item1, item2, item3 = QListWidgetItem('Members'), QListWidgetItem('Books'), QListWidgetItem('Borrows')
        self.MainMenu.addItem(item1)
        self.MainMenu.addItem(item2)
        self.MainMenu.addItem(item3)
        self.MainMenu.currentRowChanged.connect(self.selectedMainMenuItem)

        self.addMembersStack()
        self.addBooksStack()
        self.addBorrowsStack()

        self.MainStack = QStackedWidget(self)
        self.MainStack.addWidget(self.MembersStack)
        self.MainStack.addWidget(self.BooksStack)
        self.MainStack.addWidget(self.BorrowsStack)

        MainCentralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(MainCentralWidget)

        self.MainLayout = QHBoxLayout()
        self.MainLayout.addWidget(self.MainMenu)
        self.MainLayout.addWidget(self.MainStack, 2)
        MainCentralWidget.setLayout(self.MainLayout)

    # ********************* Stacks *********************

    def addMembersStack(self):
        self.MembersStack = QtWidgets.QWidget(self)
        MembersLayout = QVBoxLayout()
        MembersLayout.addWidget(QPushButton('Members'))

        self.MembersStack.setLayout(MembersLayout)
    
    def addBooksStack(self):
        self.BooksStack = QtWidgets.QWidget(self)
        BooksLayout = QVBoxLayout()
        BooksLayout.addWidget(QPushButton('Books'))

        self.BooksStack.setLayout(BooksLayout)

    def addBorrowsStack(self):
        self.BorrowsStack = QtWidgets.QWidget(self)
        BorrowsLayout = QVBoxLayout()
        BorrowsLayout.addWidget(QPushButton('Borrows'))

        self.BorrowsStack.setLayout(BorrowsLayout)

    # ********************* Signals *********************

    def selectedMainMenuItem(self, i):
        self.MainStack.setCurrentIndex(i)

def ShowWindows():
    app = QApplication(sys.argv)
    mainWin = MainWindow()

    mainWin.show()

    sys.exit(app.exec_())