import numpy as np
import time
#Numpy'nin çekirdek dili C'de yazıldığı için pythona göre hesaplamaları çok daha hızlı çalıştırabilir.

start_time1=time.time()
A=np.arange(1000000)
A**2
time_1=time.time()-start_time1

start_time2=time.time()
B=range(1000000)
[i**2 for i in B]
time_2=time.time()-start_time2

print(time_2/time_1)