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


# ax = plt.axes(projection=ccrs.PlateCarree())
# fig = plt.figure(figsize = (12, 8))
# ax = fig.add_subplot(111,projection=ccrs.PlateCarree())
# ax = fig.add_subplot(111)

# filename = "./DEM_geotiff/alwdgg.tif"
filename = "projections/ortho_test.tif"
gdal_data = gdal.Open(filename)
gdal_band = gdal_data.GetRasterBand(1)
nodataval = gdal_band.GetNoDataValue()

# convert to a numpy array
data_array = gdal_data.ReadAsArray().astype(np.float)
data_array

# replace missing values if necessary
if np.any(data_array == nodataval):
    data_array[data_array == nodataval] = np.nan
    
    
#Plot out data with Matplotlib's 'contour'
fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111)
plt.contour(data_array, cmap = "magma", 
            levels = list(range(0, 5000, 100)))
plt.title("Elevation Contours of Mt. Shasta")
# cbar = plt.colorbar()
plt.gca().set_aspect('equal', adjustable='box')
ax.set_ylim(ax.get_ylim()[::-1])

# plt.show()

#Plot our data with Matplotlib's 'contourf'
fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111)
plt.contourf(data_array, cmap = "viridis", 
            levels = list(range(0, 5000, 500)))
plt.title("Elevation Contours of Mt. Shasta")
# cbar = plt.colorbar()
plt.gca().set_aspect('equal', adjustable='box')
ax.set_ylim(ax.get_ylim()[::-1])

plt.show()