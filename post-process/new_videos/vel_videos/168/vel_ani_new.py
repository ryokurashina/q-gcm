import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from input_parameters import bccoat, bccooc, dxo, dxa, fnot
import utils as utils

datapath = '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_updated_a/'
writer = ani.ImageMagickWriter()
savepath = '/rds/general/user/rk2014/home/WORK/q-gcm/post_process/vel_videos/'

# Files that describe oceanic and atmospheric state
atpa = nc.Dataset(datapath + 'atpa.nc')
ocpo = nc.Dataset(datapath + 'ocpo.nc')

p_ = ocpo.variables['p'][:, :, :, :]

time = p_.shape[0] # total time

# 0 for zonal, 1 for meridional, 2 for speed
variable = 1

for i in range(1,2):
    for j in range(3):

        if i == 0:
            p_ = ocpo.variables['p'][:, :, :, :]
            dx = dxo
            # Dimensionalise alpha
            alpha = bccooc/dx
            p = utils.Pressure(p_[:, j, :, :])
            if variable == 0:
                u = p.zonal(i, alpha, dx, fnot)
                [fig, ax] = u.init_frame('Zonal Velocity ($ms^{-1}$)', True)
                anim = ani.FuncAnimation(fig, u.frame_i, frames=time)
                anim.save('./u'+str(j+1)+'_oc_a.gif', writer=writer)
            elif variable == 1:
                v = p.meridional(i, alpha, dx, fnot)
                [fig, ax] = v.init_frame('Meridional Velocity ($ms^{-1}$)', True)
                anim = ani.FuncAnimation(fig, v.frame_i, frames=time)
                anim.save('./v'+str(j+1)+'_oc_a.gif', writer=writer)
            else:
                s = p.speed(i, alpha, dx, fnot)
                [fig, ax] = s.init_frame('Speed ($ms^{-1}$)', True)
                anim = ani.FuncAnimation(fig, s.frame_i, frames=time)
                anim.save('./s'+str(j+1)+'_oc_a.gif', writer=writer)

        else:
            p_ = atpa.variables['p'][:, :, :, :]
            dx = dxa
            # Dimensionalise alpha
            alpha = bccoat/dx
            p = utils.Pressure(p_[:, j, :, :])
            if variable == 0:
                u = p.zonal(i, alpha, dx, fnot)
                [fig, ax] = u.init_frame('Zonal Velocity ($ms^{-1}$)', False)
                anim = ani.FuncAnimation(fig, u.frame_i, frames=time)
                anim.save('./u'+str(j+1)+'_at_a.gif', writer=writer)
            elif variable == 1:
                v = p.meridional(i, alpha, dx, fnot)
                [fig, ax] = v.init_frame('Meridional Velocity ($ms^{-1}$)', False)
                anim = ani.FuncAnimation(fig, v.frame_i, frames=time)
                anim.save('./v'+str(j+1)+'_at_a.gif', writer=writer)
            else:
                s = p.speed(i, alpha, dx, fnot)
                [fig, ax] = s.init_frame('Speed ($ms^{-1}$)', False)
                anim = ani.FuncAnimation(fig, s.frame_i, frames=time)
                anim.save('./s'+str(j+1)+'_at_a.gif', writer=writer)
