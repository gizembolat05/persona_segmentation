import pandas as pd
import numpy as np
from pandas.core.groupby.generic import AggScalar

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

df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE" : "mean"}).head()
agg_df = df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE" : "mean"}).head().sort_values(by=["PRICE"],ascending=False).reset_index()

my_labels=["0_18","19_23","24_30","31_40","41_70"]
bins=[0,18,23,30,40,70]

agg_df["AGE_CUT"]=pd.cut(agg_df["AGE"], bins, labels=my_labels)
agg_df.head()

agg_df["customers_level_based"] = agg_df[["COUNTRY","SOURCE","SEX","AGE_CUT"]].apply(lambda x : "_".join(x).upper(), axis=1)
agg_df.head()
agg_df["customers_level_based"].value_counts()
agg_df=agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})
agg_df=agg_df.reset_index()
agg_df["customers_level_based"].value_counts()
agg_df.head()

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"],4 , labels=["D","C","B","A"])
agg_df.head()

new_user="BRA_ANDROID_FEMALE_0_18"
new_user2="BRA_ANDROID_FEMALE_19_23"
agg_df[agg_df["customers_level_based"] == new_user]
agg_df[agg_df["customers_level_based"] == new_user2]

agg_df.to_csv("output/agg_df.csv", index=False)
