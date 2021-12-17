#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 23:07:06 2021

@author: amir
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 21:00:31 2021

@author: amir
"""

import pandas as pd
def calculated(absolute_magneticfield,\
absolute_uncalibrated_magneticfield,incline,magnetic_declination,sum_mag_declination,\
inclinationdirection,degreedict,radiusdict,degree_calibdict,radius_calibdict,\
gyro_rotation_uncalibrated,gyro_rotation_calibrated,inclination_x,inclination_y,depth):

    exportdata_calculated=pd.DataFrame(depth['2'], columns=['Logger depth [cm]'])
    exportdata_calculated=exportdata_calculated.assign(absolute_magneticfield=pd.Series(absolute_magneticfield).values)
    exportdata_calculated.rename(columns={'absolute_magneticfield': 'absolute_magneticfield [µT]'}, inplace=True)   
    exportdata_calculated=exportdata_calculated.assign(absolute_uncalibrated_magneticfield=pd.Series(absolute_uncalibrated_magneticfield).values)
    exportdata_calculated.rename(columns={'absolute_uncalibrated_magneticfield': 'absolute_uncalibrated_magneticfield [µT]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(absolute_inclination=pd.Series(incline).values)
    exportdata_calculated.rename(columns={'absolute_inclination': 'absolute_inclination [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(magnetic_declination=pd.Series(magnetic_declination).values)
    exportdata_calculated.rename(columns={'magnetic_declination': 'magnetic_declination [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(total_rotation=pd.Series(sum_mag_declination).values)
    exportdata_calculated.rename(columns={'total_rotation': 'total_rotation [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(gyro_rotation_uncalibrated=pd.Series(gyro_rotation_uncalibrated).values)
    exportdata_calculated.rename(columns={'gyro_rotation_uncalibrated': 'gyro_rotation_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(gyro_rotation_calibrated=pd.Series(gyro_rotation_calibrated).values)
    exportdata_calculated.rename(columns={'gyro_rotation_calibrated': 'gyro_rotation_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_direction=pd.Series(inclinationdirection).values)
    exportdata_calculated.rename(columns={'inclination_direction': 'inclination_direction [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm11_calibrated=pd.Series(degree_calibdict['degreecalib_11_13']).values)
    exportdata_calculated.rename(columns={'angle_arm11_calibrated': 'angle_arm11_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm11_uncalibrated=pd.Series(degreedict['degree_11_13']).values)
    exportdata_calculated.rename(columns={'angle_arm11_uncalibrated': 'angle_arm11_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm21_calibrated=pd.Series(degree_calibdict['degreecalib_21_23']).values)
    exportdata_calculated.rename(columns={'angle_arm21_calibrated': 'angle_arm21_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm21_uncalibrated=pd.Series(degreedict['degree_21_23']).values)
    exportdata_calculated.rename(columns={'angle_arm21_uncalibrated': 'angle_arm21_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm31_calibrated=pd.Series(degree_calibdict['degreecalib_31_33']).values)
    exportdata_calculated.rename(columns={'angle_arm31_calibrated': 'angle_arm31_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm31_uncalibrated=pd.Series(degreedict['degree_31_33']).values)
    exportdata_calculated.rename(columns={'angle_arm31_uncalibrated': 'angle_arm31_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm41_calibrated=pd.Series(degree_calibdict['degreecalib_41_43']).values)
    exportdata_calculated.rename(columns={'angle_arm41_calibrated': 'angle_arm41_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm41_uncalibrated=pd.Series(degreedict['degree_41_43']).values)
    exportdata_calculated.rename(columns={'angle_arm41_uncalibrated': 'angle_arm41_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm51_calibrated=pd.Series(degree_calibdict['degreecalib_51_53']).values)
    exportdata_calculated.rename(columns={'angle_arm51_calibrated': 'angle_arm51_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm51_uncalibrated=pd.Series(degreedict['degree_51_53']).values)
    exportdata_calculated.rename(columns={'angle_arm51_uncalibrated': 'angle_arm51_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm61_calibrated=pd.Series(degree_calibdict['degreecalib_61_63']).values)
    exportdata_calculated.rename(columns={'angle_arm61_calibrated': 'angle_arm61_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm61_uncalibrated=pd.Series(degreedict['degree_61_63']).values)
    exportdata_calculated.rename(columns={'angle_arm61_uncalibrated': 'angle_arm61_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm71_calibrated=pd.Series(degree_calibdict['degreecalib_71_73']).values)
    exportdata_calculated.rename(columns={'angle_arm71_calibrated': 'angle_arm71_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm71_uncalibrated=pd.Series(degreedict['degree_71_73']).values)
    exportdata_calculated.rename(columns={'angle_arm71_uncalibrated': 'angle_arm71_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm81_calibrated=pd.Series(degree_calibdict['degreecalib_81_83']).values)
    exportdata_calculated.rename(columns={'angle_arm81_calibrated': 'angle_arm81_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm81_uncalibrated=pd.Series(degreedict['degree_81_83']).values)
    exportdata_calculated.rename(columns={'angle_arm81_uncalibrated': 'angle_arm81_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm12_calibrated=pd.Series(degree_calibdict['degreecalib_12_13']).values)
    exportdata_calculated.rename(columns={'angle_arm12_calibrated': 'angle_arm12_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm12_uncalibrated=pd.Series(degreedict['degree_12_13']).values)
    exportdata_calculated.rename(columns={'angle_arm12_uncalibrated': 'angle_arm12_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm22_calibrated=pd.Series(degree_calibdict['degreecalib_22_23']).values)
    exportdata_calculated.rename(columns={'angle_arm22_calibrated': 'angle_arm22_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm22_uncalibrated=pd.Series(degreedict['degree_22_23']).values)
    exportdata_calculated.rename(columns={'angle_arm22_uncalibrated': 'angle_arm22_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm32_calibrated=pd.Series(degree_calibdict['degreecalib_32_33']).values)
    exportdata_calculated.rename(columns={'angle_arm32_calibrated': 'angle_arm32_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm32_uncalibrated=pd.Series(degreedict['degree_32_33']).values)
    exportdata_calculated.rename(columns={'angle_arm32_uncalibrated': 'angle_arm32_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm42_calibrated=pd.Series(degree_calibdict['degreecalib_42_43']).values)
    exportdata_calculated.rename(columns={'angle_arm42_calibrated': 'angle_arm42_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm42_uncalibrated=pd.Series(degreedict['degree_42_43']).values)
    exportdata_calculated.rename(columns={'angle_arm42_uncalibrated': 'angle_arm42_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm52_calibrated=pd.Series(degree_calibdict['degreecalib_52_53']).values)
    exportdata_calculated.rename(columns={'angle_arm52_calibrated': 'angle_arm52_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm52_uncalibrated=pd.Series(degreedict['degree_52_53']).values)
    exportdata_calculated.rename(columns={'angle_arm52_uncalibrated': 'angle_arm52_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm62_calibrated=pd.Series(degree_calibdict['degreecalib_62_63']).values)
    exportdata_calculated.rename(columns={'angle_arm62_calibrated': 'angle_arm62_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm62_uncalibrated=pd.Series(degreedict['degree_62_63']).values)
    exportdata_calculated.rename(columns={'angle_arm62_uncalibrated': 'angle_arm62_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm72_calibrated=pd.Series(degree_calibdict['degreecalib_72_73']).values)
    exportdata_calculated.rename(columns={'angle_arm72_calibrated': 'angle_arm72_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm72_uncalibrated=pd.Series(degreedict['degree_72_73']).values)
    exportdata_calculated.rename(columns={'angle_arm72_uncalibrated': 'angle_arm72_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm82_calibrated=pd.Series(degree_calibdict['degreecalib_82_83']).values)
    exportdata_calculated.rename(columns={'angle_arm82_calibrated': 'angle_arm82_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(angle_arm82_uncalibrated=pd.Series(degreedict['degree_82_83']).values)
    exportdata_calculated.rename(columns={'angle_arm82_uncalibrated': 'angle_arm82_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm11_calibrated=pd.Series(radius_calibdict['radiuscalib_11_13']).values)
    exportdata_calculated.rename(columns={'radius_arm11_calibrated': 'radius_arm11_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm11_uncalibrated=pd.Series(radiusdict['radius_11_13']).values)
    exportdata_calculated.rename(columns={'radius_arm11_uncalibrated': 'radius_arm11_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm21_calibrated=pd.Series(radius_calibdict['radiuscalib_21_23']).values)
    exportdata_calculated.rename(columns={'radius_arm21_calibrated': 'radius_arm21_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm21_uncalibrated=pd.Series(radiusdict['radius_21_23']).values)
    exportdata_calculated.rename(columns={'radius_arm21_uncalibrated': 'radius_arm21_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm31_calibrated=pd.Series(radius_calibdict['radiuscalib_31_33']).values)
    exportdata_calculated.rename(columns={'radius_arm31_calibrated': 'radius_arm31_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm31_uncalibrated=pd.Series(radiusdict['radius_31_33']).values)
    exportdata_calculated.rename(columns={'radius_arm31_uncalibrated': 'radius_arm31_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm41_calibrated=pd.Series(radius_calibdict['radiuscalib_41_43']).values)
    exportdata_calculated.rename(columns={'radius_arm41_calibrated': 'radius_arm41_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm41_uncalibrated=pd.Series(radiusdict['radius_41_43']).values)
    exportdata_calculated.rename(columns={'radius_arm41_uncalibrated': 'radius_arm41_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm51_calibrated=pd.Series(radius_calibdict['radiuscalib_51_53']).values)
    exportdata_calculated.rename(columns={'radius_arm51_calibrated': 'radius_arm51_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm51_uncalibrated=pd.Series(radiusdict['radius_51_53']).values)
    exportdata_calculated.rename(columns={'radius_arm51_uncalibrated': 'radius_arm51_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm61_calibrated=pd.Series(radius_calibdict['radiuscalib_61_63']).values)
    exportdata_calculated.rename(columns={'radius_arm61_calibrated': 'radius_arm61_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm61_uncalibrated=pd.Series(radiusdict['radius_61_63']).values)
    exportdata_calculated.rename(columns={'radius_arm61_uncalibrated': 'radius_arm61_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm71_calibrated=pd.Series(radius_calibdict['radiuscalib_71_73']).values)
    exportdata_calculated.rename(columns={'radius_arm71_calibrated': 'radius_arm71_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm71_uncalibrated=pd.Series(radiusdict['radius_71_73']).values)
    exportdata_calculated.rename(columns={'radius_arm71_uncalibrated': 'radius_arm71_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm81_calibrated=pd.Series(radius_calibdict['radiuscalib_81_83']).values)
    exportdata_calculated.rename(columns={'radius_arm81_calibrated': 'radius_arm81_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm81_uncalibrated=pd.Series(radiusdict['radius_81_83']).values)
    exportdata_calculated.rename(columns={'radius_arm81_uncalibrated': 'radius_arm81_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm12_calibrated=pd.Series(radius_calibdict['radiuscalib_12_13']).values)
    exportdata_calculated.rename(columns={'radius_arm12_calibrated': 'radius_arm12_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm12_uncalibrated=pd.Series(radiusdict['radius_12_13']).values)
    exportdata_calculated.rename(columns={'radius_arm12_uncalibrated': 'radius_arm12_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm22_calibrated=pd.Series(radius_calibdict['radiuscalib_22_23']).values)
    exportdata_calculated.rename(columns={'radius_arm22_calibrated': 'radius_arm22_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm22_uncalibrated=pd.Series(radiusdict['radius_22_23']).values)
    exportdata_calculated.rename(columns={'radius_arm22_uncalibrated': 'radius_arm22_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm32_calibrated=pd.Series(radius_calibdict['radiuscalib_32_33']).values)
    exportdata_calculated.rename(columns={'radius_arm32_calibrated': 'radius_arm32_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm32_uncalibrated=pd.Series(radiusdict['radius_32_33']).values)
    exportdata_calculated.rename(columns={'radius_arm32_uncalibrated': 'radius_arm32_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm42_calibrated=pd.Series(radius_calibdict['radiuscalib_42_43']).values)
    exportdata_calculated.rename(columns={'radius_arm42_calibrated': 'radius_arm42_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm42_uncalibrated=pd.Series(radiusdict['radius_42_43']).values)
    exportdata_calculated.rename(columns={'radius_arm42_uncalibrated': 'radius_arm42_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm52_calibrated=pd.Series(radius_calibdict['radiuscalib_52_53']).values)
    exportdata_calculated.rename(columns={'radius_arm52_calibrated': 'radius_arm52_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm52_uncalibrated=pd.Series(radiusdict['radius_52_53']).values)
    exportdata_calculated.rename(columns={'radius_arm52_uncalibrated': 'radius_arm52_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm62_calibrated=pd.Series(radius_calibdict['radiuscalib_62_63']).values)
    exportdata_calculated.rename(columns={'radius_arm62_calibrated': 'radius_arm62_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm62_uncalibrated=pd.Series(radiusdict['radius_62_63']).values)
    exportdata_calculated.rename(columns={'radius_arm62_uncalibrated': 'radius_arm62_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm72_calibrated=pd.Series(radius_calibdict['radiuscalib_72_73']).values)
    exportdata_calculated.rename(columns={'radius_arm72_calibrated': 'radius_arm72_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm72_uncalibrated=pd.Series(radiusdict['radius_72_73']).values)
    exportdata_calculated.rename(columns={'radius_arm72_uncalibrated': 'radius_arm72_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm82_calibrated=pd.Series(radius_calibdict['radiuscalib_82_83']).values)
    exportdata_calculated.rename(columns={'radius_arm82_calibrated': 'radius_arm82_calibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(radius_arm82_uncalibrated=pd.Series(radiusdict['radius_82_83']).values)
    exportdata_calculated.rename(columns={'radius_arm82_uncalibrated': 'radius_arm82_uncalibrated [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_xaxis_13=pd.Series(inclination_x['inclination_xaxis_13']).values)
    exportdata_calculated.rename(columns={'inclination_xaxis_13': 'inclination_xaxis_13 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_xaxis_23=pd.Series(inclination_x['inclination_xaxis_23']).values)
    exportdata_calculated.rename(columns={'inclination_xaxis_23': 'inclination_xaxis_23 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_xaxis_33=pd.Series(inclination_x['inclination_xaxis_33']).values)
    exportdata_calculated.rename(columns={'inclination_xaxis_33': 'inclination_xaxis_33 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_xaxis_43=pd.Series(inclination_x['inclination_xaxis_43']).values)
    exportdata_calculated.rename(columns={'inclination_xaxis_43': 'inclination_xaxis_43 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_xaxis_53=pd.Series(inclination_x['inclination_xaxis_53']).values)
    exportdata_calculated.rename(columns={'inclination_xaxis_53': 'inclination_xaxis_53 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_xaxis_63=pd.Series(inclination_x['inclination_xaxis_63']).values)
    exportdata_calculated.rename(columns={'inclination_xaxis_63': 'inclination_xaxis_63 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_xaxis_73=pd.Series(inclination_x['inclination_xaxis_73']).values)
    exportdata_calculated.rename(columns={'inclination_xaxis_73': 'inclination_xaxis_73 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_xaxis_83=pd.Series(inclination_x['inclination_xaxis_83']).values)
    exportdata_calculated.rename(columns={'inclination_xaxis_83': 'inclination_xaxis_83 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_yaxis_13=pd.Series(inclination_y['inclination_yaxis_13']).values)
    exportdata_calculated.rename(columns={'inclination_yaxis_13': 'inclination_yaxis_13 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_yaxis_23=pd.Series(inclination_y['inclination_yaxis_23']).values)
    exportdata_calculated.rename(columns={'inclination_yaxis_23': 'inclination_yaxis_23 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_yaxis_33=pd.Series(inclination_y['inclination_yaxis_33']).values)
    exportdata_calculated.rename(columns={'inclination_yaxis_33': 'inclination_yaxis_33 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_yaxis_43=pd.Series(inclination_y['inclination_yaxis_43']).values)
    exportdata_calculated.rename(columns={'inclination_yaxis_43': 'inclination_yaxis_43 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_yaxis_53=pd.Series(inclination_y['inclination_yaxis_53']).values)
    exportdata_calculated.rename(columns={'inclination_yaxis_53': 'inclination_yaxis_53 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_yaxis_63=pd.Series(inclination_y['inclination_yaxis_63']).values)
    exportdata_calculated.rename(columns={'inclination_yaxis_63': 'inclination_yaxis_63 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_yaxis_73=pd.Series(inclination_y['inclination_yaxis_73']).values)
    exportdata_calculated.rename(columns={'inclination_yaxis_73': 'inclination_yaxis_73 [deg]'}, inplace=True)
    exportdata_calculated=exportdata_calculated.assign(inclination_yaxis_83=pd.Series(inclination_y['inclination_yaxis_83']).values)
    exportdata_calculated.rename(columns={'inclination_yaxis_83': 'inclination_yaxis_83 [deg]'}, inplace=True)    
    exportdata_calculated.to_excel('calculated_data.xlsx')