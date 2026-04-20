# Data Cleaning + Preprocessing
import pandas as pd

file_path = "dataset.csv"

df = pd.read_csv(file_path)

df.columns = df.columns.str.strip().str.lower()

df['pollutant_avg'] = pd.to_numeric(df['pollutant_avg'], errors='coerce')
df['pollutant_min'] = pd.to_numeric(df['pollutant_min'], errors='coerce')
df['pollutant_max'] = pd.to_numeric(df['pollutant_max'], errors='coerce')

df = df.dropna()

print("Cleaned Data:\n")
print(df.head())
