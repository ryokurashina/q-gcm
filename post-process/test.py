import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from math import pi
# from input_parameters import rhoat, rhooc, fnot
# import utils as utils

datapath = '/Users/rk2014/Documents/q-gcm/post-process/'
savepath = '/Users/rk2014/Documents/q-gcm/post-process/new_snapshots/topography/'
topog = np.array(nc.Dataset(datapath + 'topog.nc')['dtopat'])

# yla = 7680
# x = np.linspace(0, 30720, 1537)
# y = np.linspace(-3840, 3840, 385)
#
# dc = 8800
# dw = 1440
#
# xc = dc*np.ones_like(y)-2000*y/(0.5*yla)
# D = np.zeros((x.shape[0],y.shape[0]))
# for i in range(len(x)):
#     for j in range(len(y)):
#         D[i, j] = 1000*(1-abs(x[i]-xc[j])/dw)
#
# D[D<0] = 0
# print(topog.shape)
# plt.figure()
# plt.contourf(topog)
# plt.colorbar()
# plt.show()
#
# plt.figure()
# plt.contourf(np.transpose(D))
# plt.colorbar()
# plt.show()
#
# plt.figure()
# plt.contourf(topog-np.transpose(D))
# plt.colorbar()
# plt.show()


def add_ocean():
    x = np.linspace(648, 888, 241)
    y = np.linspace(72, 312, 241)
    # Bottom wall
    plt.plot(x, 72*np.ones_like(x),'k--')
    # Left wall
    plt.plot(648*np.ones_like(y), y,'k--')
    # Top wall
    plt.plot(x, 312*np.ones_like(x),'k--')
    # Right wall
    plt.plot(888*np.ones_like(y), y,'k--')

xc = 10340
yc = 3840
x = np.linspace(0, 30720, 1537)
y = np.linspace(-3840, 3840, 385)
D = np.zeros((1537,385))
R = 2600
for i in range(1536):
    for j in range(384):
        r = np.sqrt((x[i]-xc)**2+y[j]**2)
        if r <= R:
            D[i,j] = 500*np.cos(r*pi/(2*R))

plt.figure()
plt.contourf(np.transpose(D))
add_ocean()
plt.colorbar()
plt.show()
