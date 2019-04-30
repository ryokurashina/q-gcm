import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from input_parameters import fnot, hat, hoc
import utils as utils

datapath = '/Users/rk2014/Documents/q-gcm/src/outdata/'

# Files that describe oceanic and atmospheric state
atpa = nc.Dataset(datapath + 'atpa.nc')
ocpo = nc.Dataset(datapath + 'ocpo.nc')

p_oc = ocpo.variables['p'][:, :, :, :]
p_at = atpa.variables['p'][:, :, :, :]

H_at = [2000, 3000, 4000]
H_oc = [350, 750, 2900]

f0 = fnot

step = 10


# # time = q_oc.shape[0] # total time
savepath = '/Users/rk2014/Documents/q-gcm/post-process/snapshots/'

for i in range(2):
    for j in range(3):
        if i == 0:
            name = 'Sv_oc'+'_'+str(j+1)
            psi = utils.ContourData(p_oc[::step, j, :, :]*H_oc[j]/(f0*10**6), name=name)
            [fig, ax] = psi.init_frame('Transport (Sv)', True)
            psi.take_snapshots(1, step, savepath, True)
        else:
            name = 'Sv_at'+'_'+str(j+1)
            psi = utils.ContourData(p_at[::step, j, :, :]*H_at[j]/(f0*10**6), name=name)
            [fig, ax] = psi.init_frame('Transport (Sv)', False)
            psi.take_snapshots(1, step, savepath, False)
