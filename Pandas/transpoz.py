import pandas as pd

notlar={"Mat":{"Ali":50,"Mehmet":40,"Ayşe":70},
    "Fiz":{"Ali":40,"Mehmet":60,"Ayşe":50}}

df=pd.DataFrame(notlar)
print(df.T)