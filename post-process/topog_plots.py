import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from input_parameters import rhoat, rhooc, fnot, bccooc, bccoat, dxa, dxo
import utils as utils

# datapath = ['/rds/general/user/rk2014/home/WORK/q-gcm/outdata_toptest/test/NA_atmos_only/', \
#              '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_toptest/test/rockies_atmos_only/', \
#              '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_toptest/test/apalachees_atmos_only/']

datapath = ['/Users/rk2014/Documents/q-gcm/src/outdata/', '/Users/rk2014/Documents/q-gcm/src/outdata/', \
             '/Users/rk2014/Documents/q-gcm/src/outdata/']

# Files that describe average oceanic and atmospheric state
avges = [nc.Dataset(datapath[i] + 'avges.nc') for i in range(3)]

#savepath = './'
savepath = '/Users/rk2014/Desktop/'

variable = 'zonal'
# variable = 'meridional'
# variable = 'speed'

# Ocean then atmosphere
for i in range(1):
    # For each layer
    for j in range(3):
        if i == 0:
            dx = dxo
            # Dimensionalise alpha
            alpha = bccooc/dx
            dim = np.array(avges[0].variables['po'][j, :, :]).shape
            p_oc = np.zeros((3, dim[0], dim[1]))
            for k in range(2):
                p_oc[k, :, :] = np.array(avges[k].variables['po'][j, :, :])
            # p_oc = np.array(avges.variables['po'][j, :, :])
            p_oc = utils.Pressure(p_oc[:, :, :])
            if variable == 'zonal':
                name = 'u_oc_avge'+'_'+str(j+1)
                u = utils.ContourData(p_oc.zonal(0, alpha, dx, fnot).data, name=name)
                [fig, ax] = u.init_frame('Zonal Velocity ($ms^{-1}$)', True)
                u.take_snapshots(1, 1, savepath, True)
            elif variable == 'meridional':
                name = 'v_oc_avge'+'_'+str(j+1)
                v = utils.ContourData(p_oc.meridional(0, alpha, dx, fnot).data, name=name)
                [fig, ax] = v.init_frame('Meridional Velocity ($ms^{-1}$)', True)
                v.take_snapshots(1, 1, savepath, True)
            elif variable == 'speed':
                name = 's_oc_avge'+'_'+str(j+1)
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
                name = 'u_at_avge'+'_'+str(j+1)
                u = utils.ContourData(p_at.zonal(1, alpha, dx, fnot).data, name=name)
                [fig, ax] = u.init_frame('Zonal Velocity ($ms^{-1}$)', False)
                u.take_snapshots(1, 1, savepath, False)
            elif variable == 'meridional':
                name = 'v_at_avge'+'_'+str(j+1)
                v = utils.ContourData(p_at.meridional(1, alpha, dx, fnot).data, name=name)
                [fig, ax] = v.init_frame('Zonal Velocity ($ms^{-1}$)', False)
                v.take_snapshots(1, 1, savepath, False)
            elif variable == 'speed':
                name = 's_at_avge'+'_'+str(j+1)
                s = utils.ContourData(p_at.speed(1, alpha, dx, fnot).data, name=name)
                [fig, ax] = s.init_frame('Zonal Velocity ($ms^{-1}$)', False)
                s.take_snapshots(1, 1, savepath, False)
