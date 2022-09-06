from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np


ncfile = 'inso30k.nc'

data = Dataset(ncfile, mode = 'r')

lats = data.variables['lat'][:]

day = data.variables['jday'][:]

inso = data.variables['inso'][:,:,22]

std = np.std(inso, axis = 0)

max = np.max(std)

print(max)

plt.plot(lats, std)

plt.ylabel('Standard Deviation')

plt.xlabel('Latitude')

plt.savefig('Standard Deviation (8000 years ago)')

#The rotation of the earth is more of a circular shape now so we receive a 
#more consistent amount of radiation than what we did 8000 years ago.