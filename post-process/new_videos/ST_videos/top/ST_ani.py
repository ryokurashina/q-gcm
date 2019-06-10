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
atast = nc.Dataset(datapath + 'atast.nc')
ocsst = nc.Dataset(datapath + 'ocsst.nc')

ast = atast.variables['ast']
sst = ocsst.variables['sst']

time = ast.shape[0] # total time

for i in range(2):
    if i == 0:
        ast = utils.ContourData(ast[:, :, :])
        [fig, ax] = ast.init_frame('AST ($K$)', False)
        anim = ani.FuncAnimation(fig, ast.frame_i, frames=time)
        anim.save('./ast_b.gif', writer=writer)
    else:
        sst = utils.ContourData(sst[:, :, :])
        [fig, ax] = sst.init_frame('SST ($K$)', True)
        anim = ani.FuncAnimation(fig, sst.frame_i, frames=time)
        anim.save('./sst_b.gif', writer=writer)
