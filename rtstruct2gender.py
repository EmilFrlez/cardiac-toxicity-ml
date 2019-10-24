
import os
import glob

import pydicom as dicom

import matplotlib.pyplot as plt

import numpy as np

patients = ['AA', 'AP', 'AR', 'BB', 'BB1', 'BC', 'BD', 'BD1', 'BF', 'BJ', 'BL', 'BM', 'BR', 'CA-2A LUL', 'CE', 'CE1', 'CJ', 'CL-1A', 'CM', 'CR', 'CS', 'EC', 'FJ', 'FL-1A', 'GE', 'GF', 'GJ', 'GS', 'GV', 'HA', 'HB', 'HD', 'HH-1BR', 'HI', 'HJ', 'HM-1A', 'HR', 'HR1', 'JF', 'JL', 'JL1', 'JM-1A', 'JS-1B', 'KE-1A', 'LD', 'LJ', 'LL', 'LR-1A', 'LV-1A', 'MB', 'MD-1A', 'ME', 'ME1', 'MJ', 'MJ1', 'MK', 'ML', 'MM', 'MM1', 'MR', 'MS', 'OH', 'OP-1A', 'PH', 'PJ', 'RA', 'RD-1A', 'RH', 'RK', 'RM', 'SA', 'SB-1A', 'SE', 'SH', 'SJ-1A', 'SJ1-1A', 'SJ2', 'SR-1A', 'SR1', 'ST', 'TC', 'UB', 'VJ', 'WC', 'WH', 'WJ', 'WJ1']

str_files = []

for p in patients:
    fl = glob.glob(p+'/clinical/'+'RTSTRUCT*.dcm')
    exists = os.path.isfile(fl[0])
    if exists:
        str_files.append(fl[0])
        print(fl[0])
    else:
       pass

    rd_str = dicom.dcmread(fl[0], force=True)
    rd_str.dir() # check tags
    #print(rd_str.dir())
    print(p, rd_str.PatientSex)
