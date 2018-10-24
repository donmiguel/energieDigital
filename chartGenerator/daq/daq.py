#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DataAquisition

Created on Thu Oct 11 14:29:53 2018

@author: pi
"""
import comDevice
import time
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

filename = 'dataFile.csv'
sensor = comDevice.initBME680()
tint = 3 # [sec]
hukseConnect = False

try:
    while True:
        time.sleep(tint)
        currT = dt.datetime.now()
        
        temp, prea, humi, resi = comDevice.getBME680(sensor)
        if hukseConnect:
            resH, resT = comDevice.comHukse()             
        else:
            resH = 0
            resT = 0
            
        tempR = comDevice.rpiT()                    
        print(str(currT) + '; ' + \
              str(temp) + '°C; ' + \
              str(prea) + 'hPa; ' +  \
              str(humi) + '%; ' + \
              str(resi) + ' 100kOhm; ' + \
              str(tempR) + '°C; ' + \
              str(resH) + 'W/m2; ' + \
              str(resT) + '°C; ')

        string =  currT.strftime('%Y-%m-%d %H:%M:%S; ') + \
            str(temp) + ';' + \
            str(prea) + ';' +  \
            str(humi) + ';' + \
            str(resi) + ';' + \
            str(tempR) + ';' + \
            str(resH) + ';' + \
            str(resT) + '\n'
            
        file = open(filename, 'a')
        file.write(string)
        file.close()
except KeyboardInterrupt:
    pass