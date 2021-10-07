import pandas as pd

a=pd.Series(["Yigit","Semih","Yusuf",21,9.5],index=["a","b","c","d","e"]);
print(a)

print()
#Sözlük veri yapısını series'e çevirme

puan={"Ali":65,"Veli":80,"Mahmut":55}
sr=pd.Series(puan)
print("Puanı 60'dan büyük olanlar \n {}".format(sr[sr>60]))

sr[sr<60]=False
print(sr)

print("Ali" in sr)