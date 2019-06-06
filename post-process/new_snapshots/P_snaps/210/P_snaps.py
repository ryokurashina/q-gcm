import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from input_parameters import fnot
import utils as utils

datapath = '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_210_b/'

# Files that describe oceanic and atmospheric state
atpa = nc.Dataset(datapath + 'atpa.nc')
ocpo = nc.Dataset(datapath + 'ocpo.nc')

steps = [0, 36, 73, 109, 146, 182, 219, 255, 292, 328, 365]

p_oc = ocpo.variables['p'][steps, :, :, :]
p_at = atpa.variables['p'][steps, :, :, :]

f0 = fnot

savepath = './'
for i in range(2):
    for j in range(3):
        if i == 0:
            name = 'P_oc'+'_b_'+str(j+1)
            p = utils.ContourData(p_oc[:, j, :, :], name=name)
            [fig, ax] = p.init_frame('Pressure ($m^2s^{-2}$)', True)
            p.take_snapshots(1, 365, savepath, True)
        else:
            name = 'P_at'+'_b_'+str(j+1)
            p = utils.ContourData(p_at[:, j, :, :], name=name)
            [fig, ax] = p.init_frame('Pressure ($m^2s^{-2}$)', False)
            p.take_snapshots(1, 365, savepath, False)
