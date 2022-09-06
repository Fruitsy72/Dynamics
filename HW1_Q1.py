import matplotlib.pyplot as plt
import numpy as np


E1 = np.arange(0.0, 1.01, 0.01)

E2 = np.arange(0.0, 1.01, 0.01)

grid1,grid2 = np.meshgrid(E1,E2)

Ts = ((4-(grid1*grid2))/(2-grid1) * ((255**4)/(2-grid2)))**(1/4)

T1 = ((2+grid2-(grid1*grid2))/(2-grid1) * (255**4)/(2-grid2))**(1/4)

#plt.contourf(grid1, grid2, Ts, cmap = 'jet')

#plt.colorbar()
 
#plt.savefig('Surface Temperature')

plt.contourf(grid1, grid2, T1, cmap = 'jet')

plt.colorbar()

plt.savefig('Temperature for Layer 1')