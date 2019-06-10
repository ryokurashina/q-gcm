import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from input_parameters import fnot, hat, hoc
import utils as utils

datapath = '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_190_b/'

# Files that describe oceanic and atmospheric state
atpa = nc.Dataset(datapath + 'atpa.nc')
ocpo = nc.Dataset(datapath + 'ocpo.nc')

steps = [0, 36, 73, 109, 146, 182, 219, 255, 292, 328, 365]

p_oc = ocpo.variables['p'][steps, :, :, :]
p_at = atpa.variables['p'][steps, :, :, :]

H_at = [2000, 3000, 4000]
H_oc = [350, 750, 2900]

f0 = fnot

savepath = './'

for i in range(2):
    for j in range(3):
        if i == 0:
            name = 'Sv_oc'+'_a_'+str(j+1)
            psi = utils.ContourData(p_oc[:, j, :, :]*H_oc[j]/(f0*10**6), name=name)
            [fig, ax] = psi.init_frame('Layer Transport (Sv)', True)
            psi.take_snapshots(1, 365, savepath, True)
        else:
            name = 'Sv_at'+'_a_'+str(j+1)
            psi = utils.ContourData(p_at[:, j, :, :]*H_at[j]/(f0*10**6), name=name)
            [fig, ax] = psi.init_frame('Layer Transport (Sv)', False)
            psi.take_snapshots(1, 365, savepath, False)
