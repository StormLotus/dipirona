import csv
import os

final = {}

for filename in os.listdir('csvs'):
	with open('csvs/'+filename) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			# for el in row:
			# 	print(row[el], end=',')
			# print(filename[:-4])
			if str(row['id'])+' '+row['nome'] in final:
				final[row['id']+' '+row['nome']].append((float(row['remBru'])-float(row['red']), filename[:-4], row['remLiq'])) 
			else:
				final[row['id']+' '+row['nome']] = [(float(row['remBru'])-float(row['red']), filename[:-4], row['remLiq'])]

for el in final:
	print(el + ':')
	final[el] = sorted(final[el], key=lambda x: x[1])
	for data in final[el]:
		print('\t'+str(data))