from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np

ncfile = 'inso30k.nc'

data = Dataset(ncfile, mode = 'r')

lats = data.variables['lat'][:]

day = data.variables['jday'][:]

inso = data.variables['inso'][:,:,22]

Jan = day[16]

Feb = day[43]

Mar = day[71]

Apr = day[99]

May = day[127]

Jun = day[155]

Jul = day[183]

Aug = day[211]

Sep = day[239]

Oct = day[267]

Nov = day[295]

Dec = day[323]

months = Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec

inso = np.transpose(inso)

levels = [0,50,100,150,200,250,300,350,400,450,500,550]

plt.contour(day, lats, inso, cmap = 'jet', levels = levels)

plt.xticks(months, labels = ('J','F','M','A','M','J','J','A','S','O','N','D'))

plt.colorbar(drawedges=True, 
             ticks = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550],
             label = ('Radiation'))

plt.title('Top of Atmosphere Radiation 8000 Years Ago')

plt.ylabel('Latitude')

plt.xlabel('Months')

plt.savefig('Radiation 8000 Years Ago')

###########################################################################

inso2 = inso

inso2 = np.squeeze(inso2)

a = (6.37*10**6)

latr = lats * (np.pi/180)

radius = a * np.cos(latr)

A = 2*np.pi*radius

So = np.mean(inso2,1)

avg_rad = (np.sum(So * A))/np.sum(A)

print(avg_rad) 