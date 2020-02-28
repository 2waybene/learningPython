from scipy.stats import hypergeom
import matplotlib.pyplot as plt
import numpy as np


#[M,n,N] = [20,7,12]
#rv = hypergeom(M,n,N)

#x = 5
(M,n,N,x) =(12716, 265, 23, 5)
rv = hypergeom(M, n, N)
print (1 - rv.cdf(x))
#5.800300047265061e-06


(M,n,N,x) =(12451, 265, 23, 5)

rv = hypergeom(M, n, N)
print (1 - rv.cdf(x))



print ( 1- hypergeom.cdf ( (45 -1) , (92 + 7518) , 92, 1392))
print ( 1- hypergeom.cdf ( (5 -1) , (50 + 400) , 50, 20))

#6.539773592773024e-06
#print (1-rv.pdf(x))
