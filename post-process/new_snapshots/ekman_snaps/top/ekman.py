import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
# from input_parameters import rhoat, rhooc, fnot
import utils as utils

datapath = '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_toptest/1/'
savepath='./'

ocsst = nc.Dataset(datapath + 'ocsst.nc')

steps = [0, 36, 73, 109, 146, 182, 219, 255, 292, 328, 365]
ek_vel = ocsst['wekt'][steps, :, :]
time = ek_vel.shape[0]

ek_av = np.einsum('ijk->jk',np.array(ocsst['wekt']))/time

name = 'ek_av_oc'
ek_av = utils.ContourData(ek_av[np.newaxis, :, :], name=name)
[fig, ax] = ek_av.init_frame('Ekman Velocity ($ms^{-1}$)', True)
ek_av.take_snapshots(1, 1, savepath, True)

name = 'ek_oc'
ek = utils.ContourData(ek_vel[:, :, :], name=name)
[fig, ax] = ek.init_frame('Ekman Velocity ($ms^{-1}$)', True)
ek.take_snapshots(1, 365, savepath, True)
