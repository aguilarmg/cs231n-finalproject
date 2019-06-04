import numpy as np
import csv
from imageio import imread
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle

def testing(csv_file):
    with open('Data/csv_files/'+csv_file, 'r') as f:
        train_labels = list(csv.reader(f))
     
    print(len(train_labels))
    #print(train_labels[0])
    #print(train_labels[1])

def grab_data(csv_file):
    with open('Data/csv_files/'+csv_file, 'r') as f:
        train_labels = list(csv.reader(f))
 

    labels = []
    X = []
    y = []

    labels = train_labels[0]
    
    for i, line in enumerate(train_labels[1:]):
        img = imread('Data/source_data/'+line[0])
        X.append(crop_center(img, 320, 320))       
        y.append(line[1:])

        if i % 2000 == 0:
            print(i)
        
    return (labels, X, y)

# Found image cropping code from StackOverflow to crop the center of our chest scans: 
# https://stackoverflow.com/questions/39382412/crop-center-portion-of-a-numpy-image/39382475 
def crop_center(img,cropx,cropy):
    y,x = img.shape
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)    
    return img[starty:starty+cropy,startx:startx+cropx]

def grab_processed_data(csv_file, pickle_file):
   
    X = []
    y = []
    labels = []
    
    with open('Data/csv_files/'+ csv_file, 'r') as f:
        csv_labels = list(csv.reader(f))
  
    temp = []
    temp.append(csv_labels[0][13])
    temp.append(csv_labels[0][7])
    temp.append(csv_labels[0][11])
    temp.append(csv_labels[0][10])
    temp.append(csv_labels[0][15])
    labels = temp
    
    for i, line in enumerate(csv_labels[1:]):    
        temp = []
        temp.append(line[13])
        temp.append(line[7])
        temp.append(line[11])
        temp.append(line[10])
        temp.append(line[15])
        y.append(temp)
    
    with open('Data/pkl_files/' + pickle_file, "rb") as fp:
        X = pickle.load(fp)
    
    #for idx,img in enumerate(X):
        #img = np.asarray(np.reshape(img, (1,320,320)))
        #X[idx] = img
    
    y = process_outputs(y)
    num_images = len(X)
    
    return (labels, np.reshape(np.asarray(X), (num_images, 1, 320, 320)).astype(np.uint8), np.asarray(y))

def process_outputs(y):
    for j, line in enumerate(y):
        for i, element in enumerate(line):
            if element == '':
                line[i] = 0.0
            elif element == '-1.0':
                if i == 5 or i == 8:
                    line[i] = 1.0
                elif i == 2 or i == 6 or i == 10:
                    line[i] = 0.0
                else:
                    line[i] = 0.0
            else:
                line[i] = float(element)
    
    return y