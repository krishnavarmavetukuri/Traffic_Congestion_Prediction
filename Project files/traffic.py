# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'traffic.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 441)
        MainWindow.setStyleSheet("color: rgb(170, 0, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 310, 401, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 100, 31, 33))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 140, 31, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(300, 180, 31, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 220, 31, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 251, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 241, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 241, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 180, 241, 31))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 260, 241, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 260, 31, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(210, 20, 391, 33))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 20, 151, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 60, 821, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(710, 140, 31, 33))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(440, 180, 241, 31))
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(710, 180, 31, 33))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(440, 100, 251, 31))
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(710, 100, 31, 33))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(440, 140, 241, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(440, 220, 241, 31))
        self.label_12.setObjectName("label_12")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(710, 260, 31, 33))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(710, 220, 31, 33))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(440, 260, 241, 31))
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Traffic Details at the Junction"))
        self.pushButton.setText(_translate("MainWindow", "Store Traffic Details in Data base"))
        self.label_3.setText(_translate("MainWindow", "Traffic in incoming Road 1:"))
        self.label_4.setText(_translate("MainWindow", "Traffic in incoming Road 2:"))
        self.label_5.setText(_translate("MainWindow", "Traffic in incoming Road 4:"))
        self.label_6.setText(_translate("MainWindow", "Traffic in incoming Road 3:"))
        self.label_2.setText(_translate("MainWindow", "Traffic in incoming Road 5:"))
        self.label_7.setText(_translate("MainWindow", "Junction Name:"))
        self.label_8.setText(_translate("MainWindow", "Note: Use a scale of 0 to 5, with 5 standing for heavy traffic, while giving following inputs."))
        self.label_9.setText(_translate("MainWindow", "Traffic in outgoing Road 3:"))
        self.label_10.setText(_translate("MainWindow", "Traffic in outgoing Road 1:"))
        self.label_11.setText(_translate("MainWindow", "Traffic in outgoing Road 2:"))
        self.label_12.setText(_translate("MainWindow", "Traffic in outgoing Road 4:"))
        self.label_13.setText(_translate("MainWindow", "Traffic in outgoing Road 5:"))
