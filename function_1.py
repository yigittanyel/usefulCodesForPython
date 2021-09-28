"""
x=input("İsminiz nedir: ")
def my_func(x):
    print("Hoş geldin " +x) 

my_func(x)
"""

""""
def my_func(name,surname="Tanyel"):
    print("Hoş geldin "+name + " "+surname)

my_func("Yigit")
"""
""""
# using *args
def my_func(*ages):
	print("Yaşca en küçük olan {0}'dır.".format(my_func2(*ages)))

def my_func2(a,b,c):
	if a<b and a<c :
    	return a
    elif b<a and b<c:
    	print(b)
    elif c<a and c<b:
    	return c


    
my_func(20,23,41)
"""
""""
def my_func(*kids):
    print("En küçük çocuk {0}'dır.".format(kids[2]))

my_func("Yigit","Semih","Yusuf")
"""
