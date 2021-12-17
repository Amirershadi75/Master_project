#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:30:59 2021

@author: amir
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:24:44 2021

@author: amir
"""
import numpy as np
import math
import pandas as pd
def gyroscope(numdata,data,NaN,encoder_finder,encoder_diff):
    #Define Gyroscope variables
    gyro_x=np.zeros(numdata)
    gyro_y=np.zeros(numdata)
    gyro_z=np.zeros(numdata)    
    gyro_rotation_uncalibrated=np.zeros(numdata)
    gyro_rotation_calibrated=np.zeros(numdata)
    gyro_rotation_xuncalibrated=np.zeros(numdata)
    gyro_rotation_xcalibrated=np.zeros(numdata)
    gyro_rotation_yuncalibrated=np.zeros(numdata)
    gyro_rotation_ycalibrated=np.zeros(numdata)    
    for j in range(3): 
        for i in range (numdata): 
            gyro_x[i]=(((float(data[46+(i*585)]))/(32*((2**16)/4000)))*0.5)
            gyro_y[i]=(((float(data[53+(i*585)]))/(32*((2**16)/4000)))*0.5)
            gyro_z[i]=-(((float(data[60+(i*585)]))/(32*((2**16)/4000)))*0.5)
            if math.isnan(gyro_x[i])==True:
                gyro_x[i]=gyro_x[i-1]
            if math.isnan(gyro_y[i])==True:
                gyro_y[i]=gyro_y[i-1]
            if math.isnan(gyro_z[i])==True:
                gyro_z[i]=gyro_z[i-1]

    calibration_gyro=pd.read_excel(r'calibration.xlsx', engine='openpyxl')
    gyro_xuncalibrated=gyro_x
    gyro_yuncalibrated=gyro_y
    gyro_zuncalibrated=gyro_z
    gyro_zcalibrated=gyro_z+np.array(calibration_gyro['gyro_z_offset'][0])
    gyro_xcalibrated=gyro_x+np.array(calibration_gyro['gyro_x_offset'][0])
    gyro_ycalibrated=gyro_y+np.array(calibration_gyro['gyro_y_offset'][0])
    
    #Rotation based on Gyroscope
    for i in range (numdata):
        gyro_rotation_uncalibrated[i]=np.sum(gyro_zuncalibrated[0:i])
        gyro_rotation_calibrated[i]=np.sum(gyro_zcalibrated[0:i]) 
        gyro_rotation_xuncalibrated[i]=np.sum(gyro_xuncalibrated[0:i])
        gyro_rotation_xcalibrated[i]=np.sum(gyro_xcalibrated[0:i]) 
        gyro_rotation_yuncalibrated[i]=np.sum(gyro_yuncalibrated[0:i])
        gyro_rotation_ycalibrated[i]=np.sum(gyro_ycalibrated[0:i]) 

        
    return gyro_x,gyro_y,gyro_z,gyro_xuncalibrated,gyro_yuncalibrated,gyro_zuncalibrated,\
    gyro_xcalibrated,gyro_ycalibrated,gyro_zcalibrated,gyro_rotation_uncalibrated,gyro_rotation_calibrated,\
    gyro_rotation_xuncalibrated,gyro_rotation_xcalibrated,gyro_rotation_yuncalibrated,gyro_rotation_ycalibrated
            
            