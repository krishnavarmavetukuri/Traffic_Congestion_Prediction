import sys
import os
from adminOps import *
from PyQt5 import QtWidgets, QtGui, QtCore

class AdminOpsForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.backup_junction_table)
        self.ui.pushButton_2.clicked.connect(self.backup_traffic_details_table)
        self.ui.pushButton_4.clicked.connect(self.load_initial_traffic_to_db)
        self.ui.pushButton_5.clicked.connect(self.generate_backup_csvs)
        self.ui.pushButton_6.clicked.connect(self.generate_backup_trafficset_csv)

    def backup_junction_table(self):
        os.system("python load_jndtls_DBtable_csv_to_db.py")

    def backup_traffic_details_table(self):
        os.system("python load_trfcdtls_DBtable_csv_to_db.py")

    def load_initial_traffic_to_db(self):
        os.system("python load_intial_traffic_csv_to_db.py")

    def generate_backup_csvs(self):
        os.system("python backup_DB_tables_to_csv.py")

    def generate_backup_trafficset_csv(self):
        os.system("python backup_trafficset_to_csv.py")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    admin_app = AdminOpsForm()
    admin_app.show()
    sys.exit(app.exec_())
