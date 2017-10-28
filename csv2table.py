import csv
import sqlite3

conn = sqlite3.connect('salarios')

c = conn.cursor()
c.execute('create table ago17 (id int primary key, nome text,remLiq real);')

with open('folhasPagamento/2017-08.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		values = str(row['id']) + ','
		values += "'" + row['nome'] + "'" + ','
		values += row['remLiq'] + ''
		c.execute('insert into ago17 values (' + values + ');')

conn.commit()
conn.close()
