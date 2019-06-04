import csv

train_labels = []

with open('../Data/csv_files/train.csv', 'r') as f:
	train_labels = list(csv.reader(f))

with open('../Data/csv_files/train_lateral.csv', 'w') as lateralTrainFile:
	writer = csv.writer(lateralTrainFile)
	writer.writerow(train_labels[0])

lateralTrainFile.close()

with open('../Data/csv_files/train_frontal_ap.csv', 'w') as frontalapTrainFile:
	writer = csv.writer(frontalapTrainFile)
	writer.writerow(train_labels[0])

frontalapTrainFile.close()

with open('../Data/csv_files/train_frontal_pa.csv', 'w') as frontalpaTrainFile:
	writer = csv.writer(frontalpaTrainFile)
	writer.writerow(train_labels[0])

frontalpaTrainFile.close()

for idx, patient in enumerate(train_labels):
	if idx > 0:
		if patient[3] == 'Lateral':
			with open('../Data/csv_files/train_lateral.csv', 'a') as lateralTrainFile:
				writer = csv.writer(lateralTrainFile)
				writer.writerow(patient)
		elif patient[3] == 'Frontal':
			if patient[4] == 'AP':
				with open('../Data/csv_files/train_frontal_ap.csv', 'a') as frontalapTrainFile:
					writer = csv.writer(frontalapTrainFile)
					writer.writerow(patient)
			else:
				with open('../Data/csv_files/train_frontal_pa.csv', 'a') as frontalpaTrainFile:
					writer = csv.writer(frontalpaTrainFile)
					writer.writerow(patient)

valid_labels = []
with open('../Data/csv_files/valid.csv', 'r') as f:
	valid_labels = list(csv.reader(f))

with open('../Data/csv_files/valid_lateral.csv', 'w') as lateralValidFile:
	writer = csv.writer(lateralValidFile)
	writer.writerow(valid_labels[0])
lateralValidFile.close()

with open('../Data/csv_files/valid_frontal_ap.csv', 'w') as frontalapValidFile:
	writer = csv.writer(frontalapValidFile)
	writer.writerow(valid_labels[0])
frontalapValidFile.close()

with open('../Data/csv_files/valid_frontal_pa.csv', 'w') as frontalpaValidFile:
	writer = csv.writer(frontalpaValidFile)
	writer.writerow(valid_labels[0])
frontalpaValidFile.close()

for idx, patient in enumerate(valid_labels):
	if idx > 0:
		if patient[3] == 'Lateral':
			with open('../Data/csv_files/valid_lateral.csv', 'a') as lateralValidFile:
				writer = csv.writer(lateralValidFile)
				writer.writerow(patient)
		elif patient[3] == 'Frontal':
			if patient[4] == 'AP':
				with open('../Data/csv_files/valid_frontal_ap.csv', 'a') as frontalapValidFile:
					writer = csv.writer(frontalapValidFile)
					writer.writerow(patient)
			else:
				with open('../Data/csv_files/valid_frontal_pa.csv', 'a') as frontalpaValidFile:
					writer = csv.writer(frontalpaValidFile)
					writer.writerow(patient)

