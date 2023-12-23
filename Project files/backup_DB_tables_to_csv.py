import sqlite3
import csv
con = sqlite3.connect('traffic1')
cur = con.cursor()

cur.execute('SELECT * FROM jndtls;')# For Junction Table
rows = cur.fetchall()
fp = open('backup_jndtls.csv', 'w', newline='')  # Use 'newline='' for Windows compatibility
myFile = csv.writer(fp)
myFile.writerows([["jname", "cname", "njunc", "distnj", "sgnlsno", "inroadsno", "outroadsno"]])
myFile.writerows(rows)
fp.close()
print('backup_jndtls.csv file successfully created')

cur.execute('SELECT * FROM trfcdtls;')# For Traffic Details Table
rows = cur.fetchall()
fp = open('backup_trfcdtls.csv', 'w', newline='')  # Use 'newline='' for Windows compatibility
myFile = csv.writer(fp)
myFile.writerows([["jname", "RD_tfc_N1i", "RD_tfc_N1o", "RD_tfc_N2i", "RD_tfc_N2o", "RD_tfc_S1i", "RD_tfc_S1o", "RD_tfc_E1i", "RD_tfc_E1o", "RD_tfc_W1i", "RD_tfc_W1o"]])
myFile.writerows(rows)
fp.close()
print('backup_trfcdtls.csv file successfully created')

con.commit()
con.close()


