#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 20:50:12 2021

@author: amir
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:07:15 2021

@author: amir
"""

import math
import numpy as np
import pandas as pd
def arm(acc_sensor,xarm_calibrated,yarm_calibrated,zarm_calibrated,\
numdata,anglecaliball,degreecaliball,radiuscaliball,thetadict_calib,degree_calibdict,radius_calibdict,\
angle_calibrated,degree_calibrated,radius_calibrated,aa,lcont,larm,ljoint):
    calibration_angle=pd.read_excel(r'calibration.xlsx', engine='openpyxl')

    yy={}
    zz={}
    for i in range (8):
        i=i+1
        yy[str(i)+'1']=np.zeros(numdata)
        yy[str(i)+'2']=np.zeros(numdata)
        zz[str(i)+'1']=np.zeros(numdata)
        zz[str(i)+'2']=np.zeros(numdata)
    for k in range (8):    
        k=k+1
        for i in range (numdata):
            theta=np.array(calibration_angle['offset_along_y'][(k-1)*2])
            theta_2=np.array(calibration_angle['offset_along_y'][(k*2)-1])
            yy[str(k)+'1'][i]=acc_sensor['y_'+str(k)+'1'][i]
            yy[str(k)+'2'][i]=acc_sensor['y_'+str(k)+'2'][i]
            acc_sensor['y_'+str(k)+'1'][i]=((math.sin(math.radians(theta))*acc_sensor['x_'+str(k)+'1'][i])+(math.cos(math.radians(theta))*acc_sensor['y_'+str(k)+'1'][i]))
            acc_sensor['y_'+str(k)+'2'][i]=((math.sin(math.radians(theta_2))*acc_sensor['x_'+str(k)+'2'][i])+(math.cos(math.radians(theta_2))*acc_sensor['y_'+str(k)+'2'][i]))
            acc_sensor['x_'+str(k)+'1'][i]=((math.cos(math.radians(theta))*acc_sensor['x_'+str(k)+'1'][i])-(math.sin(math.radians(theta))*yy[str(k)+'1'][i]))
            acc_sensor['x_'+str(k)+'2'][i]=((math.cos(math.radians(theta_2))*acc_sensor['x_'+str(k)+'2'][i])-(math.sin(math.radians(theta_2))*yy[str(k)+'2'][i]))
      
            theta=np.array(calibration_angle['offset_along_x'][0])
            zz[str(k)+'1'][i]=acc_sensor['z_'+str(k)+'1'][i]
            zz[str(k)+'2'][i]=acc_sensor['z_'+str(k)+'2'][i]   
            acc_sensor['z_'+str(k)+'1'][i]=((math.sin(math.radians(theta))*acc_sensor['y_'+str(k)+'1'][i])+(math.cos(math.radians(theta))*acc_sensor['z_'+str(k)+'1'][i]))
            acc_sensor['z_'+str(k)+'2'][i]=((math.sin(math.radians(theta_2))*acc_sensor['y_'+str(k)+'2'][i])+(math.cos(math.radians(theta_2))*acc_sensor['z_'+str(k)+'2'][i]))

            acc_sensor['y_'+str(k)+'1'][i]=((math.cos(math.radians(theta))*acc_sensor['y_'+str(k)+'1'][i])-(math.sin(math.radians(theta))*zz[str(k)+'1'][i]))
            acc_sensor['y_'+str(k)+'2'][i]=((math.cos(math.radians(theta_2))*acc_sensor['y_'+str(k)+'2'][i])-(math.sin(math.radians(theta_2))*zz[str(k)+'1'][i]))            


    for j in range(8): 
        for i in range (numdata): 
            if j==0:
                k=1
            else:
                k=j+1
            if k<5:    
                angle_calibrated[j][i]=np.arccos(((acc_sensor['x_'+str(k)+'1'][i]*xarm_calibrated[str(k)+'3'][i])+(acc_sensor['y_'+str(k)+'1'][i]*yarm_calibrated[str(k)+'3'][i])+(acc_sensor['z_'+str(k)+'1'][i]*zarm_calibrated[str(k)+'3'][i]))/(math.sqrt((acc_sensor['x_'+str(k)+'1'][i]**2)+(acc_sensor['y_'+str(k)+'1'][i]**2)+(acc_sensor['z_'+str(k)+'1'][i]**2))*(math.sqrt((xarm_calibrated[str(k)+'3'][i]**2)+(yarm_calibrated[str(k)+'3'][i]**2)+(zarm_calibrated[str(k)+'3'][i]**2)))))        
                degree_calibrated[j][i]=eval('angle_calibrated[j][i]')*180/math.pi 
            else:    
                angle_calibrated[j][i]=np.arccos(((acc_sensor['x_'+str(k)+'1'][i]*xarm_calibrated[str(k)+'3'][i])+(-acc_sensor['y_'+str(k)+'1'][i]*yarm_calibrated[str(k)+'3'][i])+(acc_sensor['z_'+str(k)+'1'][i]*zarm_calibrated[str(k)+'3'][i]))/(math.sqrt((acc_sensor['x_'+str(k)+'1'][i]**2)+(acc_sensor['y_'+str(k)+'1'][i]**2)+(acc_sensor['z_'+str(k)+'1'][i]**2))*(math.sqrt((xarm_calibrated[str(k)+'3'][i]**2)+(yarm_calibrated[str(k)+'3'][i]**2)+(zarm_calibrated[str(k)+'3'][i]**2)))))        
                degree_calibrated[j][i]=(eval('angle_calibrated[j][i]')*180/math.pi )
    
    for j in range(16):
        for i in range (numdata): 
            if j<=7:
                pass
            else:
                    k=aa[j]
                    if k<5: 
                        k=k+1
                        angle_calibrated[j][i]=np.arccos(((-acc_sensor['x_'+str(k)+'1'][i]*xarm_calibrated[str(k)+'3'][i])+(acc_sensor['y_'+str(k)+'1'][i]*yarm_calibrated[str(k)+'3'][i])+(-acc_sensor['z_'+str(k)+'1'][i]*zarm_calibrated[str(k)+'3'][i]))/(math.sqrt((acc_sensor['x_'+str(k)+'1'][i]**2)+(acc_sensor['y_'+str(k)+'1'][i]**2)+(acc_sensor['z_'+str(k)+'1'][i]**2))*(math.sqrt((xarm_calibrated[str(k)+'3'][i]**2)+(yarm_calibrated[str(k)+'3'][i]**2)+(zarm_calibrated[str(k)+'3'][i]**2)))))        
                        degree_calibrated[j][i]=eval('angle_calibrated[j][i]')*180/math.pi 
                    else:    
                        angle_calibrated[j][i]=np.arccos(((-acc_sensor['x_'+str(k)+'1'][i]*xarm_calibrated[str(k)+'3'][i])+(-acc_sensor['y_'+str(k)+'1'][i]*yarm_calibrated[str(k)+'3'][i])+(-acc_sensor['z_'+str(k)+'1'][i]*zarm_calibrated[str(k)+'3'][i]))/(math.sqrt((acc_sensor['x_'+str(k)+'1'][i]**2)+(acc_sensor['y_'+str(k)+'1'][i]**2)+(acc_sensor['z_'+str(k)+'1'][i]**2))*(math.sqrt((xarm_calibrated[str(k)+'3'][i]**2)+(yarm_calibrated[str(k)+'3'][i]**2)+(zarm_calibrated[str(k)+'3'][i]**2)))))        
                        degree_calibrated[j][i]=(eval('angle_calibrated[j][i]')*180/math.pi )
    
  
                        
    for i in range(16):        
        globals()[anglecaliball[i]]=thetadict_calib.get(anglecaliball[i])  
        globals()[degreecaliball[i]]=degree_calibdict.get(degreecaliball[i])  
  
    for j in range(8): 
        for i in range (numdata): 
            if j==0:
                k=1
            else:
                k=j+1
            radius_calibrated[j][i]=ljoint+lcont+(larm*(math.sin(math.radians(eval('degree_calibrated[j][i]')))))
    
    
    for j in range(16):
        for i in range (numdata): 
            if j<=7:
                pass
            else:
                    k=aa[j]
                    radius_calibrated[j][i]=ljoint+lcont+(larm*(math.sin(math.radians(eval('degree_calibrated[j][i]')))))
               
    
    for i in range(16):        
        globals()[radiuscaliball[i]]=radius_calibdict.get(radiuscaliball[i])  
    
    
    for j in range(8): 
        for i in range (numdata): 
            if j==0:
                k=1
            else:
                k=j+1
            radius_calibrated[j][i]=ljoint+lcont+(larm*(math.sin(math.radians(eval('degree_calibrated[j][i]')))))
            radius_calibrated[j][i]=radius_calibrated[j][i] #mm
    
    for j in range(16):
        for i in range (numdata): 
            if j<=7:
                pass
            else:
                    k=aa[j]
                    radius_calibrated[j][i]=ljoint+lcont+(larm*(math.sin(math.radians(eval('degree_calibrated[j][i]')))))         
                    radius_calibrated[j][i]=radius_calibrated[j][i] #mm
           
    return acc_sensor,radius_calibdict,degree_calibdict