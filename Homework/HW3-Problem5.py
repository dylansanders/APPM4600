import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-2, 10, 100)
y = x-4*np.sin(2*x)-3

plt.axhline()
plt.plot(x,y)
plt.show()
