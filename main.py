import pandas as pd
import numpy as np
df = pd.read_csv("https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv")
df['email'] = df['email'].str.lower()
df['web'] = df['web'].str.lower()
df = df.rename(columns={'phone2': 'fax'})

df["phone1"] = df["phone1"].str.replace("-", "")
df["fax"] = df["fax"].str.replace("-", "")

df.info()
df.describe()
df.isna().sum()
df.duplicated().sum()





print(df)