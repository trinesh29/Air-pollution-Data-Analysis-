
##Correlation + Scatter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")

df['pollutant_min'] = pd.to_numeric(df['pollutant_min'], errors='coerce')
df['pollutant_max'] = pd.to_numeric(df['pollutant_max'], errors='coerce')
df['pollutant_avg'] = pd.to_numeric(df['pollutant_avg'], errors='coerce')

df = df.dropna()

# Scatter
plt.scatter(df['pollutant_min'], df['pollutant_max'])
plt.title("Min vs Max Pollution")
plt.show()

# Heatmap
sns.heatmap(df[['pollutant_min','pollutant_max','pollutant_avg']].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()
