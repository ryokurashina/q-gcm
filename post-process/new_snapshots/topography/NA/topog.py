import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import cm
import utils as utils

# plt.rcParams.update({'font.size': 14})
# rc('text', usetex=True)

datapath = '/rds/general/user/rk2014/home/WORK/q-gcm/outdata_toptest/test/NA_atmos_only/'
savepath = './'
topog = nc.Dataset(datapath + 'topog.nc')['dtopat']

# plt.figure()
# plt.contourf(topog[:],100, cmap=cm.jet)
# plt.colorbar()
# plt.show()


top = np.array(topog)
print(top.shape)
name = 'atmos_topog'
top = utils.ContourData(top[np.newaxis, :, :], name=name)


[fig, ax] = top.init_frame('Height ($m$)', False)
top.take_snapshots(1, 1, savepath, False)
