import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
# from input_parameters import rhoat, rhooc, fnot
import utils as utils

datapath = '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_210_a/'

# Files that describe oceanic and atmospheric state
atast = nc.Dataset(datapath + 'atast.nc')
ocsst = nc.Dataset(datapath + 'ocsst.nc')

steps = [0, 36, 73, 109, 146, 182, 219, 255, 292, 328, 365]

ast = atast.variables['ast'][steps, :, :]
sst = ocsst.variables['sst'][steps, :, :]

time = ast.shape[0] # total time
savepath = './'
for i in range(2):

    if i == 0:
        name = 'sst_a_'
        sst = utils.ContourData(sst[:, :, :], name=name)
        [fig, ax] = sst.init_frame('SST ($K$)', True)
        sst.take_snapshots(1, 365, savepath, True)
    else:
        name = 'ast_a_'
        ast = utils.ContourData(ast[:, :, :], name=name)
        [fig, ax] = ast.init_frame('AST ($K$)', False)
        ast.take_snapshots(1, 365, savepath, False)
