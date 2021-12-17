#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 20:31:32 2021

@author: amir
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 20:18:23 2021

@author: amir
"""
import numpy as np
import math
def ang_rad(numdata, angle, degree, aa, thetadict,\
angleall, degreedict, degreeall, ljoint, larm, lcont, radius,\
radiusdict, radiusall,acc_sensor):
    for j in range(8): 
        for i in range (numdata): 
            if j==0:
                k=1
            else:
                k=j+1
            if k<5:    
                angle[j][i]=np.arccos((((acc_sensor['x_'+str(k)+'1'])[i]*(acc_sensor['x_'+str(k)+'3'])[i])+((acc_sensor['y_'+str(k)+'1'])[i]*(acc_sensor['y_'+str(k)+'3'])[i])+((acc_sensor['z_'+str(k)+'1'])[i]*(acc_sensor['z_'+str(k)+'3'])[i]))/(math.sqrt(((acc_sensor['x_'+str(k)+'1'])[i]**2)+((acc_sensor['y_'+str(k)+'1'])[i]**2)+((acc_sensor['z_'+str(k)+'1'])[i]**2))*(math.sqrt(((acc_sensor['x_'+str(k)+'3'])[i]**2)+((acc_sensor['y_'+str(k)+'3'])[i]**2)+((acc_sensor['z_'+str(k)+'3'])[i]**2)))))        
                degree[j][i]=eval('angle[j][i]')*180/math.pi 
            else:    
                angle[j][i]=np.arccos((((acc_sensor['x_'+str(k)+'1'])[i]*(acc_sensor['x_'+str(k)+'3'])[i])+((acc_sensor['y_'+str(k)+'1'])[i]*(acc_sensor['y_'+str(k)+'3'])[i])+((acc_sensor['z_'+str(k)+'1'])[i]*(acc_sensor['z_'+str(k)+'3'])[i]))/(math.sqrt(((acc_sensor['x_'+str(k)+'1'])[i]**2)+((acc_sensor['y_'+str(k)+'1'])[i]**2)+((acc_sensor['z_'+str(k)+'1'])[i]**2))*(math.sqrt(((acc_sensor['x_'+str(k)+'3'])[i]**2)+((acc_sensor['y_'+str(k)+'3'])[i]**2)+((acc_sensor['z_'+str(k)+'3'])[i]**2)))))        
                degree[j][i]=eval('angle[j][i]')*180/math.pi 
    
    for j in range(16):
        for i in range (numdata): 
            if j<=7:
                pass
            else:
                    k=aa[j]
                    if k<5: 
                        k=k+1
                        angle[j][i]=np.arccos((((-acc_sensor['x_'+str(k)+'2'])[i]*(acc_sensor['x_'+str(k)+'3'])[i])+((acc_sensor['y_'+str(k)+'2'])[i]*(acc_sensor['y_'+str(k)+'3'])[i])+((-acc_sensor['z_'+str(k)+'2'])[i]*(acc_sensor['z_'+str(k)+'3'])[i]))/(math.sqrt(((acc_sensor['x_'+str(k)+'2'])[i]**2)+((acc_sensor['y_'+str(k)+'2'])[i]**2)+((acc_sensor['z_'+str(k)+'2'])[i]**2))*(math.sqrt(((acc_sensor['x_'+str(k)+'3'])[i]**2)+((acc_sensor['y_'+str(k)+'3'])[i]**2)+((acc_sensor['z_'+str(k)+'3'])[i]**2)))))
                        degree[j][i]=eval('angle[j][i]')*180/math.pi 
                    else:    
                         angle[j][i]=np.arccos((((-acc_sensor['x_'+str(k)+'2'])[i]*(acc_sensor['x_'+str(k)+'3'])[i])+((acc_sensor['y_'+str(k)+'2'])[i]*(acc_sensor['y_'+str(k)+'3'])[i])+((-acc_sensor['z_'+str(k)+'2'])[i]*(acc_sensor['z_'+str(k)+'3'])[i]))/(math.sqrt(((acc_sensor['x_'+str(k)+'2'])[i]**2)+((acc_sensor['y_'+str(k)+'2'])[i]**2)+((acc_sensor['z_'+str(k)+'2'])[i]**2))*(math.sqrt(((acc_sensor['x_'+str(k)+'3'])[i]**2)+((acc_sensor['y_'+str(k)+'3'])[i]**2)+((acc_sensor['z_'+str(k)+'3'])[i]**2)))))
                         degree[j][i]=eval('angle[j][i]')*180/math.pi 
    
    
                        
    for i in range(16):        
        globals()[angleall[i]]=thetadict.get(angleall[i])  
        globals()[degreeall[i]]=degreedict.get(degreeall[i])  
    
    for j in range(8): 
        for i in range (numdata): 
            if j==0:
                k=1
            else:
                k=j+1
            radius[j][i]=ljoint+lcont+(larm*(math.sin(math.radians(eval('degree[j][i]')))))
    
    
    for j in range(16):
        for i in range (numdata): 
            if j<=7:
                pass
            else:
                    k=aa[j]
                    radius[j][i]=ljoint+lcont+(larm*(math.sin(math.radians(eval('degree[j][i]')))))
               
    
    for i in range(16):        
        globals()[radiusall[i]]=radiusdict.get(radiusall[i])  
    
    
    for j in range(8): 
        for i in range (numdata): 
            if j==0:
                k=1
            else:
                k=j+1
            radius[j][i]=ljoint+lcont+(larm*(math.sin(math.radians(eval('degree[j][i]')))))
            radius[j][i]=radius[j][i] #cm
    
    for j in range(16):
        for i in range (numdata): 
            if j<=7:
                pass
            else:
                    k=aa[j]
                    radius[j][i]=ljoint+lcont+(larm*(math.sin(math.radians(eval('degree[j][i]')))))         
                    radius[j][i]=radius[j][i] #cm
    return degreeall,radiusall
                
