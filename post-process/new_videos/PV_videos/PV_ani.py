import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
# from input_parameters import rhoat, rhooc, fnot
import utils as utils

plt.rcParams['animation.ffmpeg_path'] = '/rds/general/user/rk2014/home/anaconda3/envs/post-process/bin/ffmpeg'

datapath = '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_b/'

# Files that describe oceanic and atmospheric state
atpa = nc.Dataset(datapath + 'atpa.nc')
ocpo = nc.Dataset(datapath + 'ocpo.nc')

q_oc = ocpo.variables['q'][:, :, :, :]
q_at = atpa.variables['q'][:, :, :, :]

time = q_oc.shape[0] # total time
FFwriter = ani.ImageMagickWriter()

for i in range(2):
    for j in range(3):
        if i == 0:
            q = utils.ContourData(q_oc[:,j,:,:])
        else:
            q = utils.ContourData(q_at[:,j,:,:])
        [fig, ax] = q.init_frame()
        anim = ani.FuncAnimation(fig, q.frame_i, frames=time)

        if i == 0:
            anim.save('./pv'+str(j+1)+'_oc_b.gif',writer=FFwriter)
        else:
            anim.save('./pv'+str(j+1)+'_at_b.gif',writer=FFwriter)
