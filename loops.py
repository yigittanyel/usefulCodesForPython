""""
#while
i=1
s1=int(input("Bir sayı giriniz: "))
while i<s1:
    print(i)
    i+=2
    #if i==11:
     #   continue
else:
    print("Sayı belirlenen aralığın dışında kaldı.") 
"""

#for
for x in range(3,23,5):
    print(x) #3 8 13 18. 23 not included


adj=["nice","tasty","bad"]
smt=["movie","apple","moment"]

for x in adj:
    for y in smt:
        print(x,y)