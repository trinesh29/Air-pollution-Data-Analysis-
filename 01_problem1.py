# Problem 1:
# To detect and remove outliers in pollutant_avg using the IQR method
# and visualize before and after cleaning using boxplots.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("air_pollution.csv")

data = df.copy()

# -------------------------------
# Basic Info
# -------------------------------
print(data.head())
print(data.info())
print(data.describe())

print("Missing Values:\n", data.isnull().sum())

# -------------------------------
# Select Column
# -------------------------------
col = 'pollutant_avg'

# Convert to numeric
data[col] = pd.to_numeric(data[col], errors='coerce')
data = data.dropna(subset=[col])

# -------------------------------
# IQR Method
# -------------------------------
Q1 = data[col].quantile(0.25)
Q3 = data[col].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Remove outliers
data_clean = data[(data[col] >= lower) & (data[col] <= upper)]

# -------------------------------
# Visualization
# -------------------------------
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.boxplot(y=data[col])
plt.title("Before Outlier Removal")

plt.subplot(1,2,2)
sns.boxplot(y=data_clean[col])
plt.title("After Outlier Removal")

plt.suptitle("Outlier Detection using IQR")

plt.tight_layout()
plt.show()
