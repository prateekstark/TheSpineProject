import pandas as pd
import numpy as np
import random
import csv

damaged_data_size = 328
normal_data_size = 350

damaged_prefix = 'Training/Damaged/ID ('
damaged_im1 = []
damaged_im2 = []

for i in range(damaged_data_size):
	damaged_im1.append(damaged_prefix + str(i+1) + ")/AP/AP.jpg")
	damaged_im2.append(damaged_prefix + str(i+1) + ")/LAT/LAT.jpg")

normal_prefix = 'Training/Normal/ID ('
# ./Training/Damaged/ID\ \(1\)/AP/

normal_im1 = []
normal_im2 = []

for i in range(normal_data_size):
	normal_im1.append(normal_prefix + str(i+1) + ")/AP/AP.jpg")
	normal_im2.append(normal_prefix + str(i+1) + ")/LAT/LAT.jpg")

# 0 is damaged, 1 is normal

with open('data.csv', 'w', newline='') as file:
    fieldnames = ['im1', 'im2', 'label']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(damaged_data_size):
    	writer.writerow({'im1': damaged_im1[i], 'im2': damaged_im2[i], 'label': 0})

    for i in range(normal_data_size):
    	writer.writerow({'im1': normal_im1[i], 'im2': normal_im2[i], 'label': 1})