import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
# from input_parameters import rhoat, rhooc, fnot
import utils as utils

datapath = '/Users/rk2014/Documents/q-gcm/src/outdata/'

# Files that describe oceanic and atmospheric state
# atpa = nc.Dataset(datapath + 'atpa.nc')
# ocpo = nc.Dataset(datapath + 'ocpo.nc')
avges = nc.Dataset(datapath + 'avges.nc')

print(avges.variables)

# time = q_oc.shape[0] # total time
