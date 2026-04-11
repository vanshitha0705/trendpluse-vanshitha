import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleaned_data.csv')

# Histogram (BEST for marks)
df['Marks'].plot(kind='hist', bins=10)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()