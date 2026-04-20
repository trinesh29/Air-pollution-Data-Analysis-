## Comparative Analysis
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

df['pollutant_avg'] = pd.to_numeric(df['pollutant_avg'], errors='coerce')
df = df.dropna()

city_avg = df.groupby('city')['pollutant_avg'].mean().head(10)

# Bar Chart
city_avg.plot(kind='bar')
plt.title("Top Cities Pollution")
plt.show()

# Pie Chart
plt.pie(city_avg, labels=city_avg.index, autopct='%1.1f%%')
plt.title("City Pollution Share")
plt.show()
