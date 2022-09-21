from pandas import read_csv
#import matplotlib.pyplot as plt

csv = read_csv('HW2.csv')

# print(csv)

Alt = csv['Altitude']

Temp = csv['Temperature']

Press = csv['Pressure']

Dens = csv['Density']

def math(height):
    temp = 0
    for i in range(len(csv)-1):
        temp1 = csv['Temperature'][i]
        temp2 = csv['Temperature'][i+1]
        avg_temp = (temp1 + temp2)/2
        delta_z = csv['Altitude'][i+1] - csv['Altitude'][i]
        temp += avg_temp * delta_z
    
        if csv['Altitude'][i+1] == height:
            return temp/height
    
temp12 = math(12)

temp32 = math(32)

print(temp12)

print(temp32)

##################################################################

Rd = 287

G = 9.8

scale_height12 = (Rd/G) * temp12

print(scale_height12)

scale_height32 = (Rd/G) * temp32

print(scale_height32)