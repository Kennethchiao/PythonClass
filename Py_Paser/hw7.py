# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Thu Jul 18 16:17:56 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.oper = ''
        self.num1=0
        self.num2=0
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(357, 253)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 321, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(240, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 357, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.btn_add)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()"), self.btn_equal)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "+", None))
        self.pushButton_2.setText(_translate("MainWindow", "-", None))
        self.pushButton_3.setText(_translate("MainWindow", "*", None))
        self.pushButton_4.setText(_translate("MainWindow", "/", None))
        self.pushButton_5.setText(_translate("MainWindow", "C", None))
        self.pushButton_6.setText(_translate("MainWindow", "=", None))

    def btn_add(self):
        if self.num1 == 0:
            self.num1 = int(self.lineEdit.text())
        else:
            self.num1 = self.num1 + int(self.lineEdit.text())
            print(self.num1)
    def btn_equal(self):
        print(self.num1 + int(self.lineEdit.text()))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
