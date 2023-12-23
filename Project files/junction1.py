import sys
import os
from junction import *
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
      cname = str(self.ui.lineEdit_4.text())
      njunc = str(self.ui.lineEdit_5.text())
      distnj = str(self.ui.lineEdit_6.text())
      sgnlsno = str(self.ui.lineEdit_7.text())
      inroadsno = str(self.ui.lineEdit_8.text())
      outroadsno = str(self.ui.lineEdit_10.text())
      cur.execute('INSERT INTO jndtls(jname,cname,njunc,distnj,sgnlsno,inroadsno,outroadsno) VALUES(?,?,?,?,?,?,?)',(jname,cname,njunc,distnj,sgnlsno,inroadsno,outroadsno))
      con.commit()

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
