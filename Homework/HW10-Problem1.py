import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial


x = np.linspace(0, 5, 100)

pade1Err = ((x-((7/60)*(x**3)))/(1+((x**2)/20))) - np.sin(x)
pade2Err = (x/(1+((x**2)/6)+(7*(x**4)/360))) - np.sin(x)
pade3Err = ((x-((7/60)*(x**3)))/(1+((x**2)/20))) - np.sin(x)


plt.plot(x,pade1Err , 'r', label = 'pade 1 error')  
plt.plot(x,pade2Err , 'b', label = 'pade 2 error')  
plt.plot(x,pade3Err , 'g', label = 'pade 3 error') 
plt.show()
