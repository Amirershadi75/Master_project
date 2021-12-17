#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 23:32:28 2021

@author: amir
"""

##Load Data
import decodea as decodea
from tkinter import filedialog
from tkinter import *
import os
import platform
global countnew
def l():
    #Find path and system platform
            path=os.path.abspath('calibration.txt')
            if platform.system()=='Darwin':
                path=path.replace("/calibration.txt", "")
            if platform.system()=='Linux':
                path=path.replace("/calibration.txt", "")    
            if platform.system()=='Windows':
                path=path.replace("\calibration.txt", "")
            try:    
                os.remove("test.raw") # one file at a time    
            except:
                pass
            Tk().withdraw()
            rawdata=filedialog.askopenfilename(filetypes=(("text file", "*.txt"), ("All files", "*.*")))
            raw=decodea.main(rawdata)
            fileObject = open("test.raw", encoding="utf8", errors='ignore')
            text_trans = fileObject.read()
            data=text_trans
            data=data.split ("\n")
            data=data[2:len(data)]
            numdata=len(data)-1
        
            data=str(data)
            data = data.replace("'", "")
            data = data.replace('"', "")
            data = data.replace(",", ";")
            data = data.replace(" ", "")
            data = data.replace(",", ";")
            data = data.replace(" ", "")
            data = data.replace(":", ";")
            data=data.split (";")
            data=' '.join(data).split()
            NaN = ("NaN")
            empty=[i for i,val in enumerate(data) if val=='[{}']
            
            return data,numdata,empty,NaN  
