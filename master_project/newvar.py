#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:41:47 2021

@author: amir
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 12:27:07 2021

@author: amir
"""
import numpy as np

def allvariable(numdata,data,empty,NaN):
    acc_sensor={}
    pressure={}
    voltage={}
    depth={}
    pressure['1']=np.zeros(numdata)
    pressure['2']=np.zeros(numdata)
    pressure['3']=np.zeros(numdata)
    pressure['4']=np.zeros(numdata)
    pressure['5']=np.zeros(numdata)
    voltage['1']=np.zeros(numdata)
    voltage['2']=np.zeros(numdata)
    voltage['3']=np.zeros(numdata)
    voltage['4']=np.zeros(numdata)
    depth['1']=np.zeros(numdata)
    depth['2']=np.zeros(numdata)
    depth['3']=np.zeros(numdata)
    depth['4']=np.zeros(numdata)
    

    thetadict={}
    thetadict_calib={}
    inclination_x={}
    inclination_y={}
  
    degreedict={}  
    radiusdict={} 
    degree_calibdict={}  
    radius_calibdict={}     

     
    magnetic_declination =np.zeros(numdata) 
    inclinationdirection=np.zeros(numdata)
    incline=np.zeros(numdata)
    logger_height=np.zeros(numdata-1)
    logger_height=np.arange(0,numdata*10,10)
    logger_height=-logger_height
    ii=np.arange(0,72)
    ii=ii*6 
    lcont=15 #mm
    larm=130.2 #mm
    ljoint=35 #mm  
    for i in range (8):
        i=i+1   
        i=str(i)    
        acc_sensor["x_" +i+'1']=np.zeros(numdata)
        acc_sensor["y_" +i+'1']=np.zeros(numdata)
        acc_sensor["z_" +i+'1']=np.zeros(numdata)
        acc_sensor["x_" +i+'2']=np.zeros(numdata)
        acc_sensor["y_" +i+'2']=np.zeros(numdata)
        acc_sensor["z_" +i+'2']=np.zeros(numdata)
        acc_sensor["x_" +i+'3']=np.zeros(numdata)
        acc_sensor["y_" +i+'3']=np.zeros(numdata)
        acc_sensor["z_" +i+'3']=np.zeros(numdata)
        inclination_x["inclination_xaxis_"+i+'3']=np.zeros(numdata) 
        inclination_y["inclination_yaxis_"+i+'3']=np.zeros(numdata) 
        i=int(i)
        sensor_name=list(acc_sensor.keys())   
    for i in range (8):
        i=i+1   
        i=str(i) 
        thetadict["theta_" +i+'1_'+i+'3']=np.zeros(numdata) 
        thetadict_calib["thetacalib_" +i+'1_'+i+'3']=np.zeros(numdata)
        degreedict["degree_" +i+'1_'+i+'3']=np.zeros(numdata) 
        degree_calibdict["degreecalib_" +i+'1_'+i+'3']=np.zeros(numdata) 
        radiusdict["radius_" +i+'1_'+i+'3']=np.zeros(numdata) 
        radius_calibdict["radiuscalib_" +i+'1_'+i+'3']=np.zeros(numdata)   
   
    aa=np.arange(9)
    aa=list(aa)
    aa=aa+aa

    for i in range (8):
            i=i+1
            i=str(i) 
            thetadict["theta_" +i+'2_'+i+'3']=np.zeros(numdata)
            thetadict_calib["thetacalib_" +i+'2_'+i+'3']=np.zeros(numdata)
            angleall=list(thetadict.keys())
            anglecaliball=list(thetadict_calib.keys())
            degreedict["degree_" +i+'2_'+i+'3']=np.zeros(numdata) 
            degree_calibdict["degreecalib_" +i+'2_'+i+'3']=np.zeros(numdata)
            degreeall=list(degreedict.keys())  
            degreecaliball=list(degree_calibdict.keys()) 
            radiusdict["radius_" +i+'2_'+i+'3']=np.zeros(numdata)    
            radius_calibdict["radiuscalib_" +i+'2_'+i+'3']=np.zeros(numdata) 
            radiusall=list(radiusdict.keys())  
            radiuscaliball=list(radius_calibdict.keys())    

    for i in range (len(empty)):
        empty=data.index('[{}')
        index=empty
        data[index]=str(NaN)
        data[index+1]=str(NaN)
        data[index+2]=str(NaN)
    
        for j in range (15):
           data.insert(index,str(NaN))
    
    
    for j in range (72):    
            alldata=list(acc_sensor.values())
            try:
                alldata[j][0]=(float(data[101+ii[j]]))
            except:
                alldata[j][0]=(float(data[102+ii[j]]))
            angle=list(thetadict.values())
            angle_calibrated=list(thetadict_calib.values())
            degree=list(degreedict.values())
            degree_calibrated=list(degree_calibdict.values())
            radius=list(radiusdict.values())
            radius_calibrated=list(radius_calibdict.values())

    encoder_finder=[i for i,val in enumerate(data) if val=='201']       
    encoder_diff=np.diff(encoder_finder)
    import math
    count=0
    for i in range (numdata):
        try:
            if math.isnan(float(data[encoder_finder[i]+count+1]))==True:
                data.insert(encoder_finder[i]+i+1,'NaN')
                count=count+1
        except:
            pass
    return alldata,acc_sensor,ii,\
sensor_name,encoder_finder,encoder_diff,pressure,voltage,depth,aa,\
thetadict,angleall,degreedict,degreeall,ljoint,larm,lcont,radius,\
radiusdict,radiusall,angle,degree,inclinationdirection,incline,\
magnetic_declination,inclination_x,inclination_y,anglecaliball,degreecaliball,\
radiuscaliball,thetadict_calib,degree_calibdict,radius_calibdict,\
angle_calibrated,degree_calibrated,radius_calibrated
 