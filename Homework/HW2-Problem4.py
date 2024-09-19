import numpy as np

t = np.arange(0,np.pi,(np.pi)/30)
y = y = np.cos(t)
n = 2

def summation(n): 
    sumX = 0
    for i in range(1, n + 1):
        sumX += (y*t)
    print('the sum is: ',sumX)
    print('for n=', n)

summation(n)
