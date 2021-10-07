import numpy as np

x=np.array([1,2,3.0])
print(x.dtype) #Upcasting

y=np.array([1.2,3.5,7.9],dtype=np.int)
print(y.dtype) #Downcasting

print()
x=x.astype(np.complex) #Astype 
print(x)