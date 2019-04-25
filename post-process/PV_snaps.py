import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
# from input_parameters import rhoat, rhooc, fnot
import utils as utils

datapath = '/Users/rk2014/Documents/q-gcm/src/outdata/'

# Files that describe oceanic and atmospheric state
atpa = nc.Dataset(datapath + 'atpa.nc')
ocpo = nc.Dataset(datapath + 'ocpo.nc')

q_oc = ocpo.variables['q'][:, :, :, :]
q_at = atpa.variables['q'][:, :, :, :]

time = q_oc.shape[0] # total time
savepath = '/Users/rk2014/Documents/q-gcm/post-process/snapshots/'
for i in range(2):
    for j in range(3):
        if i == 0:
            name = 'PV_oc'+'_'+str(j+1)
            q = utils.ContourData(q_oc[:, j, :, :], name=name)
            [fig, ax] = q.init_frame('Potential Vorticity ($s^{-1}$)', True)
            q.take_snapshots(10, 1, savepath, True)
        else:
            name = 'PV_at'+'_'+str(j+1)
            q = utils.ContourData(q_at[:, j, :, :], name=name)
            [fig, ax] = q.init_frame('Potential Vorticity ($s^{-1}$)', False)
            q.take_snapshots(10, 1, savepath, False)
