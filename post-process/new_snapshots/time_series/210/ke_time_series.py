import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
import utils as utils

# Option is at or oc
option = 'at'

#datapath = ['/rds/general/user/rk2014/home/WORK/q-gcm/outdata_210_a/', '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_210_b/']
datapath = ['/rds/general/user/rk2014/home/WORK/q-gcm/outdata_final/1/']
# Number of times code has been run
N = len(datapath)
monit = nc.Dataset(datapath[0] + 'monit.nc')

if option == 'oc':
    length = monit['kealoc'].shape[0]
    ke_array = np.zeros((length*N, monit['kealoc'].shape[1]))
else:
    length = monit['kealat'].shape[0]
    ke_array = np.zeros((length*N, monit['kealat'].shape[1]))

time = [10*i for i in range(N*length)]
units = '$Jm^{-2}$'

for i in range(N):
    monit = nc.Dataset(datapath[i] + 'monit.nc')
    if option == 'oc':
        ke_array[i*length:(i+1)*length, :] = np.array(monit['kealoc'])
    else:
        ke_array[i*length:(i+1)*length, :] = np.array(monit['kealat'])


plt.figure()
for k in range(3):
    ke = utils.TimeSeriesData(time, ke_array[:, k],name='Layer '+str(k+1))
    plt.xlabel('Time (Days)')
    plt.ylabel('Average Kinetic Energy (' + units + ')')
    ke.time_series_plot()
    if option == 'oc':
        plt.legend(loc='upper left')
        plt.savefig('./KE_time_series_oc.png')
    else:
        plt.legend(loc='upper right')
        plt.savefig('./KE_time_series_at.png')
