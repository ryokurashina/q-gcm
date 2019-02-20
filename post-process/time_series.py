import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
import utils as utils

datapath = '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_long/'

monit = nc.Dataset(datapath + 'monit.nc')
KE_at = monit['kealat']
KE_oc = monit['kealoc']
time = [i for i in range(KE_at.shape[0])]

for i in range(2):
    plt.figure()
    for j in range(3):
        if i == 0:
            KE = utils.TimeSeriesData(time, KE_at[:, j],name='Layer '+str(j+1))
            plt.xlabel('Time (Days)')
            plt.ylabel('Average Kinetic Energy (' + KE_at.units + ')')
            KE.time_series_plot()
        else:
            KE = utils.TimeSeriesData(time, KE_oc[:, j],name='Layer '+str(j+1))
            plt.xlabel('Time (Days)')
            plt.ylabel('Average Kinetic Energy (' + KE_oc.units + ')')
            KE.time_series_plot()
    if i == 0:
        plt.legend(loc='upper right')
        plt.savefig('./KE_time_series_at.png')
    if i == 1:
        plt.legend(loc='upper left')
        plt.savefig('./KE_time_series_oc.png')
