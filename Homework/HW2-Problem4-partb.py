import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.autolayout"] = True

R      = 1.2
deltar = 0.1
f      = 15
p      = 0
theta  = np.linspace(0,2*np.pi,400)

x, y  = R*(1 + deltar*np.sin((f*theta)+p))*np.cos(theta), R*(1 + deltar*np.sin((f*theta)+p))*np.sin(theta)

fig,ax = plt.subplots()
ax.plot(x,y)

## plt.plot(theta,xfunc,label=)
##plt.show()

##confused about the for loop

# for i in range(10):
#    R = i 
#    p =np. random.uniform(0,2)
#    x, y  = R*(1 + deltar*np.sin((f*theta)+p))*np.cos(theta), R*(1 + deltar*np.sin((f*theta)+p))*np.sin(theta)
#    fig,ax = plt.subplots()
    
plt.show()
