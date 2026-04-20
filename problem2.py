# Problem 2:
# To analyze the distribution of pollution values,
# handle missing data, and visualize using histogram and boxplot.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("air pollution.csv")

data = df[['pollutant_avg']]

# -------------------------------
# Missing Values
# -------------------------------
print("Missing Values:\n", data.isnull().sum())

# Fill missing values
data = data.fillna(data.mean(numeric_only=True))

# -------------------------------
# Visualization
# -------------------------------
plt.figure(figsize=(10,4))

# Histogram
plt.subplot(1,2,1)
plt.hist(data['pollutant_avg'], bins=30)
plt.title("Pollution Distribution")
plt.xlabel("Pollution Avg")
plt.ylabel("Frequency")
plt.grid()

# Boxplot
plt.subplot(1,2,2)
plt.boxplot(data['pollutant_avg'])
plt.title("Pollution Boxplot")

plt.tight_layout()
plt.show()
