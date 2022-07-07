from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QHBoxLayout, QVBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QStackedWidget, QLabel, QSpacerItem, QLineEdit, QTableWidget,
    QSizePolicy
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

        # Main Menu
        self.MainMenu = QListWidget(self)
        self.MainMenu.setFixedWidth(MainWindowWidth/5)
        item1, item2, item3 = QListWidgetItem('Members'), QListWidgetItem('Books'), QListWidgetItem('Borrows')
        self.MainMenu.addItem(item1)
        self.MainMenu.addItem(item2)
        self.MainMenu.addItem(item3)
        self.MainMenu.currentRowChanged.connect(self.selectedMainMenuItem)
        self.MainMenu.setCurrentItem(item1)

        # Stacks
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
        MembersLayout.setAlignment(QtCore.Qt.AlignTop)

        # Title
        MembersTitle = QLabel('Members')
        MembersTitle.setAlignment(QtCore.Qt.AlignCenter)
        MembersTitle.setFixedHeight(150)

        # add, delete, edit and information Buttons
        MembersAddButton = QPushButton('Add')
        MembersDeleteButton = QPushButton('Delete')
        MembersEditButton = QPushButton('Edit')
        MembersSpacer = QSpacerItem(100, 10, QSizePolicy.Expanding)
        MmebersInfoButton = QPushButton('Full Information')

        # Layout for Widget of Buttons
        MembersButtonsLayout = QHBoxLayout()
        MembersButtonsLayout.addWidget(MembersAddButton)
        MembersButtonsLayout.addWidget(MembersDeleteButton)
        MembersButtonsLayout.addWidget(MembersEditButton)
        MembersButtonsLayout.addSpacerItem(MembersSpacer)
        MembersButtonsLayout.addWidget(MmebersInfoButton)
        MembersButtonsWidget = QtWidgets.QWidget(self)
        MembersButtonsWidget.setLayout(MembersButtonsLayout)

        # Search Box
        MembersSearchBox = QLineEdit()
        MembersSearchBox.setAlignment(QtCore.Qt.AlignCenter)

        # Members Table
        MembersTable = QTableWidget()

        # adding Widgets
        MembersLayout.addWidget(MembersTitle)
        MembersLayout.addWidget(MembersButtonsWidget)
        MembersLayout.addWidget(MembersSearchBox)
        MembersLayout.addWidget(MembersTable)

        self.MembersStack.setLayout(MembersLayout)
    
    def addBooksStack(self):
        self.BooksStack = QtWidgets.QWidget(self)
        BooksLayout = QVBoxLayout()

        # Title
        BooksTitle = QLabel('Books')
        BooksTitle.setAlignment(QtCore.Qt.AlignCenter)
        BooksTitle.setFixedHeight(150)

        # add, delete, edit and information Buttons
        BooksAddButton = QPushButton('Add')
        BooksDeleteButton = QPushButton('Delete')
        BooksEditButton = QPushButton('Edit')
        BooksSpacer = QSpacerItem(100, 10, QSizePolicy.Expanding)
        BooksInfoButton = QPushButton('Full Information')

        # Layout for Widget of Buttons
        BooksButtonsLayout = QHBoxLayout()
        BooksButtonsLayout.addWidget(BooksAddButton)
        BooksButtonsLayout.addWidget(BooksDeleteButton)
        BooksButtonsLayout.addWidget(BooksEditButton)
        BooksButtonsLayout.addSpacerItem(BooksSpacer)
        BooksButtonsLayout.addWidget(BooksInfoButton)
        BooksButtonsWidget = QtWidgets.QWidget(self)
        BooksButtonsWidget.setLayout(BooksButtonsLayout)

        # Search Box
        BooksSearchBox = QLineEdit()
        BooksSearchBox.setAlignment(QtCore.Qt.AlignCenter)

        # Books Table
        BooksTable = QTableWidget()

        # adding Widgets
        BooksLayout.addWidget(BooksTitle)
        BooksLayout.addWidget(BooksButtonsWidget)
        BooksLayout.addWidget(BooksSearchBox)
        BooksLayout.addWidget(BooksTable)

        self.BooksStack.setLayout(BooksLayout)

    def addBorrowsStack(self):
        self.BorrowsStack = QtWidgets.QWidget(self)
        BorrowsLayout = QVBoxLayout()

        BorrowsTitle = QLabel('Borrows')
        BorrowsTitle.setAlignment(QtCore.Qt.AlignCenter)

        BorrowsLayout.addWidget(BorrowsTitle)

        self.BorrowsStack.setLayout(BorrowsLayout)

    # ********************* Signals *********************

    def selectedMainMenuItem(self, i):
        self.MainStack.setCurrentIndex(i)

def ShowWindows():
    app = QApplication(sys.argv)
    mainWin = MainWindow()

    mainWin.show()

    sys.exit(app.exec_())