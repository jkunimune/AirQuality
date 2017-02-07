import csv
import os

filename = 'pm10_2016'

with open('_big_'+filename+'.csv', newline='') as f1:
	reader = csv.reader(f1, delimiter=',', quotechar='"')
	hit_data = False
	rows = []

	for row in reader:
		if len(rows) == 0:
			rows.append(row)
		elif row[0] == '15' and row[1] == '003' and row[2] == '0010':
			hit_data = True
			rows.append(row)
		elif hit_data:
			break

	with open(filename+'.csv', 'w', newline='') as f2:
		writer = csv.writer(f2)
		writer.writerows(rows)

os.remove('_big_'+filename+'.csv')