
import pandas as pd
file1=pd.read_csv("homes.csv")
print(file1.head()) #ilk 5 satır
print("----------------")
print(file1.dtypes)
print("*************")
print(file1.Sell.describe())
print()
print(file1.Sell.value_counts()) #her değerden kaç tane var
print()
print()
print(file1.Sell.value_counts(normalize=True))