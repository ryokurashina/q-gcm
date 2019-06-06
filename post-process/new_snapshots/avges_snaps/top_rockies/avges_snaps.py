import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from input_parameters import rhoat, rhooc, fnot, bccooc, bccoat, dxa, dxo
import utils as utils

datapath = '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_toptest/1/'

# Files that describe average oceanic and atmospheric state
avges = nc.Dataset(datapath + 'avges.nc')

savepath = './'

#variable = 'zonal'
variable = 'meridional'
#variable = 'speed'

for i in range(2):
    for j in range(3):
        if i == 0:
            dx = dxo
            # Dimensionalise alpha
            alpha = bccooc/dx
            p_oc = np.array(avges.variables['po'][j, :, :])
            p_oc = utils.Pressure(p_oc[np.newaxis, :, :])
            if variable == 'zonal':
                name = 'u_oc_avge'+'_'+str(j+1)+'_a'
                u = utils.ContourData(p_oc.zonal(0, alpha, dx, fnot).data, name=name)
                [fig, ax] = u.init_frame('Zonal Velocity ($ms^{-1}$)', True)
                u.take_snapshots(1, 1, savepath, True)
            elif variable == 'meridional':
                name = 'v_oc_avge'+'_'+str(j+1)+'_a'
                v = utils.ContourData(p_oc.meridional(0, alpha, dx, fnot).data, name=name)
                [fig, ax] = v.init_frame('Meridional Velocity ($ms^{-1}$)', True)
                v.take_snapshots(1, 1, savepath, True)
            elif variable == 'speed':
                name = 's_oc_avge'+'_'+str(j+1)+'_a'
                s = utils.ContourData(p_oc.speed(0, alpha, dx, fnot).data, name=name)
                [fig, ax] = s.init_frame('Speed ($ms^{-1}$)', True)
                s.take_snapshots(1, 1, savepath, True)
        else:
            dx = dxa
            # Dimensionalise alpha
            alpha = bccoat/dx
            p_at = np.array(avges.variables['pa'][j, :, :])
            p_at = utils.Pressure(p_at[np.newaxis, :, :])
            if variable == 'zonal':
                name = 'u_at_avge'+'_'+str(j+1)+'_a'
                u = utils.ContourData(p_at.zonal(1, alpha, dx, fnot).data, name=name)
                [fig, ax] = u.init_frame('Zonal Velocity ($ms^{-1}$)', False)
                u.take_snapshots(1, 1, savepath, False)
            elif variable == 'meridional':
                name = 'v_at_avge'+'_'+str(j+1)+'_a'
                v = utils.ContourData(p_at.meridional(1, alpha, dx, fnot).data, name=name)
                [fig, ax] = v.init_frame('Zonal Velocity ($ms^{-1}$)', False)
                v.take_snapshots(1, 1, savepath, False)
            elif variable == 'speed':
                name = 's_at_avge'+'_'+str(j+1)+'_a'
                s = utils.ContourData(p_at.speed(1, alpha, dx, fnot).data, name=name)
                [fig, ax] = s.init_frame('Zonal Velocity ($ms^{-1}$)', False)
                s.take_snapshots(1, 1, savepath, False)
