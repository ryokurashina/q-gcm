import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from input_parameters import bccoat, bccooc, dxo, dxa, fnot
import utils as utils

datapath = '/Users/rk2014/Documents/q-gcm/src/outdata/'

# Files that describe oceanic and atmospheric state
atpa = nc.Dataset(datapath + 'atpa.nc')
ocpo = nc.Dataset(datapath + 'ocpo.nc')

p_ = ocpo.variables['p'][:, :, :, :]

time = p_.shape[0] # total time

# 0 for zonal, 1 for meridional, 2 for speed
variable = 2

for i in range(2):
    if i == 0:
        p_ = ocpo.variables['p'][:, :, :, :]
        dx = dxo
        # Dimensionalise alpha
        alpha = bccooc/dx
    else:
        p_ = atpa.variables['p'][:, :, :, :]
        dx = dxa
        # Dimensionalise alpha
        alpha = bccoat/dx

    for j in range(3):

        p = utils.Pressure(p_[:, j, :, :])
        if variable == 0:
            u = p.zonal(i, alpha, dx, fnot)
        elif variable == 1:
            v = p.meridional(i, alpha, dx, fnot)
        else:
            s = p.speed(i, alpha, dx, fnot)

        if i == 0:
            if variable == 0:
                [fig, ax] = u.init_frame('Zonal Velocity ($ms^{-1}$)', True)
                anim = ani.FuncAnimation(fig, u.frame_i, frames=time)
                anim.save('/Users/rk2014/Documents/q-gcm/post-process/u'+str(j+1)+'_oc.mp4')
            elif variable == 1:
                [fig, ax] = v.init_frame('Meridional Velocity ($ms^{-1}$)', True)
                anim = ani.FuncAnimation(fig, v.frame_i, frames=time)
                anim.save('/Users/rk2014/Documents/q-gcm/post-process/v'+str(j+1)+'_oc.mp4')
            else:
                [fig, ax] = s.init_frame('Speed ($ms^{-1}$)', True)
                anim = ani.FuncAnimation(fig, s.frame_i, frames=time)
                anim.save('/Users/rk2014/Documents/q-gcm/post-process/s'+str(j+1)+'_oc.mp4')
        else:
            if variable == 0:
                [fig, ax] = u.init_frame('Zonal Velocity ($ms^{-1}$)', False)
                anim = ani.FuncAnimation(fig, u.frame_i, frames=time)
                anim.save('/Users/rk2014/Documents/q-gcm/post-process/u'+str(j+1)+'_at.mp4')
            elif variable == 1:
                [fig, ax] = v.init_frame('Meridional Velocity ($ms^{-1}$)', False)
                anim = ani.FuncAnimation(fig, v.frame_i, frames=time)
                anim.save('/Users/rk2014/Documents/q-gcm/post-process/v'+str(j+1)+'_at.mp4')
            else:
                [fig, ax] = s.init_frame('Speed ($ms^{-1}$)', False)
                anim = ani.FuncAnimation(fig, s.frame_i, frames=time)
                anim.save('/Users/rk2014/Documents/q-gcm/post-process/s'+str(j+1)+'_at.mp4')
