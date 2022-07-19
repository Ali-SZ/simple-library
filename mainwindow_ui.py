# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(991, 600)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MenuButtonsFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MenuButtonsFrame.sizePolicy().hasHeightForWidth())
        self.MenuButtonsFrame.setSizePolicy(sizePolicy)
        self.MenuButtonsFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.MenuButtonsFrame.setObjectName("MenuButtonsFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MenuButtonsFrame)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MenuButton = QtWidgets.QPushButton(self.MenuButtonsFrame)
        self.MenuButton.setMinimumSize(QtCore.QSize(175, 40))
        self.MenuButton.setIconSize(QtCore.QSize(25, 25))
        self.MenuButton.setObjectName("MenuButton")
        self.verticalLayout.addWidget(self.MenuButton, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ToMemebersPageButton = QtWidgets.QPushButton(self.MenuButtonsFrame)
        self.ToMemebersPageButton.setMinimumSize(QtCore.QSize(0, 40))
        self.ToMemebersPageButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ToMemebersPageButton.setIconSize(QtCore.QSize(25, 25))
        self.ToMemebersPageButton.setObjectName("ToMemebersPageButton")
        self.verticalLayout.addWidget(self.ToMemebersPageButton, 0, QtCore.Qt.AlignVCenter)
        self.ToBooksPageButton = QtWidgets.QPushButton(self.MenuButtonsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToBooksPageButton.sizePolicy().hasHeightForWidth())
        self.ToBooksPageButton.setSizePolicy(sizePolicy)
        self.ToBooksPageButton.setMinimumSize(QtCore.QSize(0, 40))
        self.ToBooksPageButton.setIconSize(QtCore.QSize(25, 25))
        self.ToBooksPageButton.setObjectName("ToBooksPageButton")
        self.verticalLayout.addWidget(self.ToBooksPageButton, 0, QtCore.Qt.AlignVCenter)
        self.ToBorrowPageButton = QtWidgets.QPushButton(self.MenuButtonsFrame)
        self.ToBorrowPageButton.setMinimumSize(QtCore.QSize(0, 40))
        self.ToBorrowPageButton.setIconSize(QtCore.QSize(25, 25))
        self.ToBorrowPageButton.setObjectName("ToBorrowPageButton")
        self.verticalLayout.addWidget(self.ToBorrowPageButton, 0, QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.MenuButtonsFrame)
        self.Pages = QtWidgets.QStackedWidget(self.centralwidget)
        self.Pages.setMinimumSize(QtCore.QSize(800, 600))
        self.Pages.setObjectName("Pages")
        self.MembersPage = QtWidgets.QWidget()
        self.MembersPage.setObjectName("MembersPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.MembersPage)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.MembersPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MembersImage = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MembersImage.sizePolicy().hasHeightForWidth())
        self.MembersImage.setSizePolicy(sizePolicy)
        self.MembersImage.setMaximumSize(QtCore.QSize(50, 50))
        self.MembersImage.setObjectName("MembersImage")
        self.horizontalLayout_2.addWidget(self.MembersImage)
        self.MembersLable = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MembersLable.sizePolicy().hasHeightForWidth())
        self.MembersLable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.MembersLable.setFont(font)
        self.MembersLable.setObjectName("MembersLable")
        self.horizontalLayout_2.addWidget(self.MembersLable)
        self.verticalLayout_3.addWidget(self.widget)
        spacerItem2 = QtWidgets.QSpacerItem(20, 106, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.MembersTableView = QtWidgets.QTableView(self.MembersPage)
        self.MembersTableView.setMinimumSize(QtCore.QSize(0, 350))
        self.MembersTableView.setObjectName("MembersTableView")
        self.verticalLayout_3.addWidget(self.MembersTableView)
        self.widget_5 = QtWidgets.QWidget(self.MembersPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.AddMemberButton = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddMemberButton.sizePolicy().hasHeightForWidth())
        self.AddMemberButton.setSizePolicy(sizePolicy)
        self.AddMemberButton.setMinimumSize(QtCore.QSize(0, 30))
        self.AddMemberButton.setObjectName("AddMemberButton")
        self.horizontalLayout_5.addWidget(self.AddMemberButton)
        self.DeleteMemberButton = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeleteMemberButton.sizePolicy().hasHeightForWidth())
        self.DeleteMemberButton.setSizePolicy(sizePolicy)
        self.DeleteMemberButton.setMinimumSize(QtCore.QSize(0, 30))
        self.DeleteMemberButton.setObjectName("DeleteMemberButton")
        self.horizontalLayout_5.addWidget(self.DeleteMemberButton)
        self.EditMemberButton = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EditMemberButton.sizePolicy().hasHeightForWidth())
        self.EditMemberButton.setSizePolicy(sizePolicy)
        self.EditMemberButton.setMinimumSize(QtCore.QSize(0, 30))
        self.EditMemberButton.setObjectName("EditMemberButton")
        self.horizontalLayout_5.addWidget(self.EditMemberButton)
        self.verticalLayout_3.addWidget(self.widget_5, 0, QtCore.Qt.AlignLeft)
        self.Pages.addWidget(self.MembersPage)
        self.BooksPage = QtWidgets.QWidget()
        self.BooksPage.setObjectName("BooksPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.BooksPage)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_3 = QtWidgets.QWidget(self.BooksPage)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.BooksImage = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BooksImage.sizePolicy().hasHeightForWidth())
        self.BooksImage.setSizePolicy(sizePolicy)
        self.BooksImage.setMaximumSize(QtCore.QSize(50, 50))
        self.BooksImage.setObjectName("BooksImage")
        self.horizontalLayout_6.addWidget(self.BooksImage)
        self.BooksLable = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BooksLable.sizePolicy().hasHeightForWidth())
        self.BooksLable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BooksLable.setFont(font)
        self.BooksLable.setObjectName("BooksLable")
        self.horizontalLayout_6.addWidget(self.BooksLable)
        self.verticalLayout_5.addWidget(self.widget_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 112, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.BooksTableView = QtWidgets.QTableView(self.BooksPage)
        self.BooksTableView.setMinimumSize(QtCore.QSize(0, 350))
        self.BooksTableView.setObjectName("BooksTableView")
        self.verticalLayout_5.addWidget(self.BooksTableView)
        self.widget_7 = QtWidgets.QWidget(self.BooksPage)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.AddBookButton = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddBookButton.sizePolicy().hasHeightForWidth())
        self.AddBookButton.setSizePolicy(sizePolicy)
        self.AddBookButton.setMinimumSize(QtCore.QSize(0, 30))
        self.AddBookButton.setObjectName("AddBookButton")
        self.horizontalLayout_8.addWidget(self.AddBookButton, 0, QtCore.Qt.AlignLeft)
        self.DeleteBookButton = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeleteBookButton.sizePolicy().hasHeightForWidth())
        self.DeleteBookButton.setSizePolicy(sizePolicy)
        self.DeleteBookButton.setMinimumSize(QtCore.QSize(0, 30))
        self.DeleteBookButton.setObjectName("DeleteBookButton")
        self.horizontalLayout_8.addWidget(self.DeleteBookButton)
        self.EditBookButton = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EditBookButton.sizePolicy().hasHeightForWidth())
        self.EditBookButton.setSizePolicy(sizePolicy)
        self.EditBookButton.setMinimumSize(QtCore.QSize(0, 30))
        self.EditBookButton.setObjectName("EditBookButton")
        self.horizontalLayout_8.addWidget(self.EditBookButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_5.addWidget(self.widget_7)
        self.Pages.addWidget(self.BooksPage)
        self.BorrowPage = QtWidgets.QWidget()
        self.BorrowPage.setObjectName("BorrowPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.BorrowPage)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_8 = QtWidgets.QWidget(self.BorrowPage)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.BorrowsImage = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BorrowsImage.sizePolicy().hasHeightForWidth())
        self.BorrowsImage.setSizePolicy(sizePolicy)
        self.BorrowsImage.setObjectName("BorrowsImage")
        self.horizontalLayout_10.addWidget(self.BorrowsImage)
        self.label_7 = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.verticalLayout_2.addWidget(self.widget_8)
        spacerItem5 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.label = QtWidgets.QLabel(self.BorrowPage)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.BorrowsTableView = QtWidgets.QTableView(self.BorrowPage)
        self.BorrowsTableView.setObjectName("BorrowsTableView")
        self.verticalLayout_2.addWidget(self.BorrowsTableView)
        self.widget_2 = QtWidgets.QWidget(self.BorrowPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.AddBorrowButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddBorrowButton.sizePolicy().hasHeightForWidth())
        self.AddBorrowButton.setSizePolicy(sizePolicy)
        self.AddBorrowButton.setMinimumSize(QtCore.QSize(0, 30))
        self.AddBorrowButton.setObjectName("AddBorrowButton")
        self.horizontalLayout_3.addWidget(self.AddBorrowButton)
        self.ReturnBorrowButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ReturnBorrowButton.sizePolicy().hasHeightForWidth())
        self.ReturnBorrowButton.setSizePolicy(sizePolicy)
        self.ReturnBorrowButton.setMinimumSize(QtCore.QSize(0, 30))
        self.ReturnBorrowButton.setObjectName("ReturnBorrowButton")
        self.horizontalLayout_3.addWidget(self.ReturnBorrowButton)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.Pages.addWidget(self.BorrowPage)
        self.horizontalLayout.addWidget(self.Pages)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MenuButton.setText(_translate("MainWindow", "  Menu"))
        self.ToMemebersPageButton.setText(_translate("MainWindow", "  Members"))
        self.ToBooksPageButton.setText(_translate("MainWindow", "  Books"))
        self.ToBorrowPageButton.setText(_translate("MainWindow", "  Borrow"))
        self.MembersImage.setText(_translate("MainWindow", "_MembersImage"))
        self.MembersLable.setText(_translate("MainWindow", "Members"))
        self.AddMemberButton.setText(_translate("MainWindow", "   Add New Member   "))
        self.DeleteMemberButton.setText(_translate("MainWindow", "   Delete Member   "))
        self.EditMemberButton.setText(_translate("MainWindow", "   Edit Member\'s Information   "))
        self.BooksImage.setText(_translate("MainWindow", "_BooksImage"))
        self.BooksLable.setText(_translate("MainWindow", "Books"))
        self.AddBookButton.setText(_translate("MainWindow", "   Add New Book   "))
        self.DeleteBookButton.setText(_translate("MainWindow", "   Delete Book   "))
        self.EditBookButton.setText(_translate("MainWindow", "   Edit Book\'s Information   "))
        self.BorrowsImage.setText(_translate("MainWindow", "_borrowImage"))
        self.label_7.setText(_translate("MainWindow", "Borrows"))
        self.label.setText(_translate("MainWindow", "List of Borrows"))
        self.AddBorrowButton.setText(_translate("MainWindow", "   Add Borrow   "))
        self.ReturnBorrowButton.setText(_translate("MainWindow", "   Return Borrow   "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
