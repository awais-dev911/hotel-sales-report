import pandas as pd

# Read CSV file
df = pd.read_csv("sales.csv")

# Preview data
print("First 5 rows of data:")
print(df.head())
print("\nDataset info:")
df.info()
print("\nQuick statistics:")
print(df.describe())

# Clean data
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Quantity"] = df["Quantity"].fillna(0).astype(int)
df["Price"] = df["Price"].fillna(0.0).astype(float)

# Add new column
df["Total"] = df["Quantity"] * df["Price"]

# Remove duplicates
df = df.drop_duplicates()

# Clean text in Product column
df["Product"] = df["Product"].str.strip().str.title()

# Show cleaned data
print("\nCleaned data:")
print(df.head())

# Save cleaned data
df.to_csv("sales_cleaned.csv", index=False)
print("\n✅ Cleaned data saved to 'sales_cleaned.csv'")
