import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
# from input_parameters import rhoat, rhooc, fnot
import utils as utils

datapath = '/Users/rk2014/Documents/q-gcm/src/outdata/'

# Files that describe oceanic and atmospheric state
atast = nc.Dataset(datapath + 'atast.nc')
ocsst = nc.Dataset(datapath + 'ocsst.nc')

ast = atast.variables['ast']
sst = ocsst.variables['sst']

time = ast.shape[0] # total time
savepath = '/Users/rk2014/Documents/q-gcm/post-process/snapshots/'
for i in range(2):
    if i == 0:
        name = 'sst'
        sst = utils.ContourData(sst[:, :, :], name=name)
        [fig, ax] = sst.init_frame('SST ($K$)', True)
        sst.take_snapshots(10, 1, savepath, True)
    else:
        name = 'ast'
        ast = utils.ContourData(ast[:, :, :], name=name)
        [fig, ax] = ast.init_frame('AST ($K$)', False)
        ast.take_snapshots(10, 1, savepath, False)
