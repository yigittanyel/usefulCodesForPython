import numpy as np

x=np.zeros((2,3))
y=np.ones((2,3))
z=np.full((2,3),7)

print(x)
print(y)
print(z)

a=np.empty((2,2))
a.fill(3)
print(a)

b=np.eye(4,k=2) #birim matris
print(b)

c=np.diag([3,2,5,8])
print(c)