import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------
# 1) Load cleaned data
# ----------------------------------
df = pd.read_csv("sales_cleaned.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# ----------------------------------
# 2) Grouped summaries
# ----------------------------------
sales_by_product = df.groupby("Product")["Total"].sum().reset_index()
sales_by_customer = df.groupby("Customer")["Total"].sum().reset_index()
sales_by_date = df.groupby("Date")["Total"].sum().reset_index()

# ----------------------------------
# 3) Bar chart → Sales by Product
# ----------------------------------
plt.figure(figsize=(8, 5))
plt.bar(sales_by_product["Product"], sales_by_product["Total"], color="green")
plt.title("Total Sales by Product")
plt.xlabel("Product/Service")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("chart_sales_by_product.png")
plt.close()

# ----------------------------------
# 4) Bar chart → Sales by Customer
# ----------------------------------
plt.figure(figsize=(8, 5))
plt.bar(sales_by_customer["Customer"], sales_by_customer["Total"], color="blue")
plt.title("Total Sales by Customer")
plt.xlabel("Customer")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("chart_sales_by_customer.png")
plt.close()

# ----------------------------------
# 5) Line chart → Daily Sales Trend
# ----------------------------------
plt.figure(figsize=(8, 5))
plt.plot(sales_by_date["Date"], sales_by_date["Total"], marker="o", color="orange")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart_sales_by_date.png")
plt.close()

print("✅ Charts generated: chart_sales_by_product.png, chart_sales_by_customer.png, chart_sales_by_date.png")
