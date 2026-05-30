import pandas as pd

# Load dataset
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# Check missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing values in Income column
df["Income"] = df["Income"].fillna(df["Income"].mean())

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Remove duplicates (if any)
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.lower()

# Convert date column to datetime format
df["dt_customer"] = pd.to_datetime(df["dt_customer"], dayfirst=True)

# Save cleaned dataset
df.to_csv("cleaned_marketing_campaign.csv", index=False)

print("\nCleaned dataset saved successfully!")
