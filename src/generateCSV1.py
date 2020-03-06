import pandas as pd
import numpy as np
import random
import csv

damaged_data_size = 328
normal_data_size = 350

damaged_prefix = 'Training/Damaged/ID ('
damaged_im1 = []
damaged_im2 = []
d_seg_im1 = []
d_seg_im2 = []
d_seg_im3 = []
d_seg_im4 = []
d_seg_im5 = []
d_seg_im6 = []
d_seg_im7 = []
d_seg_im8 = []

for i in range(damaged_data_size):
    d_seg_im1.append(damaged_prefix + str(i+1) + ")/AP/Ap_Pedicle.png")
    d_seg_im2.append(damaged_prefix + str(i+1) + ")/AP/Ap_Spinous_Process.png")
    d_seg_im3.append(damaged_prefix + str(i+1) + ")/AP/Ap_Vertebra.png")
    d_seg_im4.append(damaged_prefix + str(i+1) + ")/LAT/Lat_Anterior_Vertebral_Line.png")
    d_seg_im5.append(damaged_prefix + str(i+1) + ")/LAT/Lat_Disk_Height.png")
    d_seg_im6.append(damaged_prefix + str(i+1) + ")/LAT/Lat_Posterior_Vertebral_Line.png")
    d_seg_im7.append(damaged_prefix + str(i+1) + ")/LAT/Lat_Spinous_Process.png")
    d_seg_im8.append(damaged_prefix + str(i+1) + ")/LAT/Lat_Vertebra.png")
    damaged_im1.append(damaged_prefix + str(i+1) + ")/AP/AP.jpg")
    damaged_im2.append(damaged_prefix + str(i+1) + ")/LAT/LAT.jpg")

normal_prefix = 'Training/Normal/ID ('
# ./Training/Damaged/ID\ \(1\)/AP/

normal_im1 = []
normal_im2 = []
n_seg_im1 = []
n_seg_im2 = []
n_seg_im3 = []
n_seg_im4 = []
n_seg_im5 = []
n_seg_im6 = []
n_seg_im7 = []
n_seg_im8 = []

for i in range(normal_data_size):
    n_seg_im1.append(normal_prefix + str(i+1) + ")/AP/Ap_Pedicle.png")
    n_seg_im2.append(normal_prefix + str(i+1) + ")/AP/Ap_Spinous_Process.png")
    n_seg_im3.append(normal_prefix + str(i+1) + ")/AP/Ap_Vertebra.png")
    n_seg_im4.append(normal_prefix + str(i+1) + ")/LAT/Lat_Anterior_Vertebral_Line.png")
    n_seg_im5.append(normal_prefix + str(i+1) + ")/LAT/Lat_Disk_Height.png")
    n_seg_im6.append(normal_prefix + str(i+1) + ")/LAT/Lat_Posterior_Vertebral_Line.png")
    n_seg_im7.append(normal_prefix + str(i+1) + ")/LAT/Lat_Spinous_Process.png")
    n_seg_im8.append(normal_prefix + str(i+1) + ")/LAT/Lat_Vertebra.png")
    normal_im1.append(normal_prefix + str(i+1) + ")/AP/AP.jpg")
    normal_im2.append(normal_prefix + str(i+1) + ")/LAT/LAT.jpg")


# 0 is damaged, 1 is normal

with open('data1.csv', 'w', newline='') as file:
    fieldnames = ['im1', 'im2', 'seg1', 'seg2', 'seg3', 'seg4', 'seg5', 'seg6', 'seg7', 'seg8', 'label']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(damaged_data_size):
    	writer.writerow({'im1': damaged_im1[i], 'im2': damaged_im2[i], 'seg1': d_seg_im1[i], 'seg2': d_seg_im2[i], 'seg3': d_seg_im3[i], 'seg4': d_seg_im4[i], 'seg5': d_seg_im5[i], 'seg6': d_seg_im6[i], 'seg7': d_seg_im7[i], 'seg8': d_seg_im8[i], 'label': 0})

    for i in range(normal_data_size):
        writer.writerow({'im1': normal_im1[i], 'im2': normal_im2[i], 'seg1': n_seg_im1[i], 'seg2': n_seg_im2[i], 'seg3': n_seg_im3[i], 'seg4': n_seg_im4[i], 'seg5': n_seg_im5[i], 'seg6': n_seg_im6[i], 'seg7': n_seg_im7[i], 'seg8': n_seg_im8[i], 'label': 1})
    	# writer.writerow({'im1': normal_im1[i], 'im2': normal_im2[i], 'label': 1})

exit()