# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: (10/(x+4))**(1/2)
# fixed point is alpha1 = 1.4987....

  #   f2 = lambda x: x
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-10

# test f1 '''
     x0 = 1.5
     [xstar,ier,x] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
     print('iteration values:', x)
     print('number of iterations:',len(x))   
#test f2 '''
#     x0 = 0.0
 #    [xstar,ier,x] = fixedpt(f2,x0,tol,Nmax)
 #    print('the approximate fixed point is:',xstar)
 #    print('f2(xstar):',f2(xstar))
 #    print('Error message reads:',ier)
     
     computeOrder(np.array(x[:-1]),xstar)

# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    x = []
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       x.append(x1)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
#          print('iteration value:', x1)
          return [xstar,ier,x]
       x0 = x1
       
    xstar = x1
    ier = 1
    print(x)
    return [xstar, ier, x]
    

def computeOrder(x,xstar):

    ## x : array of iterate values
    ## xstar : fixed point solutins

    diff1 = np.abs(x[1::]-xstar)
    diff2 = np.abs(x[0:-1]-xstar)
    fit = np.polyfit(np.log(diff2.flatten()),np.log(diff1.flatten()),1)

    _lambda = np.exp(fit[1])
    alpha = fit[0]

    print(f"lambda is {_lambda}")
    print(f"alpha is {alpha}")
    return fit



driver()
