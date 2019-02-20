import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm


class ContourData:
    def __init__(self, A, name=None):
        self.data = A
        self.vabsmax = max(abs(np.amin(A[:, :, :])),abs(np.amax(A[:, :, :])))
        [fig, ax] = plt.subplots()
        self.fig = fig
        self.ax = ax
        self.v = np.linspace(-self.vabsmax,self.vabsmax,100, endpoint=True)
        self.name = name

    def init_frame(self):
        fig, ax = self.fig, self.ax
        plt.contourf(self.data[0,:,:], self.v, cmap=cm.jet)
        plt.colorbar()
        return [fig, ax]

    def frame_i(self,i):
        self.ax.clear()
        im = self.ax.contourf(self.data[i, :, :],self.v,cmap=cm.jet)
        return self.ax


class Pressure(ContourData):
    def __init__(self, A, name=None):
        super().__init__(A, name=None)
    def velocity(self):
        print("Test Passed")

class TimeSeriesData:
    def __init__(self, time, Y, name=None):
        self.time = time
        self.data = Y
        self.name = name
    def time_series_plot(self):
        plt.plot(self.time, self.data, label=self.name)
        # plt.title('Time Series Plot of ' + self.name)
