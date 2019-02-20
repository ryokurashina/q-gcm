import os
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

 

time = 50 # total time

plt.ion()
plt.pause(5)

for t in np.arange(0, time):
    t+=1

    x = np.linspace(0.0,np.pi*6,100)
    def sinwave(x, t): 
        return pow(-1,t)*np.sin(x)


    plt.ylabel('sin(3x)')
    plt.xlabel('x')
    plt.title('Animation')
    plt.plot(x,sinwave(x,t))
    #plt.show()
    #plt.xticks(site_index, site_index)
    plt.draw()
    plt.pause(0.2)
    plt.clf()
plt.ioff()
#plt.clf()


