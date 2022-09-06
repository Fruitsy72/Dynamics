from netCDF4 import Dataset
import matplotlib.pyplot as plt

ncfile = 'air.mon.ltm.nc'

data = Dataset(ncfile, mode = 'r')

air = data.variables['air'][:12,11,36,0]

level = data.variables['level'][11]

lat = data.variables['lat'][36]

plt.plot(air)

tick = [0,1,2,3,4,5,6,7,8,9,10,11]

label = 'J','F','M','A','M','J','J','A','S','O','N','D'

plt.xticks(ticks = tick, labels = label)

plt.xlabel('Months')

plt.ylabel('Temperature')

plt.title('Annual Cycle of Temperature at the Equator')

plt.savefig('100 mb Temp')

#It looks that the winter season is the coldest. This is because the equator
#more closely follows the Northern Hemisphere seasonality. 
#Because of this we know that the circulation is stronger
#in the Northern Hemisphere.