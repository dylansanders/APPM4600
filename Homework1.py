import numpy as np
import matplotlib.pyplot as plt

xArray = np.arange(1.920,2.080,.001 )

for x in xArray:
    pArray = []
    p1 = (x^9) - (18*x^8) + (144*x^7) - (672*x^6) + (2016*x^5) - (4032*x^4) + (5376*x^3) - (4608*x^2) + (2304*x) - 512
    pArray.append(p1)


#p2 = (x-2)^9


plt.plot(x,p1)
