# import libraries
import numpy as np

def driver():

# use routines    
    f = lambda x: (x**2)-x
    fp = lambda x: (2*x)-1
    fpp = lambda x: 2
    a = -4
    b = 5

#    f = lambda x: np.sin(x)
#    a = 0.1
#    b = np.pi+0.1

    tol = 1e-8

    [astar,ier] = bisection(f,fp,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))




# define routines
def bisection(f,fp,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)
    gp = f(d)*fpp(d)/fp(d)
    while (gp> 1):
      fd = f(d)
      if (fd ==0):
        astar = d
       # print(fp(astar))
        if abs(fp(astar))<1:
          ier = 0
          print("first deriv evaluated at astar:",abs(fp)(astar))
          return[astar,ier]
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('derivative values:',abs(fp(d)))
#      if abs(fp(d))<1:
#        print(abs(fp(d)))
#        break
#      break
        #ier = 0
	#return [astar, ier]
    #  print(abs(fp(astar))
     # print('iterations:', count)
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier]
      
driver()               

