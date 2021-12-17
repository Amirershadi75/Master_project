#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 10:58:39 2021

@author: amir
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 16:21:05 2021

@author: amir
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def calib(numdata,acc_sensor,sum_mag_declination,\
inclination_x,inclination_y):
    import pandas as pd
    calibration_angle=pd.read_excel(r'calibration.xlsx', engine='openpyxl')
    xcalibrated={}
    ycalibrated={}
    zcalibrated={}
    xx_calibrated={}
    yy_calibrated={}
    zz_calibrated={}    
    xarm_calibrated={}
    yarm_calibrated={}
    zarm_calibrated={}
    for i in range (8):
        i=i+1
        xcalibrated[str(i)+'3']=np.zeros(numdata)
        ycalibrated[str(i)+'3']=np.zeros(numdata)
        zcalibrated[str(i)+'3']=np.zeros(numdata)
        xarm_calibrated[str(i)+'3']=np.zeros(numdata)
        yarm_calibrated[str(i)+'3']=np.zeros(numdata)
        zarm_calibrated[str(i)+'3']=np.zeros(numdata)
        xx_calibrated[str(i)+'3']=np.zeros(numdata)
        yy_calibrated[str(i)+'3']=np.zeros(numdata)
        zz_calibrated[str(i)+'3']=np.zeros(numdata)
        
 
    #13
    for k in range (4):
        k=k+1
        
        for i in range (numdata-1):
            
            ycalibrated[str(k)+'3'][i]=acc_sensor['y_'+str(k)+'3'][i]
            theta=np.array(calibration_angle['theta_y'][k-1])
            ycalibrated[str(k)+'3'][i]=((math.sin(math.radians(theta))*acc_sensor['x_'+str(k)+'3'][i])+(math.cos(math.radians(theta))*acc_sensor['y_'+str(k)+'3'][i]))
            xcalibrated[str(k)+'3'][i]=((math.cos(math.radians(theta))*acc_sensor['x_'+str(k)+'3'][i])-(math.sin(math.radians(theta))*acc_sensor['y_'+str(k)+'3'][i]))          
            yy_calibrated[str(k)+'3'][i]=ycalibrated[str(k)+'3'][i]
            zz_calibrated[str(k)+'3'][i]=acc_sensor['z_'+str(k)+'3'][i]
            theta=np.array(calibration_angle['theta_x'][k-1])
            zcalibrated[str(k)+'3'][i]=((math.sin(math.radians(theta))*yy_calibrated[str(k)+'3'][i])+(math.cos(math.radians(theta))*zz_calibrated[str(k)+'3'][i]))
            ycalibrated[str(k)+'3'][i]=((math.cos(math.radians(theta))*yy_calibrated[str(k)+'3'][i])-(math.sin(math.radians(theta))*zz_calibrated[str(k)+'3'][i]))
            xx_calibrated[str(k)+'3'][i]=xcalibrated[str(k)+'3'][i]
            xarm_calibrated[str(k)+'3'][i]=xcalibrated[str(k)+'3'][i]
            yarm_calibrated[str(k)+'3'][i]=ycalibrated[str(k)+'3'][i]
            zarm_calibrated[str(k)+'3'][i]=zcalibrated[str(k)+'3'][i]
            theta=np.array(calibration_angle['theta_z'][k-1])-sum_mag_declination[i]
            xcalibrated[str(k)+'3'][i]=((math.cos(math.radians(theta))*xcalibrated[str(k)+'3'][i])+(math.sin(math.radians(theta))*zcalibrated[str(k)+'3'][i]))
            zcalibrated[str(k)+'3'][i]=((-math.sin(math.radians(theta))*xx_calibrated[str(k)+'3'][i])+(math.cos(math.radians(theta))*zcalibrated[str(k)+'3'][i]))

    for k in range (8):
        k=k+1
        if k<5:
            pass
        else:
        
            for i in range (numdata-1):

                ycalibrated[str(k)+'3'][i]=-acc_sensor['y_'+str(k)+'3'][i]
                acc_sensor['y_'+str(k)+'3'][i]=-acc_sensor['y_'+str(k)+'3'][i]
                theta=np.array(calibration_angle['theta_y'][k-1])
                ycalibrated[str(k)+'3'][i]=((math.sin(math.radians(theta))*acc_sensor['x_'+str(k)+'3'][i])+(math.cos(math.radians(theta))*ycalibrated[str(k)+'3'][i]))
                xcalibrated[str(k)+'3'][i]=((math.cos(math.radians(theta))*acc_sensor['x_'+str(k)+'3'][i])-(math.sin(math.radians(theta))*acc_sensor['y_'+str(k)+'3'][i]))          
                yy_calibrated[str(k)+'3'][i]=ycalibrated[str(k)+'3'][i]
                zz_calibrated[str(k)+'3'][i]=acc_sensor['z_'+str(k)+'3'][i]
                theta=-np.array(calibration_angle['theta_x'][k-1])
                zcalibrated[str(k)+'3'][i]=((math.sin(math.radians(theta))*yy_calibrated[str(k)+'3'][i])+(math.cos(math.radians(theta))*zz_calibrated[str(k)+'3'][i]))
                ycalibrated[str(k)+'3'][i]=((math.cos(math.radians(theta))*yy_calibrated[str(k)+'3'][i])-(math.sin(math.radians(theta))*zz_calibrated[str(k)+'3'][i]))
                xx_calibrated[str(k)+'3'][i]=xcalibrated[str(k)+'3'][i]
                xarm_calibrated[str(k)+'3'][i]=xcalibrated[str(k)+'3'][i]
                yarm_calibrated[str(k)+'3'][i]=ycalibrated[str(k)+'3'][i]
                zarm_calibrated[str(k)+'3'][i]=zcalibrated[str(k)+'3'][i]
                theta=np.array(calibration_angle['theta_z'][k-1])+sum_mag_declination[i]
                xcalibrated[str(k)+'3'][i]=((math.cos(math.radians(theta))*xcalibrated[str(k)+'3'][i])+(math.sin(math.radians(theta))*zcalibrated[str(k)+'3'][i]))
                zcalibrated[str(k)+'3'][i]=((-math.sin(math.radians(theta))*xx_calibrated[str(k)+'3'][i])+(math.cos(math.radians(theta))*zcalibrated[str(k)+'3'][i]))
    for k in range (4):
        k=k+1
        for i in range (numdata-1):
            inclination_x['inclination_xaxis_'+str(k)+'3'][i]=180 * math.atan2 (-zcalibrated[str(k)+'3'][i],np.sqrt(xcalibrated[str(k)+'3'][i]*xcalibrated[str(k)+'3'][i] + ycalibrated[str(k)+'3'][i]*ycalibrated[str(k)+'3'][i]))/math.pi;
            inclination_y['inclination_yaxis_'+str(k)+'3'][i]=180 * math.atan2 (xcalibrated[str(k)+'3'][i],np.sqrt(zcalibrated[str(k)+'3'][i]*zcalibrated[str(k)+'3'][i] + ycalibrated[str(k)+'3'][i]*ycalibrated[str(k)+'3'][i]))/math.pi;  
    for k in range (8):
        k=k+1
        if k<5:
            pass
        else:
        
            for i in range (numdata-1): 
                inclination_x['inclination_xaxis_'+str(k)+'3'][i]=180 * math.atan2 (zcalibrated[str(k)+'3'][i],np.sqrt(xcalibrated[str(k)+'3'][i]*xcalibrated[str(k)+'3'][i] + ycalibrated[str(k)+'3'][i]*ycalibrated[str(k)+'3'][i]))/math.pi;
                inclination_y['inclination_yaxis_'+str(k)+'3'][i]=180 * math.atan2 (xcalibrated[str(k)+'3'][i],np.sqrt(zcalibrated[str(k)+'3'][i]*zcalibrated[str(k)+'3'][i] + ycalibrated[str(k)+'3'][i]*ycalibrated[str(k)+'3'][i]))/math.pi;  
        
    xarm_calibrated[str(k)+'3'][numdata-1]=xarm_calibrated[str(k)+'3'][numdata-2]
    yarm_calibrated[str(k)+'3'][numdata-1]=yarm_calibrated[str(k)+'3'][numdata-2]
    zarm_calibrated[str(k)+'3'][numdata-1]=zarm_calibrated[str(k)+'3'][numdata-2]
    
    
    for k in range (8):
        k=k+1
        for i in range (numdata-1):
            if math.isnan(inclination_x['inclination_xaxis_'+str(k)+'3'][i])==True:
                inclination_x['inclination_xaxis_'+str(k)+'3'][i]=inclination_x['inclination_xaxis_'+str(k)+'3'][i-1]
            if math.isnan(inclination_y['inclination_yaxis_'+str(k)+'3'][i])==True:    
                inclination_y['inclination_yaxis_'+str(k)+'3'][i]=inclination_y['inclination_yaxis_'+str(k)+'3'][i-1]
                
                
        
    inclinationdirection=np.zeros(numdata)
    incline=np.zeros(numdata)
    x3_avg=np.zeros(numdata)
    y3_avg=np.zeros(numdata)
    z3_avg=np.zeros(numdata)
         
    for i in range (numdata):
            x3_avg[i]=np.mean([np.mean( (xcalibrated['13'][i])),np.mean( (xcalibrated['23'][i])),np.mean( (xcalibrated['33'][i])),np.mean( (xcalibrated['53'][i])),np.mean( (xcalibrated['63'][i])),np.mean( (xcalibrated['73'][i]))])
            y3_avg[i]=np.mean([np.mean( (ycalibrated['13'][i])),np.mean( (ycalibrated['23'][i])),np.mean( (ycalibrated['33'][i])),np.mean( (ycalibrated['53'][i])),np.mean( (ycalibrated['63'][i])),np.mean( (ycalibrated['73'][i]))])
            z3_avg[i]=np.mean([np.mean( (-zcalibrated['13'][i])),np.mean( (-zcalibrated['23'][i])),np.mean( (-zcalibrated['33'][i])),np.mean( (zcalibrated['53'][i])),np.mean( (zcalibrated['63'][i])),np.mean( (zcalibrated['73'][i]))])
            inclinationdirection[i]=math.atan2((-z3_avg[i]),x3_avg[i])
            if math.isnan(inclinationdirection[i])==True:
                inclinationdirection[i]=inclinationdirection[i-1]
            incline[i]=np.arccos(((y3_avg[i]))/(math.sqrt((y3_avg[i]**2)+(x3_avg[i]**2)+(z3_avg[i]**2))))
    inclinationdirection=(inclinationdirection*180)/math.pi %360
    incline=180-((incline*180)/math.pi )  
    inclination_xaxis_avg=np.zeros(numdata)
    inclination_yaxis_avg=np.zeros(numdata)

    for i in range (numdata-1):
            inclination_xaxis_avg[i]=np.mean([np.mean( (inclination_x['inclination_xaxis_13'][i])),np.mean( (inclination_x['inclination_xaxis_23'][i])),np.mean( (inclination_x['inclination_xaxis_33'][i])),np.mean( (inclination_x['inclination_xaxis_53'][i])),np.mean( (inclination_x['inclination_xaxis_63'][i])),np.mean( (inclination_x['inclination_xaxis_73'][i]))])
            inclination_yaxis_avg[i]=np.mean([np.mean( (inclination_y['inclination_yaxis_13'][i])),np.mean( (inclination_y['inclination_yaxis_23'][i])),np.mean( (inclination_y['inclination_yaxis_33'][i])),np.mean( (inclination_y['inclination_yaxis_53'][i])),np.mean( (inclination_y['inclination_yaxis_63'][i])),np.mean( (inclination_y['inclination_yaxis_73'][i]))])
    for i in range (numdata):    
        if math.isnan(incline[i])==True:
            incline[i]=incline[i-1]      
    return inclination_x,inclination_y,xarm_calibrated,yarm_calibrated,zarm_calibrated,\
        xcalibrated,ycalibrated,zcalibrated,xx_calibrated,yy_calibrated,zz_calibrated,\
        inclinationdirection,incline,x3_avg,y3_avg,z3_avg,inclination_xaxis_avg,inclination_yaxis_avg