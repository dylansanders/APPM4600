import numpy as np
import math

def calc(x):
    y = math.e**x
    y2 = y-1
    print("x= ",x)
    print("y-1= ",y2)
    print("\n")

calc(1)
calc(1.2)

calc(12)
calc(12.2)

calc(9.999999995000000e-10)

