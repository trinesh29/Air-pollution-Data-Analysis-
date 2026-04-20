# Problem 5:
# To analyze trends and perform machine learning and statistical tests.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("dataset.csv")

df['pollutant_avg'] = pd.to_numeric(df['pollutant_avg'], errors='coerce')
df['pollutant_min'] = pd.to_numeric(df['pollutant_min'], errors='coerce')
df['pollutant_max'] = pd.to_numeric(df['pollutant_max'], errors='coerce')

df = df.dropna()

# -------------------------------
# Trend (Ordered Line Plot)
# -------------------------------
df_sorted = df.sort_values('pollutant_avg').reset_index(drop=True)
df_sorted['index'] = range(len(df_sorted))

plt.plot(df_sorted['index'], df_sorted['pollutant_avg'])
plt.title("Pollution Trend")
plt.show()

# -------------------------------
# Machine Learning
# -------------------------------
X = df[['pollutant_min','pollutant_max']]
y = df['pollutant_avg']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("R2 Score:", r2_score(y_test, predictions))

# -------------------------------
# Statistical Tests
# -------------------------------
data = df['pollutant_avg']

z_score = (np.mean(data) - 50) / (np.std(data)/np.sqrt(len(data)))
t_stat, p_val = stats.ttest_1samp(data, 50)

sample = data.sample(500)
s_stat, s_p = stats.shapiro(sample)

print("Z-score:", z_score)
print("T-test:", t_stat, p_val)
print("Shapiro:", s_stat, s_p))
