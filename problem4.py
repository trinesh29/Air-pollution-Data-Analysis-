# Problem 4:
# To analyze relationship between pollutant_min and pollutant_max
# and visualize distribution.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("air pollution.csv")

df['pollutant_min'] = pd.to_numeric(df['pollutant_min'], errors='coerce')
df['pollutant_max'] = pd.to_numeric(df['pollutant_max'], errors='coerce')

df = df.dropna()

# -------------------------------
# Scatter Plot
# -------------------------------
plt.figure(figsize=(8,5))

plt.scatter(df['pollutant_min'], df['pollutant_max'], alpha=0.5)

plt.title("Min vs Max Pollution")
plt.xlabel("Min Pollution")
plt.ylabel("Max Pollution")

plt.grid()
plt.show()

# -------------------------------
# Histogram
# -------------------------------
plt.hist(df['pollutant_avg'], bins=30)
plt.title("Pollution Distribution")
plt.show()
