#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:46:42 2021

@author: amir
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:03:21 2021

@author: amir
"""
import math
def acc(numdata,data,alldata,ii,sensor_name,acc_sensor,NaN,encoder_finder,encoder_diff):
        count=0
        for j in range(72):        
            for i in range (numdata):
                alldata[j][i]=(float(data[102+ii[j]+(i*585)]))
        for i in range (len(alldata)):
            globals()[sensor_name[i]]=(acc_sensor.get(sensor_name[i])/32)/4096
        for k in range(8):
            k=k+1
            for i in range (numdata):
                acc_sensor['x_'+str(k)+'1'][i]=(acc_sensor['x_'+str(k)+'1'][i]/32)/4096
                acc_sensor['y_'+str(k)+'1'][i]=(acc_sensor['y_'+str(k)+'1'][i]/32)/4096
                acc_sensor['z_'+str(k)+'1'][i]=(acc_sensor['z_'+str(k)+'1'][i]/32)/4096
                acc_sensor['x_'+str(k)+'2'][i]=(acc_sensor['x_'+str(k)+'2'][i]/32)/4096
                acc_sensor['y_'+str(k)+'2'][i]=(acc_sensor['y_'+str(k)+'2'][i]/32)/4096
                acc_sensor['z_'+str(k)+'2'][i]=(acc_sensor['z_'+str(k)+'2'][i]/32)/4096
                acc_sensor['x_'+str(k)+'3'][i]=(acc_sensor['x_'+str(k)+'3'][i]/32)/4096
                acc_sensor['y_'+str(k)+'3'][i]=(acc_sensor['y_'+str(k)+'3'][i]/32)/4096
                acc_sensor['z_'+str(k)+'3'][i]=(acc_sensor['z_'+str(k)+'3'][i]/32)/4096
        return   acc_sensor