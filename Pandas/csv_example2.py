import pandas as pd
import matplotlib
f1=pd.read_csv("homes.csv")
print(f1.Sell.value_counts().head())
print()
print(f1.Sell.unique()) #tekrar eden değerler
print(f1.Sell.nunique()) #toplam kaç adet değer var

#print(pd.crosstab(f1.Sell,f1.Age))  İkisini karşılaştırmak için
print(f1.Sell.value_counts()) #değeri 175'i geçen 2 tane 170'i geçen 1 tane


f1.Sell.plot(kind="hist")