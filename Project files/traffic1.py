import sys
import os
from traffic import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('traffic1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues)

  def insertvalues(self):
    with con:
      cur = con.cursor()
      jname = str(self.ui.lineEdit_9.text())
      RD_tfc_N1i = str(self.ui.lineEdit_3.text())
      RD_tfc_N1o = str(self.ui.lineEdit_4.text())
      RD_tfc_N2i = str(self.ui.lineEdit_5.text())
      RD_tfc_N2o = str(self.ui.lineEdit_6.text())
      RD_tfc_S1i = str(self.ui.lineEdit_2.text())
      RD_tfc_S1o = str(self.ui.lineEdit_10.text())
      RD_tfc_E1i = str(self.ui.lineEdit_7.text())
      RD_tfc_E1o = str(self.ui.lineEdit_8.text())
      RD_tfc_W1i = str(self.ui.lineEdit_12.text())
      RD_tfc_W1o = str(self.ui.lineEdit_11.text())
      cur.execute('INSERT INTO trfcdtls(jname,RD_tfc_N1i,RD_tfc_N1o,RD_tfc_N2i,RD_tfc_N2o,RD_tfc_S1i,RD_tfc_S1o,RD_tfc_E1i,RD_tfc_E1o,RD_tfc_W1i,RD_tfc_W1o) VALUES(?,?,?,?,?,?,?,?,?,?,?)',(jname,RD_tfc_N1i,RD_tfc_N1o,RD_tfc_N2i,RD_tfc_N2o,RD_tfc_S1i,RD_tfc_S1o,RD_tfc_E1i,RD_tfc_E1o,RD_tfc_W1i,RD_tfc_W1o))
      con.commit()

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
