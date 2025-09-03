import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

# -----------------------------
# 1) Load your cleaned data
# -----------------------------
df = pd.read_csv("sales_cleaned.csv")

# -----------------------------
# 2) Create Excel report
# -----------------------------
excel_file = "hotel_sales_report.xlsx"
with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    # Raw cleaned data
    df.to_excel(writer, sheet_name="Cleaned Data", index=False)
    
    # Summary by Product
    sales_by_product = df.groupby("Product")["Total"].sum().reset_index()
    sales_by_product.to_excel(writer, sheet_name="By Product", index=False)
    
    # Summary by Customer
    sales_by_customer = df.groupby("Customer")["Total"].sum().reset_index()
    sales_by_customer.to_excel(writer, sheet_name="By Customer", index=False)
    
    # Summary by Date
    sales_by_date = df.groupby("Date")["Total"].sum().reset_index()
    sales_by_date.to_excel(writer, sheet_name="By Date", index=False)

# -----------------------------
# 3) Insert charts into Excel
# -----------------------------
wb = load_workbook(excel_file)

# Insert into "By Product"
ws1 = wb["By Product"]
img1 = Image("chart_sales_by_product.png")
ws1.add_image(img1, "E2")   # Position at cell E2

# Insert into "By Customer"
ws2 = wb["By Customer"]
img2 = Image("chart_sales_by_customer.png")
ws2.add_image(img2, "E2")

# Insert into "By Date"
ws3 = wb["By Date"]
img3 = Image("chart_sales_by_date.png")
ws3.add_image(img3, "E2")

# Save final report
wb.save(excel_file)

print("✅ Final report generated:", excel_file)
