import pandas as pd
import matplotlib
f1=pd.read_csv("homes.csv")

print(f1.Sell.plot(kind="hist"))
f1.Sell.value_counts().plot(kind="bar")