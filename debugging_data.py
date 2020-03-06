import os
import pandas as pd

data = pd.read_csv('data1.csv')

for i in range(data.shape[0]):
    fp1 = data['im1'][i]
    fp2 = data['im2'][i]
    seg_fp1 = data['seg1'][i]
    seg_fp2 = data['seg2'][i]
    seg_fp3 = data['seg3'][i]
    seg_fp4 = data['seg4'][i]
    seg_fp5 = data['seg5'][i]
    seg_fp6 = data['seg6'][i]
    seg_fp7 = data['seg7'][i]
    seg_fp8 = data['seg8'][i]
    if(not os.path.exists(fp1)):
    	print(fp1)
    
    if(not os.path.exists(fp2)):
    	print(fp2)
    
    if(not os.path.exists(seg_fp1)):
    	print(seg_fp1)
    
    if(not os.path.exists(seg_fp2)):
    	print(seg_fp2)
    
    if(not os.path.exists(seg_fp3)):
    	print(seg_fp3)
    
    if(not os.path.exists(seg_fp4)):
    	print(seg_fp4)

    if(not os.path.exists(seg_fp5)):
    	print(seg_fp5)
    
    if(not os.path.exists(seg_fp6)):
    	print(seg_fp6)

    if(not os.path.exists(seg_fp7)):
    	print(seg_fp7)
    
    if(not os.path.exists(seg_fp8)):
    	print(seg_fp8)

exit()