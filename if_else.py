""""
x=int(input("Yaşınızı giriniz: "))
if x<18:
    print("You can't take driving license")
elif x>=18:
    print("You can take driving license")
"""

#short if-else
s1=48
s2=48
#print("S1") if s1>s2 else print("Equal") if s2==s1 else print("S2")
print("{0}".format(s1)) if s1>s2 else print("{0}".format("=")) if s2==s1 else print("{0}".format(s2))