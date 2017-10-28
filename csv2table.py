import csv
import sqlite3

conn = sqlite3.connect('salarios')
c = conn.cursor()
c.execute('create table salarios (nome text,remBru real,ind real,red real,desc real,remLiq real);')
with open('tabela_salarios.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		values = "'" + row['nome'] + "'" + ','
		values += row['remBru'] + ','
		values += row['ind'] + ','
		values += row['red'] + ','
		values += row['desc'] + ','
		values += row['remLiq']
		c.execute('insert into salarios values (' + values + ');')

conn.commit()
conn.close()
