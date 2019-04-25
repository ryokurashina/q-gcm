import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from input_parameters import rhoat, rhooc, fnot, bccooc, bccoat, dxa, dxo
import utils as utils

datapath = '/Users/rk2014/Documents/q-gcm/src/outdata/'

# Files that describe oceanic and atmospheric state
atpa = nc.Dataset(datapath + 'atpa.nc')
ocpo = nc.Dataset(datapath + 'ocpo.nc')

# p_oc = utils.Pressure(ocpo.variables['p'][::10, :, :, :])
# p_at = utils.Pressure(atpa.variables['p'][::10, :, :, :])

# time = q_oc.shape[0] # total time
savepath = '/Users/rk2014/Documents/q-gcm/post-process/snapshots/'
variable = 2
for i in range(2):
    for j in range(3):
        if i == 0:
            dx = dxo
            # Dimensionalise alpha
            alpha = bccooc/dx
            p_oc = utils.Pressure(ocpo.variables['p'][::10, j, :, :])
            if variable == 0:
                name = 'u_oc'+'_'+str(j+1)
                u = utils.ContourData(p_oc.zonal(0, alpha, dx, fnot).data, name=name)
                [fig, ax] = u.init_frame('Zonal Velocity ($ms^{-1}$)', True)
                u.take_snapshots(1, 1, savepath, True)
            elif variable == 1:
                name = 'v_oc'+'_'+str(j+1)
                v = utils.ContourData(p_oc.meridional(0, alpha, dx, fnot).data, name=name)
                [fig, ax] = v.init_frame('Meridional Velocity ($ms^{-1}$)', True)
                v.take_snapshots(1, 1, savepath, True)
            else:
                name = 's_oc'+'_'+str(j+1)
                s = utils.ContourData(p_oc.speed(0, alpha, dx, fnot).data, name=name)
                [fig, ax] = s.init_frame('Speed ($ms^{-1}$)', True)
                s.take_snapshots(1, 1, savepath, True)
        else:
            dx = dxa
            # Dimensionalise alpha
            alpha = bccoat/dx
            p_at = utils.Pressure(atpa.variables['p'][::10, j, :, :])
            if variable == 0:
                name = 'u_at'+'_'+str(j+1)
                u = utils.ContourData(p_at.zonal(1, alpha, dx, fnot).data, name=name)
                [fig, ax] = u.init_frame('Zonal Velocity ($ms^{-1}$)', False)
                u.take_snapshots(1, 1, savepath, False)
            elif variable == 1:
                name = 'v_at'+'_'+str(j+1)
                v = utils.ContourData(p_at.meridional(1, alpha, dx, fnot).data, name=name)
                [fig, ax] = v.init_frame('Zonal Velocity ($ms^{-1}$)', False)
                v.take_snapshots(1, 1, savepath, False)
            else:
                name = 's_at'+'_'+str(j+1)
                s = utils.ContourData(p_at.speed(1, alpha, dx, fnot).data, name=name)
                [fig, ax] = s.init_frame('Zonal Velocity ($ms^{-1}$)', False)
                s.take_snapshots(1, 1, savepath, False)
