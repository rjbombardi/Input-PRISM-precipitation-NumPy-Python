#!/usr/bin/python
#========================================================================
# How to read PRISM precipitation file as a grid using NumPy
#========================================================================
import numpy as np

# Edit the file names
# LatLon mesh .csv file
filein='PRISM_4kmesh_LatLong.csv'
# PRISM 4km .bil file
filein2='PRISM_ppt_stable_4kmD2_20010801_bil.bil'

# Reading coordinates as a list from a mesh csv file
latlon = []
fp = open(filein,'r')
for line in fp:
    line = line.strip()
    latlon.append(line)

fp.close()

# Generating arrays
missval=-9999.
nlon=1405
nlat=621

# Reading one of PRISM's files as a roster NumPy array
prism = np.fromfile(filein2, dtype=np.float32)
prism = prism.reshape(nlat, nlon)

# Mesh arrays of coordinates
lats=np.full((nlat,nlon),missval)
lons=np.full((nlat,nlon),missval)
tt=1 #start from 1 to skip header
for it in range(0,nlat):
    for jt in range(0,nlon):
        if prism[it,jt]>missval:
           lons[it,jt]=float(latlon[tt].split(',')[3])
           lats[it,jt]=float(latlon[tt].split(',')[4])
           tt+=1
