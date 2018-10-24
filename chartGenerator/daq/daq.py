#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DataAquisition

Created on Thu Oct 11 14:29:53 2018

@author: pi
"""
import os
import comDevice
import time
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

path = os.path.dirname(os.path.abspath(__file__)) # ermittelt Pfad in welchem dieses Skript-File liegt

filename =  path + '/dataFile.csv'
tint = 3 # [sec]
hukseConnect = False
bmeConnect = False

if bmeConnect:
    sensor = comDevice.initBME680()

try:
    while True:
        time.sleep(tint)
        currT = dt.datetime.now()

        if bmeConnect:
            temp, prea, humi, resi = comDevice.getBME680(sensor)
            tempR = comDevice.rpiT()
        else:
            temp = prea = humi = resi = tempR = 0
        if hukseConnect:
            resH, resT = comDevice.comHukse()
        else:
            resH = resT = 0

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
