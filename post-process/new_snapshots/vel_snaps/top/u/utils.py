import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import cm
from matplotlib import ticker
from matplotlib import rc
from input_parameters import bccoat, bccooc, dxo, dxa

plt.rcParams.update({'font.size': 14})
rc('text', usetex=True)

def add_ocean():
    x = np.linspace(648, 888, 241)
    y = np.linspace(72, 312, 241)
    # Bottom wall
    plt.plot(x, 72*np.ones_like(x),'k--')
    # Left wall
    plt.plot(648*np.ones_like(y), y,'k--')
    # Top wall
    plt.plot(x, 312*np.ones_like(x),'k--')
    # Right wall
    plt.plot(888*np.ones_like(y), y,'k--')

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

    def init_frame(self, unit, option):
        """ Produces the initial contour frame of data. Useful for when producing
         .gif files with the Animation package on matplotlib.
        param: unit: String containing unit of variable plotted.
        param: option: Boolean, True for ocean and False for atmos.
        """
        fig, ax = self.fig, self.ax
        if option:
            ax.set_aspect('equal')
            ax = plt.contourf(self.data[0, :, :], self.vec, cmap=cm.jet)
            #plt.colorbar(ax, format='%.2e', orientation = 'vertical', ticks = [-self.vabsmax, 0, self.vabsmax]).ax.set_ylabel(unit)
            plt.colorbar(ax, format='%.2e', orientation = 'vertical', ticks = [0, self.vabsmax]).ax.set_ylabel(unit)

        else:
            ax.set_aspect('equal')
            ax = plt.contourf(self.data[0, :, :], self.vec, cmap=cm.jet)
            #plt.colorbar(ax, format='%.2e', orientation = 'horizontal', ticks = [-self.vabsmax, 0, self.vabsmax]).ax.set_xlabel(unit)
            plt.colorbar(ax, format='%.2e', orientation = 'horizontal', ticks = [0, self.vabsmax]).ax.set_xlabel(unit)
            add_ocean()
        return [fig, ax]

    def frame_i(self, i):
        """ Produces the i-th time-step frame of the data. Again, this is useful
        for producing .gif files.
        """
        self.ax.clear()
        return self.ax.contourf(self.data[i, :, :], self.vec, cmap=cm.jet)

    def take_snapshots(self, period, save_period, path, option):
        """ Produces periodic snapshots of the flow.
        param: period: The period at which we take snapshots (in the data).
        param: save_period: The period at which data is saved in the q-gcm code.
        param: path: String containing datapath to save to
        param: option: Boolean, True for ocean, False for atmos.
        param: option: String containing units of variable
        """
        time = self.data.shape[0]
        for i in range(0, time, period):
            self.frame_i(i)
            add_ocean()
            # Ocean
            if option:
                plt.xticks([0, self.data.shape[2]/2, self.data.shape[2]], ['0', '$^oX/2$', '$^oX$'])
                plt.yticks([0, self.data.shape[1]/2, self.data.shape[1]], ['0', '$^oY/2$', '$^oY$'])
            # Atmosphere
            else:
                plt.xticks([0, self.data.shape[2]/2, self.data.shape[2]], ['0', '$^aX/2$', '$^aX$'])
                plt.yticks([0, self.data.shape[1]/2, self.data.shape[1]], ['0', '$^aY/2$', '$^aY$'])

            plt.savefig(path+self.name+'_day_'+str(i*save_period)+'.png', bbox_inches = 'tight', pad_inches = 0.25)




