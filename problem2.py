# Distribution + Outliers
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")

df['pollutant_avg'] = pd.to_numeric(df['pollutant_avg'], errors='coerce')
df = df.dropna()

# Histogram
plt.hist(df['pollutant_avg'], bins=30)
plt.title("Pollution Distribution")
plt.show()

# Boxplot
plt.boxplot(df['pollutant_avg'])
plt.title("Outliers Detection")
plt.show()

# Violin Plot
sns.violinplot(y=df['pollutant_avg'])
plt.title("Distribution Shape")
plt.show()
