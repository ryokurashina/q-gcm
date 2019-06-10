import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
# from input_parameters import rhoat, rhooc, fnot
import utils as utils

datapath = '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_toptest/2/'
writer = ani.ImageMagickWriter()

# Files that describe oceanic and atmospheric state
atpa = nc.Dataset(datapath + 'atpa.nc')
ocpo = nc.Dataset(datapath + 'ocpo.nc')

q_oc = np.array(ocpo.variables['q'][:,:,:,:])
q_at = np.array(atpa.variables['q'][:, :, :, :])

time = q_oc.shape[0] # total time

for i in range(2):
    for j in range(3):
        if i == 0:
            q = utils.ContourData(q_oc[:,j,:,:])
        else:
            q = utils.ContourData(q_at[:,j,:,:])
        if i == 0:
            [fig, ax] = q.init_frame('Potential Vorticity ($s^{-1}$)', True)
            anim = ani.FuncAnimation(fig, q.frame_i, frames=time)
            anim.save('./pv'+str(j+1)+'_oc_b.gif', writer=writer)
        else:
            [fig, ax] = q.init_frame('Potential Vorticity ($s^{-1}$)', False)
            anim = ani.FuncAnimation(fig, q.frame_i, frames=time)
            anim.save('./pv'+str(j+1)+'_at_b.gif', writer=writer)
