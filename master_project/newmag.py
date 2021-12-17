#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:16:51 2021

@author: amir
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:16:39 2021

@author: amir
"""
import math
import numpy as np
import pandas as pd
def magnetometer_sensor(numdata,data,NaN,encoder_finder,encoder_diff):
    #Define magnetometer sensor
    magneticfield_x_uncalibrated=np.zeros(numdata)
    magneticfield_y_uncalibrated=np.zeros(numdata)
    magneticfield_z_uncalibrated=np.zeros(numdata)
    magnetic_x=np.zeros(numdata)
    magnetic_y=np.zeros(numdata)
    magnetic_z=np.zeros(numdata)
    for j in range(4): 
        for i in range (numdata): 
            if j==0:
                k=1
            else:
                k=j+1
            calibration_mag=pd.read_excel(r'calibration.xlsx', engine='openpyxl')
            magneticfield_x_uncalibrated[i]=((float(data[18+(i*585)]))/(2**13/(2*2600)))
            magneticfield_y_uncalibrated[i]=((float(data[25+(i*585)]))/(2**13/(2*2600)))     
            magneticfield_z_uncalibrated[i]=((float(data[32+(i*585)]))/(2**15/(2*5000)))
            magnetic_x[i]=((float(data[18+(i*585)]))/(2**13/(2*2600)))+np.array(calibration_mag['magnetic_x_offset'][0])
            magnetic_y[i]=((float(data[25+(i*585)]))/(2**13/(2*2600)))+np.array(calibration_mag['magnetic_y_offset'][0])
            magnetic_z[i]=((float(data[32+(i*585)]))/(2**15/(2*5000)))
            
            if math.isnan(magnetic_x[i])==True:
                magnetic_x[i]=magnetic_x[i-1]
            if math.isnan(magnetic_y[i])==True:
                magnetic_y[i]=magnetic_y[i-1]
            if math.isnan(magnetic_z[i])==True:
                magnetic_z[i]=magnetic_z[i-1]
    #Uncalibrated magnetic field            
    absolute_uncalibrated_magneticfield=np.zeros(numdata)            
    for i in range(numdata):
         absolute_uncalibrated_magneticfield[i]=np.sqrt((magneticfield_x_uncalibrated[i]**2)+(magneticfield_y_uncalibrated[i]**2)+(magneticfield_z_uncalibrated[i]**2))                     
     
    return magnetic_x,magnetic_y,magnetic_z,magneticfield_x_uncalibrated,\
        magneticfield_y_uncalibrated,magneticfield_z_uncalibrated,absolute_uncalibrated_magneticfield