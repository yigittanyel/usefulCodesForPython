import pandas as pd

veri={"isim":["Yiğit","Yusuf","Melike","Semih"],
    "puan":[75,60,85,80],
    "cinsiyet":["E","E","K","E"]}

df=pd.DataFrame(veri,columns=["isim","cinsiyet","puan","yas"])
print(df)

print(df.head(2)) #baştan iki veri
print(df.tail(2)) #sondan iki veri
print()
print("-----------------------")
print()
print(df.iloc[[0,3]]) #0 ve 3. satırları gösterir.

#yeni bir sutun ekledik ve ona dizi atadık
deger=[10,11,12,13]
df["yas"]=deger
print(df)

df["gecti"]=df.puan>70
print(df)