class Pressure(ContourData):
    """ Sub-class for dynamic pressure data because we will also calculate
    velocities from this using the G.S. balance.
    """
    def __init__(self, A, name=None):
        super().__init__(A, name=None)

    def zonal(self, flag, alpha, dx, f):
        """ Method that generates the zonal fields given the partial slip
        B.C. parameter.
        param: flag: Enter 0 for ocean and 1 for atmosphere
        param: alpha: Dimensional partial-slip B.C. parameter.
        param: dx, dy: Spatial-step sizes in zonal and meridional directions.
        param: f: Coriolis parameter.
        """
        if flag == 0:
            # This is so we can add extra rows and columns for the ghost points
            [t, M, N] = [self.data.shape[0], self.data.shape[1], self.data.shape[2]]
            P = np.zeros((t, M+2, N+2))
            u = np.zeros((t, M, N))
            # v = np.zeros((t, M, N))
            P[:, 1:M+1, 1:N+1] = self.data
            for i in range(t):
                # Apply p_nn = -p_n to each wall
                # Left wall
                P[i, :, 0] = 2*alpha/(2*alpha+dx)*(2*P[i, :, 1]-P[i, :, 2])+\
                    dx/(2*alpha+dx)*P[i, :, 2]
                # Right wall
                P[i, :, N+1] = 2*alpha/(2*alpha-dx)*(2*P[i, :, N]-P[i, :, N-1])-\
                    dx/(2*alpha-dx)*P[i, N-1, :]
                # Bottom wall
                P[i, 0, :] = 2*alpha/(2*alpha+dx)*(2*P[i, 1, :]-P[i, 2, :])+\
                    dx/(2*alpha+dx)*P[i, 2, :]
                # Top wall
                P[i, M+1, :] = 2*alpha/(2*alpha-dx)*(2*P[i, M, :]-P[i, M-1, :])-\
                    dx/(2*alpha-dx)*P[i, M-1, :]
                # v = 1/f*dp/dx and u = -1/f*dp/dx
                #u[i, :, 1:N-1] = -1/f*(P[i, 2:M+2, 1:N-1]-P[i, 0:M, 1:N-1])/(4*dx)
                u[i, :, 1:N-1] = -1/f*(P[i, 2:M+2, 1:N-1]-P[i, 0:M, 1:N-1])/(2*dx)
            return ContourData(u)

        elif flag == 1:
            # This is so we can add extra rows and columns for the ghost points
            [t, M, N] = [self.data.shape[0], self.data.shape[1], self.data.shape[2]]
            P = np.zeros((t, M+2, N+2))
            u = np.zeros((t, M, N))
            # v = np.zeros((t, M, N))
            P[:, 1:M+1, 1:N+1] = self.data
            for i in range(t):
                # Apply p_nn = -p_n to each wall
                # Left wall - set this equal to last column of p for periodic b.c.
                P[i, :, 0] = P[i, :, N]
                # Right wall - set this equal to first column of p
                P[i, :, N+1] = P[i, :, 1]
                # Bottom wall
                P[i, 0, :] = 2*alpha/(2*alpha+dx)*(2*P[i, 1, :]-P[i, 2, :])+\
                    dx/(2*alpha+dx)*P[i, 2, :]
                # Top wall
                P[i, M+1, :] = 2*alpha/(2*alpha-dx)*(2*P[i, M, :]-P[i, M-1, :])-\
                    dx/(2*alpha-dx)*P[i, M-1, :]
                # v = 1/f*dp/dx and u = -1/f*dp/dy
                #u[i, :, 1:N-1] = -1/f*(P[i, 2:M+2, 1:N-1]-P[i, 0:M, 1:N-1])/(4*dx)
                u[i, :, 1:N-1] = -1/f*(P[i, 2:M+2, 1:N-1]-P[i, 0:M, 1:N-1])/(2*dx)
            return ContourData(u)


    def meridional(self, flag, alpha, dx, f):
        """ Method that generates the meridional velocity fields given the partial slip
        B.C. parameter.
        param: flag: Enter 0 for ocean and 1 for atmosphere
        param: alpha: Dimensional partial-slip B.C. parameter.
        param: dx, dy: Spatial-step sizes in zonal and meridional directions.
        param: f: Coriolis parameter.
        """
        if flag == 0:
            # This is so we can add extra rows and columns for the ghost points
            [t, M, N] = [self.data.shape[0], self.data.shape[1], self.data.shape[2]]
            P = np.zeros((t, M+2, N+2))
            # u = np.zeros((t, M, N))
            v = np.zeros((t, M, N))
            P[:, 1:M+1, 1:N+1] = self.data
            for i in range(t):
                # Apply p_nn = -p_n to each wall
                # Left wall
                P[i, :, 0] = 2*alpha/(2*alpha+dx)*(2*P[i, :, 1]-P[i, :, 2])+\
                    dx/(2*alpha+dx)*P[i, :, 2]
                # Right wall
                P[i, :, N+1] = 2*alpha/(2*alpha-dx)*(2*P[i, :, N]-P[i, :, N-1])-\
                    dx/(2*alpha-dx)*P[i, N-1, :]
                # Bottom wall
                P[i, 0, :] = 2*alpha/(2*alpha+dx)*(2*P[i, 1, :]-P[i, 2, :])+\
                    dx/(2*alpha+dx)*P[i, 2, :]
                # Top wall
                P[i, M+1, :] = 2*alpha/(2*alpha-dx)*(2*P[i, M, :]-P[i, M-1, :])-\
                    dx/(2*alpha-dx)*P[i, M-1, :]
                # v = 1/f*dp/dx and u = -1/f*dp/dx
                #v[i, 1:M-1, :] = 1/f*(P[i, 1:M-1, 2:N+2]-P[i, 1:M-1, 0:N])/(4*dx)
                v[i, 1:M-1, :] = 1/f*(P[i, 1:M-1, 2:N+2]-P[i, 1:M-1, 0:N])/(2*dx)
            return ContourData(v)

        elif flag == 1:
            # This is so we can add extra rows and columns for the ghost points
            [t, M, N] = [self.data.shape[0], self.data.shape[1], self.data.shape[2]]
            P = np.zeros((t, M+2, N+2))
            # u = np.zeros((t, M, N))
            v = np.zeros((t, M, N))
            P[:, 1:M+1, 1:N+1] = self.data
            for i in range(t):
                # Apply p_nn = -p_n to each wall
                # Left wall - set this equal to last column of p for periodic b.c.
                P[i, :, 0] = P[i, :, N]
                # Right wall - set this equal to first column of p
                P[i, :, N+1] = P[i, :, 1]
                # Bottom wall
                P[i, 0, :] = 2*alpha/(2*alpha+dx)*(2*P[i, 1, :]-P[i, 2, :])+\
                    dx/(2*alpha+dx)*P[i, 2, :]
                # Top wall
                P[i, M+1, :] = 2*alpha/(2*alpha-dx)*(2*P[i, M, :]-P[i, M-1, :])-\
                    dx/(2*alpha-dx)*P[i, M-1, :]
                # v = 1/f*dp/dx and u = -1/f*dp/dy
                v[i, 1:M-1, :] = 1/f*(P[i, 1:M-1, 2:N+2]-P[i, 1:M-1, 0:N])/(2*dx)
                #v[i, 1:M-1, :] = 1/f*(P[i, 1:M-1, 2:N+2]-P[i, 1:M-1, 0:N])/(4*dx)
            return ContourData(v)

    def speed(self, flag, alpha, dx, f):
        u = self.zonal(flag, alpha, dx, f)
        v = self.meridional(flag, alpha, dx, f)
        return ContourData(np.sqrt(np.square(np.array(u.data))+np.square(np.array(v.data))))





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
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
