import pandas as pd

# Load dataset
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# Fill missing values
df["Income"] = df["Income"].fillna(df["Income"].mean())

# Standardize column names
df.columns = df.columns.str.lower()

# Convert date column
df["dt_customer"] = pd.to_datetime(df["dt_customer"], dayfirst=True)

# Save cleaned dataset
df.to_csv("cleaned_marketing_campaign.csv", index=False)

print("Cleaned dataset saved successfully!")