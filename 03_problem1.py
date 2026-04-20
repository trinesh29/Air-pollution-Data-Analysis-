# Problem 3:
# To analyze pollution across different cities using bar and pie charts.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("air_pollution.csv")

df['pollutant_avg'] = pd.to_numeric(df['pollutant_avg'], errors='coerce')
df = df.dropna()

city_data = df.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False).head(10)

# -------------------------------
# Bar Chart
# -------------------------------
plt.figure(figsize=(8,5))

bars = plt.bar(city_data.index, city_data.values)

# Labels
for bar in bars:
    y = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, y, round(y,2), ha='center', fontsize=8)

plt.xticks(rotation=45)
plt.title("Top Cities Pollution")
plt.xlabel("City")
plt.ylabel("Pollution Avg")

plt.show()

# -------------------------------
# Pie Chart
# -------------------------------
city_data.plot(kind='pie', autopct='%1.1f%%')
plt.title("City Pollution Share")
plt.ylabel("")
plt.show()
