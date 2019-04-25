import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from input_parameters import bccoat, bccooc, dxo, dxa, fnot
import utils as utils

datapath = '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_b/'

# Files that describe oceanic and atmospheric state
atpa = nc.Dataset(datapath + 'atpa.nc')
ocpo = nc.Dataset(datapath + 'ocpo.nc')

p_ = ocpo.variables['p'][:, :, :, :]

time = p_.shape[0] # total time

writer = ani.ImageMagickWriter()

for i in range(2):
    if i == 0:
        p_ = ocpo.variables['p'][:, :, :, :]
        dx = dxo
        alpha = bccooc*dx
    else:
        p_ = atpa.variables['p'][:, :, :, :]
        dx = dxa
        alpha = bccoat*dx

    for j in range(3):
        p = utils.Pressure(p_[:, j, :, :])
        # u = p.zonal(i, alpha, dx, fnot)
        # v = p.meridional(i, alpha, dx, fnot)
        s = p.speed(i, alpha, dx, fnot)

        # [fig1, ax1] = u.init_frame()
        # [fig2, ax2] = v.init_frame()
        [fig3, ax3] = s.init_frame()
        # anim1 = ani.FuncAnimation(fig1, u.frame_i, frames=time)
        # anim2 = ani.FuncAnimation(fig2, v.frame_i, frames=time)
        anim3 = ani.FuncAnimation(fig3, s.frame_i, frames=time)
        if i == 0:
            # anim1.save('/rds/general/user/rk2014/home/WORK/q-gcm/post_process/vel_videos/u'+str(j+1)+'_oc.gif', writer=writer)
            # anim2.save('/rds/general/user/rk2014/home/WORK/q-gcm/post_process/vel_videos/v'+str(j+1)+'_oc.gif',writer=writer)
            anim3.save('/rds/general/user/rk2014/home/WORK/q-gcm/post_process/vel_videos/s'+str(j+1)+'_oc_b.gif',writer=writer)
        else:
            # anim1.save('/rds/general/user/rk2014/home/WORK/q-gcm/post_process/vel_videos/u'+str(j+1)+'_at.gif', writer = writer)
            # anim2.save('/rds/general/user/rk2014/home/WORK/q-gcm/post_process/vel_videos/v'+str(j+1)+'_at.gif', writer=writer)
            anim3.save('/rds/general/user/rk2014/home/WORK/q-gcm/post_process/vel_videos/s'+str(j+1)+'_at_b.gif',writer=writer)
