import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
import utils as utils

datapath = '/Users/rk2014/Documents/q-gcm/post-process/210/a/'

# Number of times code has been run
N = 1
monit = nc.Dataset(datapath + 'monit.nc')
# print(monit.variables)
length = monit['ugminoc'].shape[0]

ug_min_at = np.zeros((length*N, monit['ugminat'].shape[1]))
ug_max_at = np.zeros((length*N, monit['ugmaxat'].shape[1]))
ug_min_oc = np.zeros((length*N, monit['ugminoc'].shape[1]))
ug_max_oc = np.zeros((length*N, monit['ugminat'].shape[1]))

vg_min_at = np.zeros((length*N, monit['kealat'].shape[1]))
vg_max_at = np.zeros((length*N, monit['kealat'].shape[1]))
vg_min_oc = np.zeros((length*N, monit['kealat'].shape[1]))
vg_max_oc = np.zeros((length*N, monit['kealat'].shape[1]))

time = [i for i in range(N*length)]
units = monit['ugminat'].units


for i in range(N):
    # monit = nc.Dataset(datapath + 'monit' + str(i+1) +'.nc')
    monit = nc.Dataset(datapath + 'monit.nc')

    ug_min_at[i*length:(i+1)*length, :] = np.array(monit['ugminat'])
    ug_max_at[i*length:(i+1)*length, :] = np.array(monit['ugmaxat'])
    ug_min_oc[i*length:(i+1)*length, :] = np.array(monit['ugminoc'])
    ug_max_oc[i*length:(i+1)*length, :] = np.array(monit['ugmaxoc'])

    vg_min_at[i*length:(i+1)*length, :] = np.array(monit['vgminat'])
    vg_max_at[i*length:(i+1)*length, :] = np.array(monit['vgmaxat'])
    vg_min_oc[i*length:(i+1)*length, :] = np.array(monit['vgminoc'])
    vg_max_oc[i*length:(i+1)*length, :] = np.array(monit['vgmaxoc'])

for j in range(4):
    plt.figure()
    for k in range(3):
        if j == 0:
            ug_min = utils.TimeSeriesData(time, ug_min_at[:, k],name='Minimum u (Atmospheric Layer '+str(k+1)+')')
            ug_max = utils.TimeSeriesData(time, ug_max_at[:, k],name='Maximum u (Atmospheric Layer '+str(k+1)+')')
            plt.xlabel('Time (Days)')
            plt.ylabel('Velocity (' + units + ')')
            ug_min.time_series_plot()
            ug_max.time_series_plot()
        elif j == 1:
            vg_min = utils.TimeSeriesData(time, vg_min_at[:, k],name='Minimum v (Atmospheric Layer '+str(k+1)+')')
            vg_max = utils.TimeSeriesData(time, vg_max_at[:, k],name='Maximum v (Atmospheric Layer '+str(k+1)+')')
            plt.xlabel('Time (Days)')
            plt.ylabel('Velocity (' + units + ')')
            vg_min.time_series_plot()
            vg_max.time_series_plot()
        elif j == 2:
            ug_min = utils.TimeSeriesData(time, ug_min_oc[:, k],name='Minimum u (Oceanic Layer '+str(k+1)+')')
            ug_max = utils.TimeSeriesData(time, ug_max_oc[:, k],name='Maximum u (Oceanic Layer '+str(k+1)+')')
            plt.xlabel('Time (Days)')
            plt.ylabel('Velocity (' + units + ')')
            ug_min.time_series_plot()
            ug_max.time_series_plot()
        else:
            vg_min = utils.TimeSeriesData(time, vg_min_oc[:, k],name='Minimum v (Oceanic Layer '+str(k+1)+')')
            vg_max = utils.TimeSeriesData(time, vg_max_oc[:, k],name='Maximum v (Oceanic Layer '+str(k+1)+')')
            plt.xlabel('Time (Days)')
            plt.ylabel('Velocity (' + units + ')')
            vg_min.time_series_plot()
            vg_max.time_series_plot()
    if j == 0:
        plt.legend(loc='upper right')
        plt.savefig('/Users/rk2014/Documents/q-gcm/post-process/210/a/u_time_series_at.png')
    elif j == 1:
        plt.legend(loc='upper left')
        plt.savefig('/Users/rk2014/Documents/q-gcm/post-process/210/a/v_time_series_at.png')
    elif j == 2:
        plt.legend(loc='upper right')
        plt.savefig('/Users/rk2014/Documents/q-gcm/post-process/210/a/u_time_series_oc.png')
    else:
        plt.legend(loc='upper left')
        plt.savefig('/Users/rk2014/Documents/q-gcm/post-process/210/a/v_time_series_oc.png')
