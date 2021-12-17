#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:38:50 2021

@author: amir
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:18:55 2021

@author: amir
"""
import math    
import numpy as np
def p_v_d_t(numdata,data,pressure,\
voltage,depth,NaN,encoder_finder,encoder_diff):

    
        for i in range (numdata):
            
        #with encoder        
                    time=np.zeros(numdata)
                    temperature=np.zeros(numdata)
                    #Define pressure,temperature,voltage,depth of the logger
                    for i in range (numdata):
                     pressure['1'][i]=(float(data[66+(i*585)]))
                     pressure['2'][i]=(float(data[72+(i*585)]))
                     pressure['3'][i]=(float(data[78+(i*585)]))
                     pressure['4'][i]=(float(data[84+(i*585)]))
                     pressure['5'][i]=(float(data[90+(i*585)]))     #INCH HG
                     temperature[i]=(float(data[6+(i*585)])) 
                     voltage['1'][i]=(float(data[2+(i*585)]))
                     voltage['2'][i]=(float(data[3+(i*585)]))
                     voltage['3'][i]=(float(data[4+(i*585)]))
                     voltage['4'][i]=(float(data[5+(i*585)]))
                     if '[' in data[0+(i*585)]:
                         data[0+(i*585)]=data[0+(i*585)][1:18]
                         time[i]=((data[0+(i*585)]))
                     else:   
                         time[i]=((data[0+(i*585)])) 
                     if math.isnan(float(data[10]))==False:
                         try:
                             depth['1'][i]=(float(data[10+(i*585)]))
                             depth['2'][i]=(float(data[11+(i*585)]))
                             depth['3'][i]=(float(data[12+(i*585)]))
                             depth['4'][i]=(float(data[13+(i*585)]))     
                         except:
                             depth['1'][i]='NaN'
                             depth['2'][i]='NaN'
                             depth['3'][i]='NaN'
                             depth['4'][i]='NaN'
        return pressure,temperature,voltage,depth,time
                 