# Python script to read in parameters
oceanonly =          0 # Ocean only run?
atmosonly =          0 # Atmos only run?
getcovar =          0  # Get covar in run?
cyclicoc =          0  # Cyclic ocean?
hflxsb =          1  # S boundary heat flux?
hflxnb =          0   # N boundary heat flux?
tauudiff =          0   # Use oc. vel. in tau?
nxto=        960        # Ocean x gridcells
nyto=        960        # Ocean y gridcells
nlo=          3         # Ocean QG layers
nxta=       1536        # Atmos. x gridcells
nyta=        384        # Atmos. y gridcells
nla=          3         # Atmos. QG layers
nxaooc=        240      # Atmos. x gridcells over ocean
nyaooc=        240      # Atmos. y gridcells over ocean
ndxr=          4        # Atmos./Ocean gridlength ratio
nx1=        649         # Starting index for ocean in atmospheric grid
ny1=         73         # Starting index for ocean in atmospheric grid
fnot=   9.37456E-05     # Coriolis parameter
beta=   1.75360E-11     # Beta
tini=   1.00000E+01     # Start time in years
trun=   1.00000E+01     # Run length in years
tend=   2.00000E+01     # Final time in years
dto=   5.40000E+02      # Ocean timestep in seconds
dta=   6.00000E+01      # Atmos. timestep in seconds
dxo=   5.00000E+03      # Ocean grid spacing in km
dxa=   2.00000E+04      # Atmos. grid spacing in km
delek=   2.00000E+00    # Ocean bottom Ekman thickness
cdat=   1.30000E-03     # Air-Sea momentum drag coefficient
rhoat=   1.00000E+00    # Atmos. density
rhooc=   1.00000E+03    # Ocean  density
cpat=   1.00000E+03     # Atmos. spec. heat capacity
cpoc=   4.00000E+03     # Ocean spec. heat capacity
bccoat=   1.00000E+00    # Mixed BC coefficient for atmos (nondim.)
bccooc=   4.17000E-02   # Mixed BC coefficient for ocean (nondim.)
xcexp=   1.00000E+00    # coupling coefficient x
ycexp=   1.00000E+00    # coupling coefficient y
valday=   2.50000E-01   # Solution check interval (days)
odiday=   1.00000E+01   # Ocean  data dump interval (days)
adiday=   1.00000E+01   # Atmos. data dump interval (days)
dgnday=   1.00000E+01   # Diagnostics dump interval (days)
resday=   0.00000E+00   # Restart dump interval (days)
noutoc=      14400     # Output interval: ocean
noutat=      14400     # Output interval: atmos.
nsko=          1        # Subsampling interval for ocean output
nska=          1        # Subsampling interval for atmos. output
dtavat=   1.00000E+00   # Atmos. averaging int. (days)
dtavoc=   1.00000E+00   # Ocean  averaging int. (days)
hmoc=   1.00000E+02     # Fixed ocean  ml depth
hmat=   1.00000E+03     # Fixed atmos. ml depth
st2d=   5.00000E+01     # sst del-sqd diffusivity
st4d=   2.00000E+09     # sst del-4th diffusivity
ahmd=   5.00000E+05     # hmixa lateral diffusivity
at2d=   5.40000E+04     # ast del-sqd diffusivity
at4d=   1.60000E+12     # ast del-4th diffusivity
tsbdy=   1.50665E+01    # o.m.l. S. bdy. temp (rel)
xlamda=   3.50000E+01   # Sensible/latent transfer
hmadmp=   1.50000E-01   # At. mixed layer h damping
fsbar=  -1.90000E+02    # Mean radiation forcing
fspamp=   8.00000E+01   # Radiation perturbation
zm=   2.00000E+02       # Optical depth in a.m.l.
zopt=   2.00000E+04     # Optical depth in layer 1
zopt= [zopt,   2.00000E+04]   # Layers 2,n
zopt= [zopt,   3.00000E+04]   # Layers 2,n
gamma=   1.00000E-02    # Adiabatic lapse rate
gpoc=   2.22000E-02     # Reduced gravity for ocean 1/2 interface
gpoc= [gpoc,   1.69000E-02]   # Interfaces 2,n-1
ah2oc=   5.00000E+01    # Del-sqd coefft ocean
ah2oc= [ah2oc,   5.00000E+01] # Layers 2,n
ah2oc= [ah2oc,   5.00000E+01] # Layers 2,n
ah4oc=   2.00000E+09    # Del-4th coefft ocean
ah4oc= [ah4oc,   2.00000E+09] # Layers 2,n
ah4oc= [ah4oc,   2.00000E+09] # Layers 2,n
tabsoc=   2.87000E+02   # Abs. temperature for ocean layer 1
tabsoc= [tabsoc,   2.82000E+02]    # Layers 2,n
tabsoc= [tabsoc,   2.76000E+02]    # Layers 2,n
tocc=  -2.98919E+00     # Rel. temperature for ocean layer 1
tocc= [tocc,  -7.98919E+00]   # Layers 2,n
tocc= [tocc,  -1.39892E+01]   # Layers 2,n
hoc=   3.50000E+02      # Thickness of ocean layer 1
hoc= [hoc,   7.50000E+02]     # Layers 2,n
hoc= [hoc,   2.90000E+03]     # Layers 2,n
gpat=   1.20000E+00     # Reduced gravity for atmos 1/2 interface
gpat= [gpat,   4.00000E-01]   # Interfaces 2,n-1
ah4at=   1.60000E+12    # Del-4th coefft atmos
ah4at= [ah4at,   1.60000E+12]   # Layers 2,n
ah4at= [ah4at,   1.60000E+12]   # Layers 2,n
tabsat=   3.30000E+02   # Abs. temperature for atmos layer 1
tabsat= [tabsat,   3.40000E+02]    # Layers 2,n
tabsat= [tabsat,   3.50000E+02]    # Layers 2,n
tat=   3.97329E+01      # Rel. temperature for atmos layer 1
tat= [tat,   4.97329E+01]     # Layers 2,n
tat= [tat,   5.97329E+01]     # Layers 2,n
hat=   2.00000E+03      # Thickness of atmos layer 1
hat= [hat,   3.00000E+03]     # Layers 2,n
hat= [hat,   4.00000E+03]     # Layers 2,n
name= './lastday.nc'            # Initial condition file
outfloc= [ 1, 1, 1, 1, 1, 1, 0]    # output flag vector for ocean
outflat= [ 1, 1, 1, 1, 1, 1, 1]    # output flag vector for atmos.
# Derived parameters
tmbara=   2.90267E+02   # Actually T_{mlao}
tmbaro=   2.89989E+02   # Actually T_{mloo}
cphsoc=   4.01815E+00   # Baroclinic wavespeed for ocean mode 1
cphsoc= [cphsoc,   2.10294E+00]   # Higher modes
rdefoc=   4.28622E+04   # Deformation radius for ocean mode 1
rdefoc= [rdefoc,   2.24325E+04]   # Higher modes
tsbdy=   1.50665E+01    # Rel. o.m.l. S. bndry temp. (K)
tnbdy=  -1.50665E+01    # Rel. o.m.l. N. bndry temp. (K)
cphsat=   4.65197E+01   # Baroclinic wavespeed for atmos mode 1
cphsat= [cphsat,   2.43203E+01]   # Higher modes
rdefat=   4.96233E+05   # Deformation radius for atmos mode 1
rdefat= [rdefat,   2.59428E+05]   # Higher modes
aface=   3.02170E-07    # eta    coefficient aface(1)
aface= [aface,  -9.12409E-08]   # Other interfaces
bface=   1.06328E-06    # etam   coefficient bface
cface=   1.06328E-06    # topog. coefficient cface
dface=   7.17687E-05    # aTm    coefficient dface
