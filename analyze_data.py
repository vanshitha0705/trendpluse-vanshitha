import pandas as pd
df=pd.read_csv('raw_data.csv.csv')

print(" Analysis")

print("Columns:", df.columns)

print("\nSummary:")
print(df.describe())

print("\nAverage Marks:")
print(df['Marks'].mean())

print("\nMax Marks:", df['Marks'].max())
print("Min Marks:", df['Marks'].min())