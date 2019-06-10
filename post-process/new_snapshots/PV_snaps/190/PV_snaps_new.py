import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
# from input_parameters import rhoat, rhooc, fnot
import utils as utils

datapath = '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_190_b/'

# Files that describe oceanic and atmospheric state
atpa = nc.Dataset(datapath + 'atpa.nc')
ocpo = nc.Dataset(datapath + 'ocpo.nc')

steps = [0, 36, 73, 109, 146, 182, 219, 255, 292, 328, 365]

q_oc = ocpo.variables['q'][steps, :, :, :]
q_at = atpa.variables['q'][steps, :, :, :]

savepath = './'
for i in range(2):
    for j in range(3):
        if i == 0:
            name = 'PV_oc'+'_'+str(j+1)+'a_'
            q = utils.ContourData(q_oc[:, j, :, :], name=name)
            [fig, ax] = q.init_frame('Potential Vorticity ($s^{-1}$)', True)
            q.take_snapshots(1, 365, savepath, True)
        else:
            name = 'PV_at'+'_'+str(j+1)+'a_'
            q = utils.ContourData(q_at[:, j, :, :], name=name)
            [fig, ax] = q.init_frame('Potential Vorticity ($s^{-1}$)', False)
            q.take_snapshots(1, 365, savepath, False)
