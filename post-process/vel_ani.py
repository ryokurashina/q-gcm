import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from input_parameters import bccoat, bccooc, dxo, dxa, fnot, rhooc, rhoat
import utils as utils

datapath = '/Users/rk2014/Documents/q-gcm/src/outdata/'

# Files that describe oceanic and atmospheric state
atpa = nc.Dataset(datapath + 'atpa.nc')
ocpo = nc.Dataset(datapath + 'ocpo.nc')

p_ = ocpo.variables['p'][:, :, :, :]

time = p_.shape[0] # total time



for i in range(2):
    if i == 0:
        p_ = ocpo.variables['p'][:, :, :, :]
        dx = dxo
        alpha = bccooc*dx
        rho = rhooc
    else:
        p_ = atpa.variables['p'][:, :, :, :]
        dx = dxa
        alpha = bccoat*dx
        rho = rhoat
    for j in range(3):
        p = utils.Pressure(p_[:, j, :, :])
        [u, v] = p.velocities(i, alpha, dx, rho, fnot)

        [fig1, ax1] = u.init_frame()
        # [fig2, ax2] = v.init_frame()
        anim1 = ani.FuncAnimation(fig1, u.frame_i, frames=time)
        # anim2 = ani.FuncAnimation(fig2, v.frame_i, frames=time)
        if i == 0:
            anim1.save('/Users/rk2014/Documents/q-gcm/post-process/u'+str(j+1)+'_oc.mp4')
            # anim2.save('/Users/rk2014/Documents/q-gcm/post-process/v'+str(j+1)+'_oc.mp4')
        else:
            anim1.save('/Users/rk2014/Documents/q-gcm/post-process/u'+str(j+1)+'_at.mp4')
            # anim2.save('/Users/rk2014/Documents/q-gcm/post-process/v'+str(j+1)+'_at.mp4')
