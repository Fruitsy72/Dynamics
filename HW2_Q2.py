import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

file_loc = 'C:/Users/fmanf/OneDrive/Documents/Dynamics/Homework 2/'

ncfile = 'shum.mon.ltm.nc'

name = file_loc + ncfile

data = xr.open_dataset(name, decode_times=True)

# Level, Lat, Lon, Time, Climatology_bounds, Shum, Valid_yr_count

zone_mean = data.mean(dim = 'lon')

year_mean = zone_mean.mean(dim = 'time')

plot = np.asarray(year_mean.to_array())[0]

maxq = np.max(plot)

minq = np.min(plot)

interval = np.arange(minq,maxq+1,1)

lat = list(data.lat.values)

level = list(data.level.values)

plt.gca().invert_yaxis()

plt.contour(lat, level, plot, levels = interval, cmap = 'jet')

plt.colorbar()

plt.title('Annual Zonal Average Specific Humidity')

plt.xlabel('Latitude')

plt.ylabel('Pressure')

plt.savefig('AnnualZonalAverageShum')