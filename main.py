import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/gizemb/Desktop/persona.csv")
df.head()
df.info()
df.dtypes
df.shape
df.isnull().values.any()
df["SOURCE"].nunique()
df["SOURCE"].value_counts()
df["PRICE"].nunique()
df["PRICE"].value_counts()
df["COUNTRY"].value_counts()
df.groupby("COUNTRY").agg({"PRICE": "sum"}).sort_values(by="PRICE", ascending=False)
df.groupby("SOURCE").agg({"SEX": "count"})
df["SOURCE"].value_counts()
df.groupby("COUNTRY").agg({"PRICE" : "mean"})
df.groupby("SOURCE").agg({"PRICE" : "mean"})
df.groupby(["COUNTRY" , "SOURCE"]).agg({"PRICE": "mean"})