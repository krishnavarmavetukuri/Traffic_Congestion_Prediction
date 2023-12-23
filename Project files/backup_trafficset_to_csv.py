import sqlite3
import csv
conn = sqlite3.connect('traffic1')
cursor = conn.cursor()
cursor.execute('SELECT * FROM trfcdtls;')
rows = cursor.fetchall()
modified_data = []

for row in rows:
    traffic_data = list(map(int, row[1:11]))
    total = sum(traffic_data)
    modified_data.append(traffic_data + [total])
conn.close()

with open('trafficset_backup.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([ "RD_tfc_N1i", "RD_tfc_N1o", "RD_tfc_N2i", "RD_tfc_N2o", "RD_tfc_S1i", "RD_tfc_S1o", "RD_tfc_E1i", "RD_tfc_E1o", "RD_tfc_W1i", "RD_tfc_W1o", "RD_tfc_Total"])
    csvwriter.writerows(modified_data)
    
print('trafficset_backup.csv file successfully created.')
