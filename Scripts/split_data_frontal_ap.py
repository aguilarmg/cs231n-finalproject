import csv


train_frontal_ap_labels = []

with open('../Data/csv_files/train_frontal_ap.csv', 'r') as f:
	train_frontal_ap_labels = list(csv.reader(f))

num_batches = 5 
size_of_batches = (len(train_frontal_ap_labels)-1) // 5

for idx in range(num_batches):
    with open('../Data/csv_files/train_frontal_ap_'+str(idx)+'.csv', 'w') as fp:
        writer = csv.writer(fp)
        writer.writerow(train_frontal_ap_labels[0])

#print(len(train_frontal_ap_labels))
train_frontal_ap_labels.pop(0)
#print(len(train_frontal_ap_labels))

for idx, patient in enumerate(train_frontal_ap_labels):
	if idx < size_of_batches:
		with open('../Data/csv_files/train_frontal_ap_0.csv', 'a') as fp_0:
			writer = csv.writer(fp_0)
			writer.writerow(patient)
	elif idx < size_of_batches*2:
		with open('../Data/csv_files/train_frontal_ap_1.csv', 'a') as fp_1:
			writer = csv.writer(fp_1)
			writer.writerow(patient)
	elif idx < size_of_batches*3:
		with open('../Data/csv_files/train_frontal_ap_2.csv', 'a') as fp_2:
			writer = csv.writer(fp_2)
			writer.writerow(patient)
	elif idx < size_of_batches*4:
		with open('../Data/csv_files/train_frontal_ap_3.csv', 'a') as fp_3:
			writer = csv.writer(fp_3)
			writer.writerow(patient)
	elif idx < size_of_batches*5:
		with open('../Data/csv_files/train_frontal_ap_4.csv', 'a') as fp_4:
			writer = csv.writer(fp_4)
			writer.writerow(patient)
