import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

file_loc = 'C:/Users/fmanf/OneDrive/Documents/Dynamics/Homework 2/'

ncfile = 'shum.mon.ltm.nc'

name = file_loc + ncfile

data = xr.open_dataset(name, decode_times=True)

lat = list(data.lat.values)

level = list(data.level.values)

file2_loc = 'C:/Users/fmanf/OneDrive/Documents/Dynamics/Homework 1/'

ncfile2 = 'air.mon.ltm.nc'

name2 = file2_loc + ncfile2

data2 = xr.open_dataset(name2, decode_times=True)

same_level = data2.sel(level = level)

mix_ratio = ((data.shum/1000)/(1 - (data.shum/1000)))

datasets = xr.merge([data,same_level], join = 'exact')

R = datasets.assign(r = mix_ratio)

Tv = (R.air + 273) * (1 + (R.r/0.622))/(1 + R.r)

diff = R.assign(Tdiff = Tv - (R.air + 273))

zone_mean_diff = diff.mean(dim = 'lon')

year_mean_diff = zone_mean_diff.mean(dim = 'time')

variable = list(year_mean_diff.variables)

variable.remove('Tdiff')

difference = year_mean_diff.drop(variable)

plot2 = np.asarray(difference.to_array())[0]

plt.gca().invert_yaxis()

diffmin = np.min(plot2)

diffmax = np.max(plot2)

interval2 = np.arange(diffmin, diffmax, 0.2)

plt.contour(lat, level, plot2, levels  = interval2, cmap = 'jet')

plt.title('Virtual Temperature - Temperature')

plt.ylabel('Pressure')

plt.xlabel('Latitude')

plt.colorbar()

plt.savefig('Virtual_Temp_Difference')