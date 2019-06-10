import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import cm
# import utils as utils

# plt.rcParams.update({'font.size': 14})
# rc('text', usetex=True)

datapath = '/Users/rk2014/Documents/q-gcm/post-process/'
savepath = '/Users/rk2014/Documents/q-gcm/post-process/new_snapshots/topography/'
topog = nc.Dataset(datapath + 'topog.nc')['dtopat']


def add_ocean():
    # 80km atmosphere
    x_start = 162
    y_start = 18
    dim = 60
    # 20 km atmosphere
    # x_start = 648
    # y_start 72
    # dim = 240
    x = np.linspace(x_start, x_start+dim, 241)
    y = np.linspace(y_start, y_start+dim, 241)
    # Bottom wall
    plt.plot(x, x_start*np.ones_like(x),'k--')
    # Left wall
    plt.plot(y_start*np.ones_like(y), y,'k--')
    # Top wall
    plt.plot(x, (x_start+dim)*np.ones_like(x),'k--')
    # Right wall
    plt.plot(y_start+dim*np.ones_like(y), y,'k--')


plt.figure()
plt.contourf(topog[:])
plt.colorbar()
plt.show()


# top = np.array(topog)
# print(top.shape)
# name = 'atmos_topog'
# top = utils.ContourData(top[np.newaxis, :, :], name=name)
#
#
# [fig, ax] = top.init_frame('Height ($m$)', False)
# top.take_snapshots(1, 1, savepath, False)
