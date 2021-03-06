from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHeaderView, QTabWidget, QMessageBox, QDateEdit, QTableView,
    QHBoxLayout, QVBoxLayout, QFormLayout, QSpinBox, QGridLayout,
    QListWidget, QListWidgetItem, QPushButton, QStackedWidget, QLabel, QSpacerItem, QLineEdit, QTableWidget,
    QSizePolicy
)
from PyQt5.QtGui import QIcon, QPixmap, QStandardItemModel
from PyQt5.QtCore import QSize, QPropertyAnimation, QSortFilterProxyModel, QDate
from PyQt5.QtSql import *

from mainwindow_ui import Ui_MainWindow
from database_connection import *
from stylesheets import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.isMenuOpen = True
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.clickedButtons_init()
        self.icons_init()
        self.database_init()
        self.stylesheet_init()
        self.ui.Pages.setCurrentIndex(0)
        
    
    # ********************* Initializers *********************
    def database_init(self):
        createDatabase()
        
        self.database = QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName(DATABASE_LOCATION)
        
        self.refreshMembersTable()
        self.refreshBooksTable()
        self.refreshBorrowsTable()
    
    def clickedButtons_init(self):
        # - for Menu Buttons
        self.ui.MenuButton.clicked.connect(self.menuButtonClicked)
        self.ui.ToMemebersPageButton.clicked.connect(self.gotoMembersPage)
        self.ui.ToBooksPageButton.clicked.connect(self.gotoBooksPage)
        self.ui.ToBorrowPageButton.clicked.connect(self.gotoBorrowsPage)
        
        # - for Pages
        self.ui.AddMemberButton.clicked.connect(self.addNewMemberButtonClicked)
        self.ui.DeleteMemberButton.clicked.connect(self.deleteMemberButtonClicked)
        self.ui.EditMemberButton.clicked.connect(self.editMemberButtonClicked)
        self.ui.AddBookButton.clicked.connect(self.addNewBookButtonClicked)
        self.ui.DeleteBookButton.clicked.connect(self.deleteBookButtonClicked)
        self.ui.EditBookButton.clicked.connect(self.editBookButtonClicked)
        self.ui.AddBorrowButton.clicked.connect(self.borrowButtonClicked)
        self.ui.ReturnBorrowButton.clicked.connect(self.returnBorrowButtonClicked)
        
    def searchBoxesTextChanged(self):
        self.ui.MembersSearchBox.textChanged.connect(self.searchMembers)
        self.ui.BooksSearchBox.textChanged.connect(self.searchBooks)
        
    def icons_init(self):
        # - for Menu Buttons
        self.ui.MenuButton.setIcon(QIcon(MENU_ICON_LOCATION))
        self.ui.ToMemebersPageButton.setIcon(QIcon(MEMBERS_ICON_LOCATION))
        self.ui.ToBooksPageButton.setIcon(QIcon(BOOKS_ICON_LOCATION))
        self.ui.ToBorrowPageButton.setIcon(QIcon(BORROWS_ICON_LOCATION))
        
        # - for Pages
        self.ui.MembersImage.setPixmap(QPixmap(MEMBERS_ICON_LOCATION))
        self.ui.BooksImage.setPixmap(QPixmap(BOOKS_ICON_LOCATION))
        self.ui.BorrowsImage.setPixmap(QPixmap(BORROWS_ICON_LOCATION))
        
    def stylesheet_init(self):
        self.ui.MenuButtonsFrame.setStyleSheet(MENU_FRAME_STYLE)
        self.ui.Pages.setStyleSheet(PAGES_STYLE)
    
    
    # ********************* Signals *********************
    # - for Menu Animation
    def menuButtonClicked(self):
        self.menuAnimation = QPropertyAnimation(self.ui.MenuButton, b'minimumWidth')
        self.menuAnimation.setDuration(200)
        
        if self.isMenuOpen:
            self.menuAnimation.setStartValue(OPEN_MENU_WIDTH)
            self.menuAnimation.setEndValue(CLOSED_MENU_WIDTH)
            self.ui.MenuButton.setText('')
            self.ui.ToMemebersPageButton.setText('')
            self.ui.ToBooksPageButton.setText('')
            self.ui.ToBorrowPageButton.setText('')
            self.isMenuOpen = False
        else:
            self.menuAnimation.setStartValue(CLOSED_MENU_WIDTH)
            self.menuAnimation.setEndValue(OPEN_MENU_WIDTH)
            self.ui.MenuButton.setText('  Menu')
            self.ui.ToMemebersPageButton.setText('  Members')
            self.ui.ToBooksPageButton.setText('  Books')
            self.ui.ToBorrowPageButton.setText('  Borrows')
            self.isMenuOpen = True
        
        self.menuAnimation.start()
            
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
    def deleteMemberButtonClicked(self):
        mayIDelete = QMessageBox.question(self, 'Delete Member', 'Are you sure you want to delete this member?',
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mayIDelete == QMessageBox.Yes:
            memberID = self.ui.MembersTableView.selectedIndexes()[0].data()
            deleteMember(memberID)
            self.refreshMembersTable()
    def editMemberButtonClicked(self):
        self.editMemberWindow = editRowWindow('member', self)
        self.editMemberWindow.show()
    
    def addNewBookButtonClicked(self, bookID):
        self.addNewBookWindow = addNewRowWindow('book', self)
        self.addNewBookWindow.show()
    def deleteBookButtonClicked(self):
        mayIDelete = QMessageBox.question(self, 'Delete Book', 'Are you sure you want to delete this book?',
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mayIDelete == QMessageBox.Yes:
            bookID = self.ui.BooksTableView.selectedIndexes()[0].data()
            deleteBook(bookID)
            self.refreshBooksTable()
    def editBookButtonClicked(self):
        self.editBookWindow = editRowWindow('book', self)
        self.editBookWindow.show()
        
    def borrowButtonClicked(self):
        self.borrowWindow = setBorrowedWindow(self)
        self.borrowWindow.show()
    def returnBorrowButtonClicked(self):
        mayIReturn = QMessageBox.question(self, 'Return Books', 'Does member returned these books?',
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mayIReturn == QMessageBox.Yes:
            borrowID = self.ui.BorrowsTableView.selectedIndexes()[0].data()
            memberID = self.ui.BorrowsTableView.selectedIndexes()[1].data()
            bookIDs = self.ui.BorrowsTableView.selectedIndexes()[2].data()
            returnBorrow(borrowID, memberID, bookIDs)
            self.refreshMembersTable()
            self.refreshBooksTable()
            self.refreshBorrowsTable()
    
    # - for Search
    def searchBooks(self):
        self.database.open()
        self.ui.BooksTableView.reset()
        self.booksTableModel = QSqlTableModel(self, self.database)
        self.booksTableModel.setTable('books')
        self.booksTableModel.setFilter("title LIKE '%" + self.ui.BooksSearchBox.text() + "%'")
        self.booksTableModel.select()
        self.ui.BooksTableView.setModel(self.booksTableModel)
        self.database.close()
        
    def searchMembers(self):
        self.database.open()
        self.ui.MembersTableView.reset()
        self.membersTableModel = QSqlTableModel(self, self.database)
        self.membersTableModel.setTable('members')
        self.membersTableModel.setFilter("name = '" + self.ui.MembersSearchBox.text() + "'")
        self.membersTableModel.select()
        self.ui.MembersTableView.setModel(self.membersTableModel)
        self.database.close()
    
    
    # ********************* Functions *********************
    # - for Database
    def refreshMembersTable(self):
        self.database.open()
        self.ui.MembersTableView.reset()
        self.membersTableModel = QSqlTableModel(self, self.database)
        self.membersTableModel.setTable('members')
        self.membersTableModel.select()
        self.ui.MembersTableView.setModel(self.membersTableModel)
        self.ui.MembersTableView.resizeColumnsToContents()
        self.database.close()
        
    def refreshBooksTable(self):
        self.database.open()
        self.ui.BooksTableView.reset()
        self.booksTableModel = QSqlTableModel(self, self.database)
        self.booksTableModel.setTable('books')
        self.booksTableModel.select()
        self.ui.BooksTableView.setModel(self.booksTableModel)
        self.ui.BooksTableView.resizeColumnsToContents()
        self.database.close()
        
    def refreshBorrowsTable(self):
        self.database.open()
        self.ui.BorrowsTableView.reset()
        self.borrowsTableModel = QSqlTableModel(self, self.database)
        self.borrowsTableModel.setTable('borrows')
        self.borrowsTableModel.select()
        self.ui.BorrowsTableView.setModel(self.borrowsTableModel)
        self.ui.BorrowsTableView.resizeColumnsToContents()
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
            input_list = MEMBERS_HEADERS_LIST.copy()
        else:
            input_list = BOOKS_HEADERS_LIST.copy()
            input_list.pop()
            
        for input_data in input_list:
            lineEdit = QLineEdit(self)
            lineEdit.setObjectName(input_data + 'LineEdit')
            self.centralLayout.addRow(self.tr('&' + input_data), lineEdit)
            
        if self.type == 'book':
            quantitySpinBox = QSpinBox(self)
            quantitySpinBox.setObjectName('quantitySpinBox')
            quantitySpinBox.setMinimum(1)
            self.centralLayout.addRow(self.tr('&Quantity'), quantitySpinBox)
            
        submitButton = QPushButton('Submit Informations', self)
        submitButton.clicked.connect(self.addInfoToDatabase)
        self.centralLayout.addWidget(submitButton)
            
        self.setLayout(self.centralLayout)
            
    def addInfoToDatabase(self):
        if self.areFieldsFull():
            mayIAdd = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to add this ' + self.type + '?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if mayIAdd == QMessageBox.Yes:
                if self.type == 'member':
                    addNewMember(self.findChild(QLineEdit, 'NameLineEdit').text(),
                                 self.findChild(QLineEdit, 'PhoneLineEdit').text(),
                                 self.findChild(QLineEdit, 'EmailLineEdit').text(),
                                 self.findChild(QLineEdit, 'AddressLineEdit').text())
                    self.parentWindow.refreshMembersTable()
                else:
                    addNewBook(self.findChild(QLineEdit, 'TitleLineEdit').text(),
                               self.findChild(QLineEdit, 'AuthorLineEdit').text(),
                               self.findChild(QLineEdit, 'PublisherLineEdit').text(),
                               self.findChild(QLineEdit, 'YearLineEdit').text(),
                               self.findChild(QSpinBox, 'quantitySpinBox').value())
                    self.parentWindow.refreshBooksTable()
            
                self.close()
            
        else:
            QMessageBox.warning(self, 'Error', 'Please fill all the fields!')
        
    def areFieldsFull(self):
        if self.type == 'member':
            if self.findChild(QLineEdit, 'NameLineEdit').text() == '' or \
               self.findChild(QLineEdit, 'PhoneLineEdit').text() == '' or \
               self.findChild(QLineEdit, 'EmailLineEdit').text() == '' or \
               self.findChild(QLineEdit, 'AddressLineEdit').text() == '':
                return False
        else:
            if self.findChild(QLineEdit, 'TitleLineEdit').text() == '' or \
               self.findChild(QLineEdit, 'AuthorLineEdit').text() == '' or \
               self.findChild(QLineEdit, 'PublisherLineEdit').text() == '' or \
               self.findChild(QLineEdit, 'YearLineEdit').text() == '':
                return False
        return True
        
class editRowWindow(QWidget):
    def __init__(self, type, parentWindow):
        super().__init__()
        self.type = type
        self.parentWindow = parentWindow
        
        self.ui_init()
        
    def ui_init(self):
        self.centralLayout = QFormLayout(self)
        
        title = QLabel(self)
        title.setText('Please change the ' + self.type + "'s information")
        self.centralLayout.addWidget(title)
        
        input_list = []
        if(self.type == 'member'):
            input_list = MEMBERS_HEADERS_LIST
        else:
            input_list = BOOKS_HEADERS_LIST
            input_list.pop()
            
        index = 1
        for input_data in input_list:
            lineEdit = QLineEdit(self)
            lineEdit.setObjectName(input_data + 'LineEdit')
            lineEdit.setText(self.parentWindow.ui.MembersTableView.selectedIndexes()[index].data())
            self.centralLayout.addRow(self.tr('&' + input_data), lineEdit)
            index += 1
            
        if self.type == 'book':
            quantitySpinBox = QSpinBox(self)
            quantitySpinBox.setObjectName('quantitySpinBox')
            quantitySpinBox.setValue(int(self.parentWindow.ui.BooksTableView.selectedIndexes()[5].data()))
            quantitySpinBox.setMinimum(1)
            self.centralLayout.addRow(self.tr('&Quantity'), quantitySpinBox)
            
        submitButton = QPushButton('Submit Informations', self)
        submitButton.clicked.connect(self.editInfoToDatabase)
        self.centralLayout.addWidget(submitButton)
            
        self.setLayout(self.centralLayout)
            
    def editInfoToDatabase(self):
        if self.areFieldsFull():
            mayIEdit = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to edit this ' + self.type + '?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if mayIEdit == QMessageBox.Yes:
                if self.type == 'member':
                    editMember(self.parentWindow.ui.MembersTableView.selectedIndexes()[0].data(),
                            self.findChild(QLineEdit, 'NameLineEdit').text(),
                            self.findChild(QLineEdit, 'PhoneLineEdit').text(),
                            self.findChild(QLineEdit, 'EmailLineEdit').text(),
                            self.findChild(QLineEdit, 'AddressLineEdit').text())
                    self.parentWindow.refreshMembersTable()
                else:
                    editBook(self.parentWindow.ui.BooksTableView.selectedIndexes()[0].data(),
                            self.findChild(QLineEdit, 'TitleLineEdit').text(),
                            self.findChild(QLineEdit, 'AuthorLineEdit').text(),
                            self.findChild(QLineEdit, 'PublisherLineEdit').text(),
                            self.findChild(QLineEdit, 'YearLineEdit').text(),
                            self.findChild(QSpinBox, 'quantitySpinBox').value())
                    self.parentWindow.refreshBooksTable()
            
                self.close()
            
        else:
            QMessageBox.warning(self, 'Error', 'Fields should not be empty!')
        
    def areFieldsFull(self):
        if self.type == 'member':
            if self.findChild(QLineEdit, 'NameLineEdit').text() == '' or \
               self.findChild(QLineEdit, 'PhoneLineEdit').text() == '' or \
               self.findChild(QLineEdit, 'EmailLineEdit').text() == '' or \
               self.findChild(QLineEdit, 'AddressLineEdit').text() == '':
                return False
        else:
            if self.findChild(QLineEdit, 'TitleLineEdit').text() == '' or \
               self.findChild(QLineEdit, 'AuthorLineEdit').text() == '' or \
               self.findChild(QLineEdit, 'PublisherLineEdit').text() == '' or \
               self.findChild(QLineEdit, 'YearLineEdit').text() == '':
                return False
        return True
        
class setBorrowedWindow(QWidget):
    def __init__(self, parentWindow):
        super().__init__()
        self.parentWindow = parentWindow
        
        self.ui_init()
        
    def ui_init(self):
        self.centralLayout = QGridLayout(self)
        
        self.member_id_title = QLabel(self, text='Member ID')
        self.member_id_input = QLineEdit(self)
        self.member_id_input.setReadOnly(True)
        self.member_id_selector = QPushButton(self, text='Select Member From Table')
        self.member_id_selector.clicked.connect(self.selectFromMembersTable)
        
        self.book_ids_title = QLabel(self, text='Book IDs')
        self.book_ids_input = QLineEdit(self)
        self.book_ids_input.textChanged.connect(self.removeFirstComma)
        self.book_ids_selector = QPushButton(self, text='Add Book From Table')
        self.book_ids_selector.clicked.connect(self.addFromBooksTable)
        
        self.borrow_date_title = QLabel(self, text='Borrow Date')
        self.borrow_date_input = QDateEdit(self)
        self.borrow_date_input.setCalendarPopup(True)
        self.borrow_date_input.setMinimumDate(QDate.currentDate())
        self.borrow_date_input.setMaximumDate(QDate.currentDate())
        
        self.return_date_title = QLabel(self, text='Return Date')
        self.return_date_input = QDateEdit(self)
        self.return_date_input.setDate(QDate.currentDate())
        self.return_date_input.setCalendarPopup(True)
        self.return_date_input.setDate(QDate.currentDate().addDays(7))
        self.return_date_input.setMinimumDate(QDate.currentDate())
        self.return_date_input.setMaximumDate(QDate.currentDate().addDays(30))
        
        self.parentWindow.database.open()
        
        self.members_table = QTableView(self)
        self.members_table.setSelectionBehavior(QTableView.SelectRows)
        self.members_table.setSelectionMode(QTableView.SingleSelection)
        self.members_table.setEditTriggers(QTableView.NoEditTriggers)
        self.members_table_model = QSqlTableModel(self, self.parentWindow.database)
        self.members_table_model.setTable('members')
        self.members_table_model.select()
        self.members_table.setModel(self.members_table_model)
        self.members_table.resizeColumnsToContents()
        
        self.books_table = QTableView(self)
        self.books_table.setSelectionBehavior(QTableView.SelectRows)
        self.books_table.setSelectionMode(QTableView.SingleSelection)
        self.books_table.setEditTriggers(QTableView.NoEditTriggers)
        self.books_table_model = QSqlTableModel(self, self.parentWindow.database)
        self.books_table_model.setTable('books')
        self.books_table_model.select()
        self.books_table.setModel(self.books_table_model)
        self.books_table.resizeColumnsToContents()
        
        self.parentWindow.database.close()
        
        self.tables_tabs= QTabWidget(self)
        self.tables_tabs.addTab(self.members_table, 'Members')
        self.tables_tabs.addTab(self.books_table, 'Books')
        
        self.submitButton = QPushButton('Submit', self)
        self.submitButton.clicked.connect(self.submit)
        
        self.centralLayout.addWidget(self.member_id_title, 0, 0)
        self.centralLayout.addWidget(self.member_id_input, 0, 1)
        self.centralLayout.addWidget(self.member_id_selector, 0, 2)
        self.centralLayout.addWidget(self.book_ids_title, 1, 0)
        self.centralLayout.addWidget(self.book_ids_input, 1, 1)
        self.centralLayout.addWidget(self.book_ids_selector, 1, 2)
        self.centralLayout.addWidget(self.borrow_date_title, 2, 0)
        self.centralLayout.addWidget(self.borrow_date_input, 2, 1)
        self.centralLayout.addWidget(self.return_date_title, 3, 0)
        self.centralLayout.addWidget(self.return_date_input, 3, 1)
        self.centralLayout.addWidget(self.tables_tabs, 4, 0, 1, 3)
        self.centralLayout.addWidget(self.submitButton, 5, 0, 1, 3)
        
    def selectFromMembersTable(self):
        self.member_id_input.setText(str(self.members_table.selectedIndexes()[0].data()))
        
    def addFromBooksTable(self):
        if str(self.books_table.selectedIndexes()[0].data()) not in self.book_ids_input.text():
            self.book_ids_input.setText(self.book_ids_input.text() + ',' + str(self.books_table.selectedIndexes()[0].data()))
        else:
            QMessageBox.warning(self, 'Error', 'This book is already in the list')
            
    def removeFirstComma(self):
        if self.book_ids_input.text()[0] == ',':
            self.book_ids_input.setText(self.book_ids_input.text()[1:])
            
    def doesMemberHavePremission(self):
        if self.members_table.selectedIndexes()[5].data() == 1:
            return True
        return False
    
    def areBooksAvailable(self):
        for book_id in self.book_ids_input.text().split(','):
            if self.books_table.selectedIndexes()[5].data() == 0:
                return False
        return True
            
    def submit(self):
        if self.member_id_input.text() == '' or self.book_ids_input.text() == '':
            QMessageBox.warning(self, 'Error', 'Please fill all the fields')
        else:
            if self.doesMemberHavePremission():
                if self.areBooksAvailable():
                    mayisubmitBorrow = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to submit this borrow?',
                                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if mayisubmitBorrow == QMessageBox.Yes:
                        borrowBook(self.member_id_input.text(),
                                self.book_ids_input.text(),
                                self.borrow_date_input.date().toString('yyyy-MM-dd'),
                                self.return_date_input.date().toString('yyyy-MM-dd'))
                        self.parentWindow.refreshMembersTable()
                        self.parentWindow.refreshBooksTable()
                        self.parentWindow.refreshBorrowsTable()
                        self.close()
                else:
                    QMessageBox.warning(self, 'Error', 'One or more books are not available')
            else:
                QMessageBox.warning(self, 'Error', 'This member does not have permission to borrow books')

        
def ShowWindows():
    app = QApplication(sys.argv)
    mainWin = MainWindow()

    mainWin.show()

    sys.exit(app.exec_())