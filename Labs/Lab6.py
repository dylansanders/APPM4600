import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 


s = np.pi/2
h = 0.01*2.**(-np.arange(0,10)) 
f = lambda x: np.cos(x)


def forwardDiff(f,s,h):
  derivForward = (f(s+h)-f(s))/h
  return derivForward

def centDiff(f,s,h):
  derivCenter = (f(s+h)-f(s-h))/(2*h) 
  return derivCenter

forward = forwardDiff(f,s,h)
center = centDiff(f,s,h)
print('forward difference:', forward)
print('center difference:', center)


x0 = np.array([1,0])
Nmax = 100
tol = 1e-10


def evalF(x): 
    F = np.zeros(2)
    F[0] = 4*(x[0]**2)+(x[1]**2)-4
    F[1] = x[0]+x[1]-np.sin(x[0]-x[1])
    return F
    
def evalJ(x):     
    J = np.array([[4, 1], 
        [1-np.cos(x[0]-x[1]), 1+np.sin(x[0]-x[1])]]) 
    return J


def LazyNewton(x0,tol,Nmax):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    J = evalJ(x0)
    Jinv = inv(J)
    for its in range(Nmax):

       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier,its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]   


[xstar,ier,its] =  LazyNewton(x0,tol,Nmax)
print(xstar)
print('Lazy Newton: the error message reads:',ier)
print('Lazy Newton: number of iterations is:',its)

