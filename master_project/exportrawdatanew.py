#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 18:04:46 2021

@author: amir
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:04:24 2021

@author: amir
"""

import pandas as pd
def raw(time,temperature,pressure,\
depth,voltage,magneticfield_x_uncalibrated,magneticfield_y_uncalibrated,\
magneticfield_z_uncalibrated,gyro_xuncalibrated,gyro_yuncalibrated,\
gyro_zuncalibrated,acc_sensor):
    exportdataraw=pd.DataFrame(time, columns=['time'])
    exportdataraw=exportdataraw.assign(temperature=pd.Series(temperature).values)
    exportdataraw.rename(columns={'temperature': 'temperature [C]'}, inplace=True)
    exportdataraw=exportdataraw.assign(pressure_1=pressure['1'])
    exportdataraw=exportdataraw.assign(pressure_2=pressure['2'])
    exportdataraw=exportdataraw.assign(pressure_3=pressure['3'])
    exportdataraw=exportdataraw.assign(pressure_4=pressure['4'])
    exportdataraw=exportdataraw.assign(pressure_5=pressure['5'])
    exportdataraw=exportdataraw.assign(depth_1=depth['1'])
    exportdataraw=exportdataraw.assign(depth_2=depth['2'])
    exportdataraw.rename(columns={'logger_depth': 'logger_depth [m]'}, inplace=True)
    exportdataraw=exportdataraw.assign(depth_3=depth['3'])
    exportdataraw.rename(columns={'velocity': 'velocity [m/s]'}, inplace=True)
    exportdataraw=exportdataraw.assign(depth_4=depth['4'])
    exportdataraw.rename(columns={'acceleration': 'acceleration [m/s^2]'}, inplace=True)
    exportdataraw=exportdataraw.assign(voltage_1=voltage['1'])
    exportdataraw.rename(columns={'voltage_1': 'voltage_1 [Volt]'}, inplace=True)
    exportdataraw=exportdataraw.assign(voltage_2=voltage['2'])
    exportdataraw.rename(columns={'voltage_2': 'voltage_2 [Volt]'}, inplace=True)
    exportdataraw=exportdataraw.assign(voltage_3=voltage['3'])
    exportdataraw.rename(columns={'voltage_3': 'voltage_3 [Volt]'}, inplace=True)
    exportdataraw=exportdataraw.assign(voltage_4=voltage['4'])
    exportdataraw.rename(columns={'voltage_4': 'voltage_4 [Volt]'}, inplace=True)
    exportdataraw=exportdataraw.assign(magneticfield_x_uncalibrated=pd.Series(magneticfield_x_uncalibrated).values)
    exportdataraw.rename(columns={'magneticfield_x_uncalibrated': 'magneticfield_x_uncalibrated [??T]'}, inplace=True)
    exportdataraw=exportdataraw.assign(magneticfield_y_uncalibrated=pd.Series(magneticfield_y_uncalibrated).values)
    exportdataraw.rename(columns={'magneticfield_y_uncalibrated': 'magneticfield_y_uncalibrated [??T]'}, inplace=True)
    exportdataraw=exportdataraw.assign(magneticfield_z_uncalibrated=pd.Series(magneticfield_z_uncalibrated).values)
    exportdataraw.rename(columns={'magneticfield_z_uncalibrated': 'magneticfield_z_uncalibrated [??T]'}, inplace=True)
    exportdataraw=exportdataraw.assign(gyro_x_uncalibrated=pd.Series(gyro_xuncalibrated).values)
    exportdataraw.rename(columns={'gyro_x_uncalibrated': 'gyro_x_uncalibrated [deg]'}, inplace=True)
    exportdataraw=exportdataraw.assign(gyro_y_uncalibrated=pd.Series(gyro_yuncalibrated).values)
    exportdataraw.rename(columns={'gyro_y_uncalibrated': 'gyro_y_uncalibrated [deg]'}, inplace=True)
    exportdataraw=exportdataraw.assign(gyro_z_uncalibrated=pd.Series(gyro_zuncalibrated).values)
    exportdataraw.rename(columns={'gyro_z_uncalibrated': 'gyro_z_uncalibrated [deg]'}, inplace=True)
    exportdataraw=exportdataraw.assign(x_11=acc_sensor['x_11'])
    exportdataraw=exportdataraw.assign(x_12=acc_sensor['x_12'])
    exportdataraw=exportdataraw.assign(x_13=acc_sensor['x_13'])
    exportdataraw=exportdataraw.assign(y_11=acc_sensor['y_11'])
    exportdataraw=exportdataraw.assign(y_12=acc_sensor['y_12'])
    exportdataraw=exportdataraw.assign(y_13=acc_sensor['y_13'])
    exportdataraw=exportdataraw.assign(z_11=acc_sensor['z_11'])
    exportdataraw=exportdataraw.assign(z_12=acc_sensor['z_12'])
    exportdataraw=exportdataraw.assign(z_13=acc_sensor['z_13'])
    exportdataraw=exportdataraw.assign(x_21=acc_sensor['x_21'])
    exportdataraw=exportdataraw.assign(x_22=acc_sensor['x_22'])
    exportdataraw=exportdataraw.assign(x_23=acc_sensor['x_23'])
    exportdataraw=exportdataraw.assign(y_21=acc_sensor['y_21'])
    exportdataraw=exportdataraw.assign(y_22=acc_sensor['y_22'])
    exportdataraw=exportdataraw.assign(y_23=acc_sensor['y_23'])
    exportdataraw=exportdataraw.assign(z_21=acc_sensor['z_21'])
    exportdataraw=exportdataraw.assign(z_22=acc_sensor['z_22'])
    exportdataraw=exportdataraw.assign(z_23=acc_sensor['z_23'])
    exportdataraw=exportdataraw.assign(x_31=acc_sensor['x_31'])
    exportdataraw=exportdataraw.assign(x_32=acc_sensor['x_32'])
    exportdataraw=exportdataraw.assign(x_33=acc_sensor['x_33'])
    exportdataraw=exportdataraw.assign(y_31=acc_sensor['y_31'])
    exportdataraw=exportdataraw.assign(y_32=acc_sensor['y_32'])
    exportdataraw=exportdataraw.assign(y_33=acc_sensor['y_33'])
    exportdataraw=exportdataraw.assign(z_31=acc_sensor['z_31'])
    exportdataraw=exportdataraw.assign(z_32=acc_sensor['z_32'])
    exportdataraw=exportdataraw.assign(z_33=acc_sensor['z_33'])
    exportdataraw=exportdataraw.assign(x_41=acc_sensor['x_41'])
    exportdataraw=exportdataraw.assign(x_42=acc_sensor['x_42'])
    exportdataraw=exportdataraw.assign(x_43=acc_sensor['x_43'])
    exportdataraw=exportdataraw.assign(y_41=acc_sensor['y_41'])
    exportdataraw=exportdataraw.assign(y_42=acc_sensor['y_42'])
    exportdataraw=exportdataraw.assign(y_43=acc_sensor['y_43'])
    exportdataraw=exportdataraw.assign(z_41=acc_sensor['z_41'])
    exportdataraw=exportdataraw.assign(z_42=acc_sensor['z_42'])
    exportdataraw=exportdataraw.assign(z_43=acc_sensor['z_43'])
    exportdataraw=exportdataraw.assign(x_51=acc_sensor['x_51'])
    exportdataraw=exportdataraw.assign(x_52=acc_sensor['x_52'])
    exportdataraw=exportdataraw.assign(x_53=acc_sensor['x_53'])
    exportdataraw=exportdataraw.assign(y_51=acc_sensor['y_51'])
    exportdataraw=exportdataraw.assign(y_52=acc_sensor['y_52'])
    exportdataraw=exportdataraw.assign(y_53=acc_sensor['y_53'])
    exportdataraw=exportdataraw.assign(z_51=acc_sensor['z_51'])
    exportdataraw=exportdataraw.assign(z_52=acc_sensor['z_52'])
    exportdataraw=exportdataraw.assign(z_53=acc_sensor['z_53'])
    exportdataraw=exportdataraw.assign(x_61=acc_sensor['x_61'])
    exportdataraw=exportdataraw.assign(x_62=acc_sensor['x_62'])
    exportdataraw=exportdataraw.assign(x_63=acc_sensor['x_63'])
    exportdataraw=exportdataraw.assign(y_61=acc_sensor['y_61'])
    exportdataraw=exportdataraw.assign(y_62=acc_sensor['y_62'])
    exportdataraw=exportdataraw.assign(y_63=acc_sensor['y_63'])
    exportdataraw=exportdataraw.assign(z_61=acc_sensor['z_61'])
    exportdataraw=exportdataraw.assign(z_62=acc_sensor['z_62'])
    exportdataraw=exportdataraw.assign(z_63=acc_sensor['z_63'])
    exportdataraw=exportdataraw.assign(x_71=acc_sensor['x_71'])
    exportdataraw=exportdataraw.assign(x_72=acc_sensor['x_72'])
    exportdataraw=exportdataraw.assign(x_73=acc_sensor['x_73'])
    exportdataraw=exportdataraw.assign(y_71=acc_sensor['y_71'])
    exportdataraw=exportdataraw.assign(y_72=acc_sensor['y_72'])
    exportdataraw=exportdataraw.assign(y_73=acc_sensor['y_73'])
    exportdataraw=exportdataraw.assign(z_71=acc_sensor['z_71'])
    exportdataraw=exportdataraw.assign(z_72=acc_sensor['z_72'])
    exportdataraw=exportdataraw.assign(z_73=acc_sensor['z_73'])
    exportdataraw=exportdataraw.assign(x_81=acc_sensor['x_81'])
    exportdataraw=exportdataraw.assign(x_82=acc_sensor['x_82'])
    exportdataraw=exportdataraw.assign(x_83=acc_sensor['x_83'])
    exportdataraw=exportdataraw.assign(y_81=acc_sensor['y_81'])
    exportdataraw=exportdataraw.assign(y_82=acc_sensor['y_82'])
    exportdataraw=exportdataraw.assign(y_83=acc_sensor['y_83'])
    exportdataraw=exportdataraw.assign(z_81=acc_sensor['z_81'])
    exportdataraw=exportdataraw.assign(z_82=acc_sensor['z_82'])
    exportdataraw=exportdataraw.assign(z_83=acc_sensor['z_83'])    
    exportdataraw.to_excel('rawdata.xlsx')    