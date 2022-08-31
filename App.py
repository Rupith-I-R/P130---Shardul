import pandas as pd
import csv

df = pd.read_csv("Merged_dataset.csv")


del df["Luminosity"]
#del df["Star_name.1"]
#del df["Distance"]
#del df["Mass"]
#del df["Radius"]

df.to_csv("Final.csv")
#print(df.shape)

df2 = pd.read_csv("Final.csv")

del df2["Unnamed: 0"]
del df2["Unnamed: 6"]
del df2["Star_name.1"]
del df2["Distance.1"]
del df2["Mass.1"]
del df2["Radius.1"]

df2.to_csv("Correct.csv")