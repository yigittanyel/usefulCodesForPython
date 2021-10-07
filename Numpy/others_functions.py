import numpy as np

x=np.arange(3,20,5) #3den 20ye 5er 5er 20 dahil değil
print(x)

print()

y=np.linspace(0,15,6) #0-15 arası 6 tane rakam 0 ve 15 dahil eğer 3. argümanı koymazsak varsayılan N=50
print(y)

print()

z=np.linspace(2,14,20).reshape(4,5)
print(z)

print()

a=np.random.random((2,4)) #0-1 arası
print(a)

print()

b=np.random.randint(3,12,size=(3,2))#3-12 arası 3 satır 2 sutun
print(b)