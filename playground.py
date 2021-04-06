#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:03:25 2021

@author: garethlomax
"""


from osgeo import gdal
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import os
import cartopy.crs as ccrs
from matplotlib.colors import LinearSegmentedColormap as lsc

 # gdalwarp -s_srs "+proj=eqc +R=470000" -t_srs "+proj=ortho +lat_0=0 +lon_0=0" data/Ceres_Dawn_FC_HAMO_DTM_DLR_Global_60ppd_Oct2016.tif projections/ceres_ortho.tif
 # "cmap": ["#e6dfcf", "#ef9f30", "#638b71", "#24293c"],
 #        "levels": [-10000, 10000, 1000],
 #        "levels_small": [-20000, 20000, 5000],
# ax = plt.axes(projection=ccrs.PlateCarree())
# fig = plt.figure(figsize = (12, 8))
# ax = fig.add_subplot(111,projection=ccrs.PlateCarree())
# ax = fig.add_subplot(111)

# filename = "./DEM_geotiff/alwdgg.tif"
cmap = lsc.from_list("cmap", ["#e6dfcf", "#ef9f30", "#638b71", "#24293c"][::-1])
blacks = lsc.from_list("cmap", ["#000000", "#000000"])

filename = "projections/ortho_test.tif"
# filename = "projections/ceres_ortho.tif"
# filename = "data/Africa-30m-DEM.tif"
gdal_data = gdal.Open(filename)
gdal_band = gdal_data.GetRasterBand(1)
nodataval = gdal_band.GetNoDataValue()

# convert to a numpy array
data_array = gdal_data.ReadAsArray().astype(np.float)
data_array
n = 50
# replace missing values if necessary
if np.any(data_array == nodataval):
    data_array[data_array == nodataval] = np.nan
    
    
#Plot out data with Matplotlib's 'contour'
fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111)
# plt.contour(data_array, cmap = blacks, 
#             levels = list(range(-5000, 5000, 500)),linewidths = 0.3, alpha = 0.5)
plt.contour(data_array, cmap = blacks, 
            levels = n,linewidths = 0.3, alpha = 0.5)
# plt.title("Elevation Contours of Mt. Shasta")
# # cbar = plt.colorbar()
# plt.gca().set_aspect('equal', adjustable='box')
# # ax.set_ylim(ax.get_ylim()[::-1])

# plt.show()

#Plot our data with Matplotlib's 'contourf'
# fig = plt.figure(figsize = (12, 8))
# ax = fig.add_subplot(111)
# plt.contourf(data_array, cmap = cmap, 
#             levels = list(range(-5000, 5000, 500)))
plt.contourf(data_array, cmap = cmap, 
            levels = n)
plt.title("Elevation Contours of Mt. Shasta")
# cbar = plt.colorbar()
plt.gca().set_aspect('equal', adjustable='box')
ax.set_ylim(ax.get_ylim()[::-1])

plt.show()