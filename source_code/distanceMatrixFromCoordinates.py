#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 21:50:54 2024

@author: sylvestre
"""

from scipy.spatial import distance_matrix
def buildDistanceMatrixFromCoordinates(filename):
    coords=[]
    f=open(filename,"r")
    lines=f.readlines()
    for l in lines[1:]:
        vLine=l.strip().split(",")
        coord=[float(vLine[1]),float(vLine[2])]
        coords.append(coord)
    f.close()
    print(coords)
    return distance_matrix(coords,coords)