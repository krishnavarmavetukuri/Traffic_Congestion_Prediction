import sqlite3
import csv
con = sqlite3.connect('traffic1')
cur = con.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS jndtls (
        jname varchar(40),
        cname varchar(40),
        njunc varchar(40),
        distnj char(2),
        sgnlsno char(2),
        inroadsno char(2),
        outroadsno char(2)
    )
''')
cur.execute('DELETE FROM jndtls;')

with open('backup_jndtls.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        cur.execute('INSERT INTO jndtls VALUES (?, ?, ?, ?, ?, ?, ?)', row)
con.commit()
con.close()

print('Data inserted into jndtls table successfully.')
