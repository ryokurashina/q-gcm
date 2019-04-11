import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from input_parameters import bccoat, bccooc, dxo, dxa


class ContourData:
    """ Class used in order to produce contour plots for data.
    param: A: 3-D array with dimensions time x dim1 x dim2.
    param: name: Optional name of data.
    """
    def __init__(self, A, name=None):
        self.data = A
        self.vabsmax = max(abs(np.amin(A[:, :, :])),abs(np.amax(A[:, :, :])))
        [fig, ax] = plt.subplots()
        self.fig = fig
        self.ax = ax
        self.vec = np.linspace(-self.vabsmax,self.vabsmax, 100, endpoint=True)
        self.name = name

    def init_frame(self):
        """ Produces the initial contour frame of data. Useful for when producing
         .gif files with the Animation package on matplotlib.
        """
        fig, ax = self.fig, self.ax
        ax = plt.contourf(self.data[0, :, :], self.vec, cmap=cm.jet)
        plt.colorbar(ax)
        return [fig, ax]

    def frame_i(self,i):
        """ Produces the i-th time-step frame of the data. Again, this is useful
        for producing .gif files.
        """
        self.ax.clear()
        return self.ax.contourf(self.data[i, :, :], self.vec, cmap=cm.jet)


class Pressure(ContourData):
    """ Sub-class for dynamic pressure data because we will also calculate
    velocities from this using the G.S. balance.
    """
    def __init__(self, A, name=None):
        super().__init__(A, name=None)

    def velocities(self, flag, alpha, dx, dy, rho, f):
        """ Method that generates the velocity fields given the partial slip
        B.C. parameter.
        param: flag: Enter 0 for ocean and 1 for atmosphere
        param: alpha: Dimensional partial-slip B.C. parameter.
        param: dx, dy: Spatial-step sizes in zonal and meridional directions.
        param: rho: Density of fluid.
        param: f: Coriolis parameter.
        """
        if flag == 0:
            # This is so we can add extra rows and columns for the ghost points
            [t, M, N] = [self.data.shape[0], self.data.shape[1], self.data.shape[2]]
            P = np.zeros((t, M+2, N+2))
            u = np.zeros((t, M, N))
            v = np.zeros((t, M, N))
            P[:, 1:M+1, 1:N+1] = self.data
            for i in range(t):
                # Apply p_nn = -p_n to each wall
                # Left wall
                P[i, :, 0] = 2*alpha/(2*alpha+dx)*(2*P[i, :, 1]-P[i, :, 2])+\
                    dx/(2*alpha+dx)*P[i, :, 2]
                # Right wall
                P[i, :, M+1] = 2*alpha/(2*alpha-dx)*(2*P[i, :, M]-P[i, :, M-1])-\
                    dx/(2*alpha-dx)*P[i, M-1, :]
                # Bottom wall
                P[i, 0, :] = 2*alpha/(2*alpha+dy)*(2*P[i, 1, :]-P[i, 2, :])+\
                    dy/(2*alpha+dy)*P[i, 2, :]
                # Top wall
                P[i, N+1, :] = 2*alpha/(2*alpha-dy)*(2*P[i, N, :]-P[i, N-1, :])-\
                    dy/(2*alpha-dy)*P[i, N-1, :]
                # v = 1/(rho*f)*dp/dx and u = -1/(rho*f)*dp/dy
                u[i, :, 1:N-1] = -1/(rho*f)*(P[i, 2:M+2, 1:N-1]-P[i, 0:M, 1:N-1])/(2*dy)
                v[i, 1:M-1, :] = 1/(rho*f)*(P[i, 1:M-1, 2:N+2]-P[i, 1:M-1, 0:N])/(2*dx)

            #return [ContourData(u), None ]
            return [None, ContourData(v)]
        else:
            raise NotImplementedError








class TimeSeriesData:
    """ Class defined to produce plots for data in time series format.
    param: time: 1-D array containing times (days) in which data is recorded.
    param: Y: 1-D array containing data values for whatever we record.
    param: name: Optional parameter which contains the name of the data.
    """

    def __init__(self, time, Y, name=None):
        self.time = time
        self.data = Y
        self.name = name
    def time_series_plot(self):
        plt.plot(self.time, self.data, label=self.name)
