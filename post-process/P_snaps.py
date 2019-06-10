import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from input_parameters import fnot
import utils as utils

datapath = '/Users/rk2014/Documents/q-gcm/src/outdata/'

# Files that describe oceanic and atmospheric state
atpa = nc.Dataset(datapath + 'atpa.nc')
ocpo = nc.Dataset(datapath + 'ocpo.nc')

steps = [0, 1]

p_oc = ocpo.variables['p'][:, :, :, :]
p_at = atpa.variables['p'][:, :, :, :]

f0 = fnot

savepath = '/Users/rk2014/Documents/q-gcm/post-process/snapshots/'
for i in range(2):
    for j in range(3):
        if i == 0:
            name = 'P_oc'+'_a_'+str(j+1)
            p = utils.ContourData(p_oc[:, j, :, :], name=name)
            [fig, ax] = p.init_frame('Pressure ($m^2s^{-2}$)', True)
            p.take_snapshots(1, 1, savepath, True)
        else:
            name = 'P_at'+'_a_'+str(j+1)
            p = utils.ContourData(p_at[:, j, :, :], name=name)
            [fig, ax] = p.init_frame('Pressure ($m^2s^{-2}$)', False)
            p.take_snapshots(1, 1, savepath, False)
