import numpy as np
import matplotlib.pyplot as plt

G = 6.67 * (10**-11)

M = 5.988 * (10**24)

a = (6370 * 1000)

g0 = (G*M)/(a**2)

z = np.arange(0,52000,2000)

g = g0 * 1/(1 + (z/a))**2

relative_error = (9.84 - g)/g

above_error = np.where(relative_error > 0.01)

bad_height = z[16]

print(bad_height)

plt.plot(relative_error, z)

plt.title('Relative Error Plot')

plt.xlabel('Relative Error')

plt.ylabel('Height (Meters)')

plt.savefig('Relative_Error')

# It is an over estimate because we have 9.84 instead of 9.81.