import sqlite3
import csv
con = sqlite3.connect('traffic1') 
cur = con.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS trfcdtls (
    jname varchar(40),
    RD_tfc_N1i char(1),
    RD_tfc_N1o char(1),
    RD_tfc_N2i char(1),
    RD_tfc_N2o char(1),
    RD_tfc_S1i char(1),
    RD_tfc_S1o char(1),
    RD_tfc_E1i char(1),
    RD_tfc_E1o char(1),
    RD_tfc_W1i char(1),
    RD_tfc_W1o char(1)
);
''')
cur.execute('DELETE FROM trfcdtls;')
with open('backup_trfcdtls.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) 
    for row in csvreader:
        cur.execute('INSERT INTO trfcdtls VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)
con.commit()
con.close()

print('Data inserted into trfcdtls table successfully.')
