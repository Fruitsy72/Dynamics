import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

file_loc = 'C:/Users/fmanf/OneDrive/Documents/Dynamics/Homework 1/'

ncfile = 'air.mon.ltm.nc'

name = file_loc + ncfile

data = xr.open_dataset(name, decode_times=True)

# Level, Lat, Lon, Time, Climatology_bounds, Air, Valid_yr_count

pres_lev = [1000,925,850,700,600,500,400,300,250,200,150,100]

month = np.where(data.time.dt.month.values==10)[0][0]

month_data = data.isel(time=month)

level_data = month_data.sel(level = pres_lev).drop(['time','valid_yr_count','climatology_bounds'])

mean_temp = level_data.mean(dim='lon')

plot = np.asarray(mean_temp.to_array())[0]

latitude = list(data.lat.values)

pressure = list(mean_temp.level.values)

level = [-70, -60, -50, -40, -30, -20, -10, 0, 10, 20]

plt.contour(latitude, pressure, plot, cmap = 'jet', levels = level)

plt.gca().invert_yaxis()

plt.colorbar(label = 'Temperature')

plt.xlabel('Latitude')

plt.ylabel('Pressure Levels')

plt.title('Annual Zonal Mean Temperature')

plt.savefig('Average Temp')