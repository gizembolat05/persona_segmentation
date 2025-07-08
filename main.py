import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/gizemb/Desktop/persona.csv")
df.head()
df.info()
df.dtypes
df.shape
df.isnull().values.any()