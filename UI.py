from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout, QFormLayout, QSpinBox,
    QListWidget, QListWidgetItem, QPushButton, QStackedWidget, QLabel, QSpacerItem, QLineEdit, QTableWidget,
    QSizePolicy
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, QPropertyAnimation
from PyQt5.QtSql import *

from mainwindow_ui import Ui_MainWindow
from database_connection import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.clickedButtons_init()
        self.icons_init()
        self.database_init()
        
    
    # ********************* Initializers *********************
    def database_init(self):
        createDatabase()
        
        self.database = QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName(DATABASE_LOCATION)
        
        self.refreshMembersTable()
        self.refreshBooksTable()
    
    def clickedButtons_init(self):
        # - for Menu Buttons
        self.ui.ToMemebersPageButton.clicked.connect(self.gotoMembersPage)
        self.ui.ToBooksPageButton.clicked.connect(self.gotoBooksPage)
        self.ui.ToBorrowPageButton.clicked.connect(self.gotoBorrowsPage)
        
        # - for Pages
        self.ui.AddMemberButton.clicked.connect(self.addNewMemberButtonClicked)
        self.ui.DeleteMemberButton.clicked.connect(self.deleteMemberButtonClicked)
        self.ui.AddBookButton.clicked.connect(self.addNewBookButtonClicked)
        self.ui.DeleteBookButton.clicked.connect(self.deleteBookButtonClicked)
        
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
        
    # - for Pages
    def addNewMemberButtonClicked(self):
        self.addNewMemberWindow = addNewRowWindow('member', self)
        self.addNewMemberWindow.show()
        self.refreshMembersTable()
        
    def deleteMemberButtonClicked(self):
        memberid = self.ui.MembersTableView.selectedIndexes()[0].data()
        deleteMember(memberid)
        self.refreshMembersTable()
    
    def addNewBookButtonClicked(self, bookID):
        self.addNewBookWindow = addNewRowWindow('book', self)
        self.addNewBookWindow.show()
        self.refreshBooksTable()
        
    def deleteBookButtonClicked(self):
        bookid = self.ui.BooksTableView.selectedIndexes()[0].data()
        deleteBook(bookid)
        self.refreshBooksTable()
    
    
    # ********************* Functions *********************
    # - for Database
    def refreshMembersTable(self):
        self.database.open()
        self.ui.MembersTableView.reset()
        self.membersTableModel = QSqlTableModel(self, self.database)
        self.membersTableModel.setTable('members')
        self.membersTableModel.select()
        self.ui.MembersTableView.setModel(self.membersTableModel)
        self.database.close()
        
    def refreshBooksTable(self):
        self.database.open()
        self.ui.BooksTableView.reset()
        self.booksTableModel = QSqlTableModel(self, self.database)
        self.booksTableModel.setTable('books')
        self.booksTableModel.select()
        self.ui.BooksTableView.setModel(self.booksTableModel)
        self.database.close()
        

class addNewRowWindow(QWidget):
    def __init__(self, type, parentWindow):
        super().__init__()
        self.type = type
        self.parentWindow = parentWindow
        
        self.ui_init()
                
    def ui_init(self):
        self.centralLayout = QFormLayout(self)
        
        title = QLabel(self)
        title.setText('Please enter the ' + self.type + "'s information")
        self.centralLayout.addWidget(title)
        
        input_list = []
        if(self.type == 'member'):
            input_list = MEMBERS_HEADERS_LIST
        else:
            input_list = BOOKS_HEADERS_LIST
            input_list.pop()
            
        for input_data in input_list:
            lineEdit = QLineEdit(self)
            lineEdit.setObjectName(input_data + 'LineEdit')
            self.centralLayout.addRow(self.tr('&' + input_data), lineEdit)
            
        if self.type == 'book':
            quantitySpinBox = QSpinBox(self)
            quantitySpinBox.setObjectName('quantitySpinBox')
            self.centralLayout.addRow(self.tr('&Quantity'), quantitySpinBox)
            
        submitButton = QPushButton('Submit Informations', self)
        submitButton.clicked.connect(self.addInfoToDatabase)
        self.centralLayout.addWidget(submitButton)
            
        self.setLayout(self.centralLayout)
            
    def addInfoToDatabase(self):
        if self.type == 'member':
            addNewMember(self.findChild(QLineEdit, 'nameLineEdit').text(),
                         self.findChild(QLineEdit, 'phoneLineEdit').text(),
                         self.findChild(QLineEdit, 'emailLineEdit').text(),
                         self.findChild(QLineEdit, 'addressLineEdit').text())
            self.parentWindow.refreshMembersTable()
        else:
            addNewBook(self.findChild(QLineEdit, 'nameLineEdit').text(),
                       self.findChild(QLineEdit, 'authorLineEdit').text(),
                       self.findChild(QLineEdit, 'publisherLineEdit').text(),
                       self.findChild(QLineEdit, 'yearLineEdit').text(),
                       self.findChild(QSpinBox, 'quantitySpinBox').text())
            self.parentWindow.refreshBooksTable()
            
        self.close()
        

def ShowWindows():
    app = QApplication(sys.argv)
    mainWin = MainWindow()

    mainWin.show()

    sys.exit(app.exec_())