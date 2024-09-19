import numpy as np

A        = .5*np.matrix([[1,1],[1+(10**-10),1-(10**-10)]])
nomrA    = np.linalg.norm(A,ord=2)
Ainv     = np.matrix([[1-(10**10),10**10],[1+(10**10),-10**10]])
normAinv = np.linalg.norm(Ainv,ord=2)
b        = np.matrix([[1],[1]])
x  	 = np.matrix([[1],[1]])
normX    = np.linalg.norm(x,ord=2)  

changeb     = np.matrix([[10**-5],[2*(10**-5)]])
sameChangeb = np.matrix([[10**-5],[(10**-5)]])


changeX     = np.matmul(Ainv,changeb)
normChangeX = np.linalg.norm(changeX,ord=2)

relError = normChangeX/normX

print('change in x: ', changeX)
print('norm of change in x: ', normChangeX)
print('norm of x: ', normX)
print('relative error: ', relError)
 
