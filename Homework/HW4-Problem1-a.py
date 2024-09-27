import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import special 

x = np.linspace(0,4000)
f = lambda x: -15 + scipy.special.erf(x/(2*np.sqrt(60*(0.1388*10**6))))*(20+15)

#x  = np.linspace(-4,8,20)
#fx = lambda x: x - 10 * np.exp(-1/10*((x-2)**2)) 
y  = [f(val) for val in x]


plt.plot(x,y)
plt.show()
        
