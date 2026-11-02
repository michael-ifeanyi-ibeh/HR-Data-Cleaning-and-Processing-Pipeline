import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("messy-and-clean_data/raw/Messy_Employee_dataset.csv")

# Quick look at the data
print("Initial shape:", df.shape)
print(df.head())


# 1. Standardize column names
df.columns = df.columns.str.strip().str.title().str.replace(" ", "_")

# 2. Remove duplicates
df = df.drop_duplicates()

# 3. Fix data types
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# 4. Clean Satus values
df["Status"] = df["Status"].str.strip().str.title()

# 5. Handle missing values
df = df.replace("?", np.nan)
df = df.dropna(subset=["Employee_Id"])
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Age"] = df["Age"].fillna(df["Age"].median())

# 6. Split Department_Region
df[['Department', 'Region']] = df['Department_Region'].str.rsplit('-', n=1, expand=True)
df['Department'] = df['Department'].str.strip().str.title()
df['Region'] = df["Region"].str.strip()
df = df.drop(columns=['Department_Region'])

# 7. Save cleaned dataset
df.to_csv("messy-and-clean_data/cleaned/Cleaned_Employee_dataset.csv", index=False)

print("Cleaned shape:", df.shape)
print("Data cleaning complete. File saved as Cleaned_Employee_dataset.csv")