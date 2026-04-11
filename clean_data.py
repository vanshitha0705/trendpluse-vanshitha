import pandas as pd
df=pd.read_csv('raw_data.csv.csv')
df=df.dropna()
df=df.drop_duplicates()
df.to_csv('data is cleaned',index=False)
print("data cleaned and saved")
