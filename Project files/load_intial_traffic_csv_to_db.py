import sqlite3
import csv
conn = sqlite3.connect('traffic1')
cur = conn.cursor()
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

with open('trafficset1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        jname = 'JNTU'
        RD_tfc_N1i,RD_tfc_N1o,RD_tfc_N2i,RD_tfc_N2o,RD_tfc_S1i,RD_tfc_S1o,RD_tfc_E1i,RD_tfc_E1o,RD_tfc_W1i,RD_tfc_W1o,RD_tfc_Total = map(int, row)  # Skip the last column 'Total'
        cur.execute('''
            INSERT INTO trfcdtls VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (jname, str(RD_tfc_N1i), str(RD_tfc_N1o), str(RD_tfc_N2i), str(RD_tfc_N2o), str(RD_tfc_S1i), str(RD_tfc_S1o), str(RD_tfc_E1i), str(RD_tfc_E1o), str(RD_tfc_W1i), str(RD_tfc_W1o)))

conn.commit()
conn.close()
print("Data from CSV has been successfully inserted into the 'trfcdtls' table.")
