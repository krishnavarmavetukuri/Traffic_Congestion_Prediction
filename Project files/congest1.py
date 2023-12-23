import sys
import os
from congest import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.trdtls)
     self.ui.pushButton_2.clicked.connect(self.dfexists)
     self.ui.pushButton_4.clicked.connect(self.blstm)
     self.ui.pushButton_5.clicked.connect(self.jndtls)
     self.ui.pushButton_6.clicked.connect(self.admin_ops)
     
  def trdtls(self):
    os.system("python traffic1.py")

  def dfexists(self):
    os.system("python file_existance1.py")

  def blstm(self):
    os.system("python -W ignore bidirect_lstm1.py")

  def jndtls(self):
    os.system("python junction1.py")

  def admin_ops(self):
    os.system("python adminOps1.py")

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
