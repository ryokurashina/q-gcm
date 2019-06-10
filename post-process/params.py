import netCDF4 as nc
from input_parameters import fnot, hoc, gpoc, hat, gpat, rdefoc
import numpy as np

def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i

# Number of layers in ocean

def bc(alpha, option=True):
    # If boundary coefficient is given in m
    if option:
        return 1/alpha
    # If boundary coefficient is given in 1/m
    else:
        return alpha



def strat(Rd_bc1, Rd_bc2, H1, H2, H3, f0, option=True):
    R12 = H1/H2
    R13 = H1/H3
    # Find gamma
    AA = (Rd_bc1**2-Rd_bc2**2)/(Rd_bc1**2+Rd_bc2**2)
    u = (R12+R13)**2
    v = 2.*(1+R12)*(R12+R13)+(4./(AA**2-1.))*(R12+R13+R12*R13)
    w = (1.+R12)**2
    gamma = (-v-np.sqrt(v**2-4.*u*w))/(2.*u)
    print("gamma = ", gamma)

    a = 1.+R12*(1.+gamma)+R13*gamma
    b = gamma*(R12+R13+R12*R13)
    c = np.sqrt((a+np.sqrt(a**2-4.*b))/(2.*b))

    Rd1 = Rd_bc1/c
    Rd21 = Rd_bc1/(c*np.sqrt(R12))
    Rd22 = Rd_bc1/(c*np.sqrt(gamma*R12))
    Rd3 = Rd_bc1/(c*np.sqrt(gamma*R13))

    # Return reduced gravities if option set as True (default)
    if option:
        return [Rd1**2*f0**2/H1, Rd22**2*f0**2/H2]
    # Otherwise just return the stratification parameters
    else:
        return [1/Rd1**2, 1/Rd21**2, 1/Rd22**2, 1/Rd3**2]


if __name__ == '__main__':
    # print("Actual gpoc:", gpoc)
    f0 = fnot
    print(f0)

    # print(hoc)
    # # H_oc = hoc
    # H_oc = [250, 750, 2900]
    # N_oc = len(H_oc)
    print(strat(40000, 20600, 250,750,3000, f0, True))
    # print(strat(40000, 20600,250,750,3000, 0.83*10**(-4), True))
    # print(bc(120*10**3))
