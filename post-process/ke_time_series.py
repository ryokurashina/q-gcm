import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
import utils as utils

datapath = '/Users/rk2014/Documents/q-gcm/post-process/'

# Number of times code has been run
N = 2
monit = nc.Dataset(datapath + 'monit1.nc')
print(monit['kealoc'].shape)
length = monit['kealat'].shape[0]
ke_at = np.zeros((length*N, monit['kealat'].shape[1]))
ke_oc = np.zeros((length*N, monit['kealat'].shape[1]))

time = [i for i in range(N*length)]
units_at = monit['kealat'].units
units_oc = monit['kealoc'].units

for i in range(N):
    monit = nc.Dataset(datapath + 'monit' + str(i+1) +'.nc')
    ke_at[i*length:(i+1)*length, :] = np.array(monit['kealat'])
    ke_oc[i*length:(i+1)*length, :] = np.array(monit['kealoc'])

for j in range(2):
    plt.figure()
    for k in range(3):
        if j == 0:
            ke = utils.TimeSeriesData(time, ke_at[:, k],name='Layer '+str(k+1))
            plt.xlabel('Time (Days)')
            plt.ylabel('Average Kinetic Energy (' + units_at + ')')
            ke.time_series_plot()
        else:
            ke = utils.TimeSeriesData(time, ke_oc[:, k],name='Layer '+str(k+1))
            plt.xlabel('Time (Days)')
            plt.ylabel('Average Kinetic Energy (' + units_oc + ')')
            ke.time_series_plot()
    if j == 0:
        plt.legend(loc='upper right')
        plt.savefig('./KE_time_series_at.png')
    else:
        plt.legend(loc='upper left')
        plt.savefig('./KE_time_series_oc.png')
