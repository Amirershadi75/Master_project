#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 21:13:36 2021

@author: amir
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 23:50:34 2021

@author: amir
"""
import numpy as np
import math
from numpy import linalg as LA
import pandas as pd
def inclination(numdata,inclinationdirection,incline,\
                magnetic_declination,acc_sensor,\
                magnetic_x,magnetic_y,magnetic_z):
    g=1
    total_rotation=np.zeros(numdata)
    for i in range (numdata):
        inclinationdirection[i]=math.atan2(((-acc_sensor['z_43'][i])),(acc_sensor['x_43'][i]))
        if math.isnan(inclinationdirection[i])==True:
            inclinationdirection[i]=inclinationdirection[i-1]
    inclinationdirection=(inclinationdirection*180)/math.pi %360

    for i in range(numdata):
        magnetic_declination[i]=math.atan2(magnetic_y[i],magnetic_x[i]) 
    magnetic_declination=(magnetic_declination*180)/(math.pi) %360
    diff_magnetic=np.diff(-1*(magnetic_declination))
    
    for i in range (numdata-1):
        if diff_magnetic[i]>300:
            diff_magnetic[i]=diff_magnetic[i]-360
        if diff_magnetic[i]<-300:
            diff_magnetic[i]=360+diff_magnetic[i]  

    
    for i in range (len(diff_magnetic)):
        total_rotation[i]=diff_magnetic[i]

            
    diff_rotation=np.diff(total_rotation)       
    for i in range (len(diff_rotation)): 
        if diff_rotation[i]>300:
            diff_rotation[i]=360-diff_rotation[i]
        if diff_rotation[i]<-300:
            diff_rotation[i]=360+diff_rotation[i]    
        if -90<diff_rotation[i]<=-30:
            diff_rotation[i]=-90-diff_rotation[i]  
        if np.abs(diff_rotation[i])>40: 
            diff_rotation[i]=diff_rotation[i-1]
    
    sum_mag_declination=np.zeros(numdata)
    
    
    for i in range (numdata-1):
        sum_mag_declination[i]=np.sum(diff_magnetic[0:i+1])

    return  sum_mag_declination,inclinationdirection