import matplotlib.pyplot as plt
import xarray as xr
import numpy as np

file_loc = 'C:/Users/fmanf/OneDrive/Documents/Dynamics/Homework 1/'

ncfile = 'air.mon.ltm.nc'

name = file_loc + ncfile

data = xr.open_dataset(name, decode_times=True)

temp = data.air.sel(level = slice(1000,200))

temp = temp + 273

for num in temp:
    theta = num * (1000/temp.level)**0.286
    
theta_mean = theta.mean(dim='lon')

lat = list(data.lat.values)

level = [1000,925,850,700,600,500,400,300,200,100]

theta_max = np.max(theta_mean)

theta_min = np.min(theta_mean)

interval = np.arange(theta_min, theta_max, 10)

plt.gca().invert_yaxis()

plt.contour(lat,level,theta_mean, levels = interval, cmap = 'jet')

plt.colorbar()

plt.xlabel('Latitude')

plt.ylabel('Pressure')

plt.title('Annual Zonal Average Potential Temperature')

plt.savefig('Potential_Temp')

# The troposphere is stable to dry convection