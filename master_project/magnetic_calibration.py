#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:47:08 2021

@author: amir
"""
import numpy as np
import math

def magcalib(magnetic_x,magnetic_y,magnetic_z,inclination_xaxis_avg,inclination_yaxis_avg,numdata,\
 magnetic_declination,inclinationdirection):
    absolute_magneticfield=np.zeros(numdata)
    for i in range(numdata):

        tilt_compensation=([(magnetic_x[i]*math.cos(math.radians(inclination_xaxis_avg[i])))-(magnetic_y[i]*math.sin(math.radians(inclination_yaxis_avg[i]))*math.sin(math.radians(inclination_xaxis_avg[i])))+(magnetic_z[i]*math.cos(math.radians(inclination_xaxis_avg[i]))*math.sin(math.radians(inclination_yaxis_avg[i])))],[(magnetic_y[i]*math.cos(math.radians(inclination_yaxis_avg[i])))-(magnetic_z[i]*math.sin(math.radians(inclination_yaxis_avg[i])))],[0])   

        tilt_compensation=np.array(tilt_compensation)
        absolute_magneticfield[i]=np.sqrt((tilt_compensation[0]**2)+(tilt_compensation[1]**2)+(magnetic_z[i]**2))         
        magnetic_declination[i]=180*math.atan2(((tilt_compensation[1])),(tilt_compensation[0]))/math.pi %360

    diff_magnetic=np.diff(magnetic_declination)
    for i in range (numdata-1):
        if diff_magnetic[i]>300:
            diff_magnetic[i]=diff_magnetic[i]-360
        if diff_magnetic[i]<-300:
            diff_magnetic[i]=360+diff_magnetic[i]  

    sum_mag_declination=np.zeros(numdata)
    
    for i in range (numdata):
        sum_mag_declination[i]=np.sum(diff_magnetic[0:i+1]) 
    
    return absolute_magneticfield,magnetic_declination,sum_mag_declination,diff_magnetic    
    absolute_magneticfield,magnetic_declination,sum_mag_declination,diff_magnetic