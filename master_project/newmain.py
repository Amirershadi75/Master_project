#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:37:31 2021

@author: amir
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 23:32:44 2021

@author: Amir
"""

##############################################################################
##############################################################################
##Load Data

import load as load
data,numdata,empty,NaN=load.l()
##############################################################################
#Import all Variables

import newvar as allvar
alldata,acc_sensor,ii,\
sensor_name,encoder_finder,encoder_diff,pressure,voltage,depth,aa,\
thetadict,angleall,degreedict,degreeall,ljoint,larm,lcont,radius,\
radiusdict,radiusall,angle,degree,inclinationdirection,incline,\
magnetic_declination,inclination_x,inclination_y,anglecaliball,degreecaliball,\
radiuscaliball,thetadict_calib,degree_calibdict,radius_calibdict,\
angle_calibrated,degree_calibrated,radius_calibrated\
=allvar.allvariable(numdata,data,empty,NaN)
###############################################################################
#Accelerometer sensors

import newacc as newacc
acc_sensor=newacc.acc(numdata,data,alldata,ii,sensor_name,acc_sensor,\
  NaN,encoder_finder,encoder_diff)
###############################################################################
##Pressure_VOLTAGE_Depth_TEMPERATURE,TIME

import newpvt
pressure,temperature,voltage,depth,time\
=newpvt.p_v_d_t(numdata,data,pressure,\
voltage,depth,NaN,encoder_finder,encoder_diff)

##############################################################################
#MAGNETOMETER SESNOR

import newmag as mag_sensor
magnetic_x,magnetic_y,magnetic_z,magneticfield_x_uncalibrated,\
magneticfield_y_uncalibrated,magneticfield_z_uncalibrated,absolute_uncalibrated_magneticfield\
=mag_sensor.magnetometer_sensor(numdata,data,NaN,encoder_finder,encoder_diff)
##############################################################################
##GYROSCOPE SENSOR

import newgyro as gyro_sensor
gyro_x,gyro_y,gyro_z,gyro_xuncalibrated,gyro_yuncalibrated,gyro_zuncalibrated,\
gyro_xcalibrated,gyro_ycalibrated,gyro_zcalibrated,gyro_rotation_uncalibrated,gyro_rotation_calibrated,\
gyro_rotation_xuncalibrated,gyro_rotation_xcalibrated,gyro_rotation_yuncalibrated,\
gyro_rotation_ycalibrated\
=gyro_sensor.gyroscope(numdata,data,NaN,encoder_finder,encoder_diff)
###############################################################################
# EXPORT RAW DATA

import exportrawdatanew as exportrawdatanew
exportdataraw=exportrawdatanew.raw(time,temperature,pressure,depth,voltage,\
magneticfield_x_uncalibrated,magneticfield_y_uncalibrated,magneticfield_z_uncalibrated,\
gyro_xuncalibrated,gyro_yuncalibrated,gyro_zuncalibrated,acc_sensor)
###############################################################################   
#Calculate the uncalibrated angle and radius of the arms

import newangleradius   
degreeall,radiusall\
=newangleradius.ang_rad(numdata, angle, degree, aa, thetadict,\
angleall, degreedict, degreeall, ljoint, larm, lcont, radius,\
radiusdict, radiusall,acc_sensor)        
###############################################################################   
#Uncalibrated rotation of the logger   

import newcalc 
sum_mag_declination,inclinationdirection\
=newcalc.inclination(numdata,inclinationdirection,incline,\
magnetic_declination,acc_sensor,magnetic_x,magnetic_y,magnetic_z)    
############################################################################### 
#Inclination 

import newinc
inclination_x,inclination_y,xarm_calibrated,yarm_calibrated,zarm_calibrated,\
xcalibrated,ycalibrated,zcalibrated,xx_calibrated,yy_calibrated,zz_calibrated,\
inclinationdirection,incline,x3_avg,y3_avg,z3_avg,inclination_xaxis_avg,inclination_yaxis_avg\
=newinc.calib(numdata,acc_sensor,sum_mag_declination,\
inclination_x,inclination_y)
###############################################################################
##ARM CALIBRATION

import newarmcalib
acc_sensor,radius_calibdict,degree_calibdict\
=newarmcalib.arm(acc_sensor,xarm_calibrated,yarm_calibrated,zarm_calibrated,\
numdata,anglecaliball,degreecaliball,radiuscaliball,thetadict_calib,degree_calibdict,radius_calibdict,\
angle_calibrated,degree_calibrated,radius_calibrated,aa,lcont,larm,ljoint) 
###############################################################################    
##MAG CALIBRATION

import magnetic_calibration
absolute_magneticfield,magnetic_declination,sum_mag_declination,diff_magnetic\
=magnetic_calibration.magcalib(magnetic_x,magnetic_y,magnetic_z,inclination_xaxis_avg,\
inclination_yaxis_avg,numdata,magnetic_declination,inclinationdirection)
###############################################################################    
import newexportcalib
    
exportdatacalibrated=newexportcalib.calibrated(time,temperature,magnetic_x,magnetic_y,\
magnetic_z,gyro_xcalibrated,gyro_ycalibrated,gyro_zcalibrated,acc_sensor)    
###############################################################################      
   
import newexportcalc 
exportdatacalculated=newexportcalc.calculated(absolute_magneticfield,\
absolute_uncalibrated_magneticfield,incline,magnetic_declination,sum_mag_declination,\
inclinationdirection,degreedict,radiusdict,degree_calibdict,radius_calibdict,\
gyro_rotation_uncalibrated,gyro_rotation_calibrated,inclination_x,inclination_y,depth) 
    
    