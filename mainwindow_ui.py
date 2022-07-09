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
        MainWindow.resize(981, 600)
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
        self.MenuButtonsWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MenuButtonsWidget.sizePolicy().hasHeightForWidth())
        self.MenuButtonsWidget.setSizePolicy(sizePolicy)
        self.MenuButtonsWidget.setObjectName("MenuButtonsWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MenuButtonsWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MenuButton = QtWidgets.QPushButton(self.MenuButtonsWidget)
        self.MenuButton.setMinimumSize(QtCore.QSize(175, 40))
        self.MenuButton.setObjectName("MenuButton")
        self.verticalLayout.addWidget(self.MenuButton, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.ToMemebersPageButton = QtWidgets.QPushButton(self.MenuButtonsWidget)
        self.ToMemebersPageButton.setMinimumSize(QtCore.QSize(175, 40))
        self.ToMemebersPageButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ToMemebersPageButton.setObjectName("ToMemebersPageButton")
        self.verticalLayout.addWidget(self.ToMemebersPageButton, 0, QtCore.Qt.AlignVCenter)
        self.ToBooksPageButton = QtWidgets.QPushButton(self.MenuButtonsWidget)
        self.ToBooksPageButton.setMinimumSize(QtCore.QSize(0, 40))
        self.ToBooksPageButton.setObjectName("ToBooksPageButton")
        self.verticalLayout.addWidget(self.ToBooksPageButton, 0, QtCore.Qt.AlignVCenter)
        self.ToBorrowPageButton = QtWidgets.QPushButton(self.MenuButtonsWidget)
        self.ToBorrowPageButton.setMinimumSize(QtCore.QSize(0, 40))
        self.ToBorrowPageButton.setObjectName("ToBorrowPageButton")
        self.verticalLayout.addWidget(self.ToBorrowPageButton, 0, QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.SettingButton = QtWidgets.QPushButton(self.MenuButtonsWidget)
        self.SettingButton.setMinimumSize(QtCore.QSize(175, 40))
        self.SettingButton.setObjectName("SettingButton")
        self.verticalLayout.addWidget(self.SettingButton, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.MenuButtonsWidget)
        self.Pages = QtWidgets.QStackedWidget(self.centralwidget)
        self.Pages.setMinimumSize(QtCore.QSize(800, 600))
        self.Pages.setObjectName("Pages")
        self.MembersPage = QtWidgets.QWidget()
        self.MembersPage.setObjectName("MembersPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.MembersPage)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
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
        self.MembersImage.setObjectName("MembersImage")
        self.horizontalLayout_2.addWidget(self.MembersImage)
        self.MembersLable = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
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
        self.widget_2 = QtWidgets.QWidget(self.MembersPage)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.ActiveMembersLable = QtWidgets.QLabel(self.widget_2)
        self.ActiveMembersLable.setObjectName("ActiveMembersLable")
        self.horizontalLayout_3.addWidget(self.ActiveMembersLable)
        spacerItem3 = QtWidgets.QSpacerItem(486, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.DeactiveMembersLable = QtWidgets.QLabel(self.widget_2)
        self.DeactiveMembersLable.setObjectName("DeactiveMembersLable")
        self.horizontalLayout_3.addWidget(self.DeactiveMembersLable)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.MembersListWidget = QtWidgets.QListWidget(self.MembersPage)
        self.MembersListWidget.setMinimumSize(QtCore.QSize(0, 350))
        self.MembersListWidget.setObjectName("MembersListWidget")
        self.verticalLayout_3.addWidget(self.MembersListWidget)
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
        self.MemberInfoButton = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MemberInfoButton.sizePolicy().hasHeightForWidth())
        self.MemberInfoButton.setSizePolicy(sizePolicy)
        self.MemberInfoButton.setMinimumSize(QtCore.QSize(0, 30))
        self.MemberInfoButton.setObjectName("MemberInfoButton")
        self.horizontalLayout_5.addWidget(self.MemberInfoButton)
        self.verticalLayout_3.addWidget(self.widget_5, 0, QtCore.Qt.AlignLeft)
        self.Pages.addWidget(self.MembersPage)
        self.BooksPage = QtWidgets.QWidget()
        self.BooksPage.setObjectName("BooksPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.BooksPage)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
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
        spacerItem4 = QtWidgets.QSpacerItem(20, 112, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.widget_4 = QtWidgets.QWidget(self.BooksPage)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.BooksCounterLable = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BooksCounterLable.sizePolicy().hasHeightForWidth())
        self.BooksCounterLable.setSizePolicy(sizePolicy)
        self.BooksCounterLable.setObjectName("BooksCounterLable")
        self.horizontalLayout_7.addWidget(self.BooksCounterLable)
        self.verticalLayout_5.addWidget(self.widget_4)
        self.BooksListWdget = QtWidgets.QListWidget(self.BooksPage)
        self.BooksListWdget.setMinimumSize(QtCore.QSize(0, 350))
        self.BooksListWdget.setObjectName("BooksListWdget")
        self.verticalLayout_5.addWidget(self.BooksListWdget)
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
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_8.addWidget(self.pushButton_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout_5.addWidget(self.widget_7)
        self.Pages.addWidget(self.BooksPage)
        self.BorrowPage = QtWidgets.QWidget()
        self.BorrowPage.setObjectName("BorrowPage")
        self.Pages.addWidget(self.BorrowPage)
        self.horizontalLayout.addWidget(self.Pages)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pages.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MenuButton.setText(_translate("MainWindow", "Menu"))
        self.ToMemebersPageButton.setText(_translate("MainWindow", "Members"))
        self.ToBooksPageButton.setText(_translate("MainWindow", "Books"))
        self.ToBorrowPageButton.setText(_translate("MainWindow", "Borrow"))
        self.SettingButton.setText(_translate("MainWindow", "Setting"))
        self.MembersImage.setText(_translate("MainWindow", "_MembersImage"))
        self.MembersLable.setText(_translate("MainWindow", "Members"))
        self.label.setText(_translate("MainWindow", "Active Members: "))
        self.ActiveMembersLable.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Deactive Members: "))
        self.DeactiveMembersLable.setText(_translate("MainWindow", "0"))
        self.AddMemberButton.setText(_translate("MainWindow", "Add New Member"))
        self.DeleteMemberButton.setText(_translate("MainWindow", "Delete Member"))
        self.MemberInfoButton.setText(_translate("MainWindow", "Member\'s Information"))
        self.BooksImage.setText(_translate("MainWindow", "_BooksImage"))
        self.BooksLable.setText(_translate("MainWindow", "Books"))
        self.label_5.setText(_translate("MainWindow", "Number of Books: "))
        self.BooksCounterLable.setText(_translate("MainWindow", "0"))
        self.AddBookButton.setText(_translate("MainWindow", "Add New Book"))
        self.DeleteBookButton.setText(_translate("MainWindow", "Delete Book"))
        self.pushButton_5.setText(_translate("MainWindow", "Book\'s Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
