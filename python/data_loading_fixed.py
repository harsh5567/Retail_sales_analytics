import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ==================================================
# 1. LOAD RAW DATA
# ==================================================

df = pd.read_csv(r"data\raw\retail_sales.csv")

# ==================================================
# 2. INITIAL DATA PROFILING
# ==================================================

sample_records = df.head()
print("Sample records:")
print(sample_records)

shape = df.shape
print("\nShape:")
print(shape)

column_names = df.columns
print("\nColumn names:")
print(column_names)

data_types = df.dtypes
print("\nData types:")
print(data_types)

missing_values = df.isnull().sum()
print("\nMissing values:")
print(missing_values)

duplicate_records = df.duplicated().sum()
print("\nDuplicate records:")
print(duplicate_records)

statistics = df.describe()
print("\nStatistics:")
print(statistics)

# ==================================================
# 3. CREATE WORKING COPY
# ==================================================

# Keep the raw DataFrame unchanged.
cleaned_df = df.copy()

# ==================================================
# 4. REMOVE EXACT DUPLICATES
# ==================================================

cleaned_df = cleaned_df.drop_duplicates()

print("\nShape after removing duplicates:")
print(cleaned_df.shape)

# ==================================================
# 5. CONVERT DATA TYPES
# ==================================================

numeric_columns = [
    "Quantity",
    "Unit_Price",
    "Discount",
    "Sales",
    "Cost",
    "Profit"
]

for column in numeric_columns:
    cleaned_df[column] = pd.to_numeric(
        cleaned_df[column],
        errors="coerce"
    )

# Convert Order_Date before checking/removing invalid dates.
cleaned_df["Order_Date"] = pd.to_datetime(
    cleaned_df["Order_Date"],
    errors="coerce"
)

print("\nData types after conversion:")
print(cleaned_df.dtypes)

# ==================================================
# 6. HANDLE MISSING VALUES
# ==================================================

for column in numeric_columns:
    cleaned_df[column] = cleaned_df[column].fillna(
        cleaned_df[column].median()
    )

text_columns = [
    "City",
    "Product",
    "Customer_Segment",
    "Payment_Method"
]

for column in text_columns:
    cleaned_df[column] = cleaned_df[column].fillna("Unknown")

# Order_Date is important for time-based analysis.
# Rows with missing/invalid dates are removed.
cleaned_df = cleaned_df.dropna(subset=["Order_Date"])

print("\nMissing values after handling:")
print(cleaned_df.isnull().sum())

# ==================================================
# 7. CHECK INVALID NUMERIC VALUES
# ==================================================

negative_values = {
    "Quantity": (cleaned_df["Quantity"] < 0).sum(),
    "Discount": (cleaned_df["Discount"] < 0).sum(),
    "Sales": (cleaned_df["Sales"] < 0).sum(),
    "Cost": (cleaned_df["Cost"] < 0).sum(),
    "Profit": (cleaned_df["Profit"] < 0).sum()
}

print("\nNegative values:")
print(negative_values)

# ==================================================
# 8. REMOVE INVALID QUANTITY
# ==================================================

cleaned_df = cleaned_df[
    cleaned_df["Quantity"] >= 0
]

# ==================================================
# 9. REMOVE INVALID DISCOUNT
# ==================================================

cleaned_df = cleaned_df[
    (cleaned_df["Discount"] >= 0) &
    (cleaned_df["Discount"] <= 1)
]

# ==================================================
# 10. REMOVE INVALID SALES
# ==================================================

cleaned_df = cleaned_df[
    cleaned_df["Sales"] >= 0
]

# Negative Profit is NOT removed.
# A negative profit can represent a legitimate business loss.

# ==================================================
# 11. STANDARDIZE CITY
# ==================================================

cleaned_df["City"] = (
    cleaned_df["City"]
    .str.strip()
    .str.title()
)

cleaned_df["City"] = cleaned_df["City"].replace({
    "Bengaluru": "Bangalore",
    "Banglore":"Bangalore"
})

print("\nCity values after standardization:")
print(cleaned_df["City"].value_counts())

# ==================================================
# 12. STANDARDIZE CATEGORY
# ==================================================

cleaned_df["Category"] = (
    cleaned_df["Category"]
    .str.strip()
    .str.title()
)

print("\nCategory values after standardization:")
print(cleaned_df["Category"].value_counts())

# ==================================================
# 13. STANDARDIZE PRODUCT
# ==================================================

cleaned_df["Product"] = cleaned_df["Product"].str.strip()

product_mapping = {
    "laptop": "Laptop",
    "Tshirt": "T-Shirt",
    "MOUSE": "Mouse",
    "mouse": "Mouse",
    "Printer paper": "Printer Paper"
}

cleaned_df["Product"] = cleaned_df["Product"].replace(
    product_mapping
)

print("\nProduct values after standardization:")
print(cleaned_df["Product"].value_counts())

# ==================================================
# 14. FINAL VALIDATION
# ==================================================

missing_values_after_cleaning = cleaned_df.isnull().sum()
print("\nMissing values after cleaning:")
print(missing_values_after_cleaning)

duplicate_count = cleaned_df.duplicated().sum()
print("\nDuplicate rows after cleaning:")
print(duplicate_count)

invalid_numeric_values = {
    "Quantity": (cleaned_df["Quantity"] < 0).sum(),
    "Discount": (
        (cleaned_df["Discount"] < 0) |
        (cleaned_df["Discount"] > 1)
    ).sum(),
    "Sales": (cleaned_df["Sales"] < 0).sum(),
    "Cost": (cleaned_df["Cost"] < 0).sum()
}

print("\nInvalid numeric values after cleaning:")
print(invalid_numeric_values)

negative_profit_count = (
    cleaned_df["Profit"] < 0
).sum()

print("\nNegative Profit records retained:")
print(negative_profit_count)

invalid_dates = cleaned_df["Order_Date"].isna().sum()
print("\nInvalid dates after cleaning:")
print(invalid_dates)

print("\nFinal data types:")
print(cleaned_df.dtypes)

print("\nFinal shape:")
print(cleaned_df.shape)

expected_sales = (
    cleaned_df["Quantity"] *
    cleaned_df["Unit_Price"]*
    (1-cleaned_df["Discount"])
)

sales_difference = (
    cleaned_df["Sales"] - expected_sales
).abs()

sales_mismatch = cleaned_df[
    sales_difference>1
]

print("\nSales Mismatch record:")
print(
    sales_mismatch[
        ["Order_ID", "Quantity", "Unit_Price", "Discount",
         "Sales"]
    ]
)

mismatch_count = len(sales_mismatch)

total_records = len(cleaned_df)

mismatch_percentage = (mismatch_count / total_records) * 100

print("\nSales mismatch count:")
print(mismatch_count)

print("\nSales mismatch percentage:")
print(mismatch_percentage)

mismatch_summary=sales_mismatch[
        ["Order_ID", "Quantity", "Unit_Price", "Discount",
         "Sales"]]
print("\nsales mismatch summary:")
print(mismatch_summary.describe())

print("\nSales calculation difference")
print(sales_difference.describe())


expected_profit = (cleaned_df["Sales"] - cleaned_df["Cost"])

profit_difference = (
    cleaned_df["Profit"] - expected_profit
).abs()

print("\nProfit calculation difference")
print(profit_difference.describe())

profit_mismatch = cleaned_df[profit_difference > 1]

profit_mismatch_count = len(profit_mismatch)

profit_mismatch_percentage = (
    profit_mismatch_count / len(cleaned_df)
) * 100

print(profit_mismatch_count)
print(profit_mismatch_percentage)

duplicate_order_ids = cleaned_df["Order_ID"].duplicated().sum()

print("Duplicate Order_IDs:", duplicate_order_ids)

zero_quantity = (cleaned_df["Quantity"] == 0).sum()
print("Zero Quantity:", zero_quantity)

invalid_discount = (
    (cleaned_df["Discount"] < 0) |
    (cleaned_df["Discount"] > 1)
).sum()

print("Invalid Discount:", invalid_discount)

negative_cost = (cleaned_df["Cost"] < 0).sum()
print("Negative Cost:", negative_cost)

negative_sales = (cleaned_df["Sales"] < 0).sum()
print("Negative Sales:", negative_sales)

negative_profit = (cleaned_df["Profit"] < 0).sum()
print("Negative Profit:", negative_profit)

# Additional numeric and required-field validation

invalid_unit_price = (cleaned_df["Unit_Price"] <= 0).sum()

non_integer_quantity = (
    cleaned_df["Quantity"] % 1 != 0
).sum()

missing_order_id = cleaned_df["Order_ID"].isnull().sum()

missing_customer_id = cleaned_df["Customer_ID"].isnull().sum()

unknown_city = (
    cleaned_df["City"] == "Unknown"
).sum()

unknown_product = (
    cleaned_df["Product"] == "Unknown"
).sum()

print("Invalid Unit Price:", invalid_unit_price)
print("Non-integer Quantity:", non_integer_quantity)
print("Missing Order_ID:", missing_order_id)
print("Missing Customer_ID:", missing_customer_id)
print("Unknown City:", unknown_city)
print("Unknown Product:", unknown_product)

# Product and Category consistency validation

product_category_counts = (
    cleaned_df.groupby("Product")["Category"]
    .nunique()
)

inconsistent_products = product_category_counts[
    product_category_counts > 1
]

print("Products linked to multiple categories:")
print(inconsistent_products)

# Check Order Status values
order_status_counts = cleaned_df["Order_Status"].value_counts()

print("\nOrder Status values:")
print(order_status_counts)

# Date range validation

minimum_order_date = cleaned_df["Order_Date"].min()
maximum_order_date = cleaned_df["Order_Date"].max()

future_dates = (
    cleaned_df["Order_Date"] > pd.Timestamp.today()
).sum()

print("Minimum Order Date:", minimum_order_date)
print("Maximum Order Date:", maximum_order_date)
print("Future-dated records:", future_dates)

# Final data types check
print("\nFinal Data Types:")
print(cleaned_df.dtypes)

# ==================================================
# 15. SAVE CLEANED DATASET
# ==================================================

cleaned_file_path = r"data\cleaned\retail_sales_cleaned.csv"

cleaned_df.to_csv(
    cleaned_file_path,
    index=False
)

print("\nCleaned data saved successfully.")

category_analysis = (
    cleaned_df.groupby("Category")
    .agg(
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum"),
        total_orders=("Order_ID", "count")
    )
    .sort_values("total_sales", ascending=False)
)

print(category_analysis)

city_analysis = (
    cleaned_df.groupby("City")
    .agg(
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum"),
        total_orders=("Order_ID", "count")
    )
    .sort_values("total_sales", ascending=False)
)

print(city_analysis)

product_analysis = (
    cleaned_df.groupby("Product")
    .agg(
        total_quantity=("Quantity", "sum"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum"),
        total_orders=("Order_ID", "count")
    )
    .sort_values("total_sales", ascending=False)
)

print(product_analysis)

segment_analysis = (
    cleaned_df.groupby("Customer_Segment")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .sort_values("total_sales", ascending=False)
)

print(segment_analysis)

payment_analysis = (
    cleaned_df.groupby("Payment_Method")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .sort_values("total_sales", ascending=False)
)

print(payment_analysis)

status_analysis = (
    cleaned_df.groupby("Order_Status")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .sort_values("total_sales", ascending=False)
)

print(status_analysis)

monthly_analysis = (
    cleaned_df
    .assign(
        year=cleaned_df["Order_Date"].dt.year,
        month=cleaned_df["Order_Date"].dt.month
    )
    .groupby(["year", "month"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(["year", "month"])
)

print(monthly_analysis)

city_profitability = (
    cleaned_df.groupby("City")
    .agg(
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
)

city_profitability["profit_margin_percentage"] = (
    city_profitability["total_profit"]
    / city_profitability["total_sales"]
    * 100
).round(2)

city_profitability = city_profitability.sort_values(
    "profit_margin_percentage",
    ascending=False
)

print(city_profitability)

product_profitability = (
    cleaned_df.groupby("Product")
    .agg(
        total_quantity=("Quantity", "sum"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
)

product_profitability["profit_margin_percentage"] = (
    product_profitability["total_profit"]
    / product_profitability["total_sales"]
    * 100
).round(2)

product_profitability = product_profitability.sort_values(
    "total_sales",
    ascending=False
)

print(product_profitability)

payment_profitability = (
    cleaned_df.groupby("Payment_Method")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
)

payment_profitability["profit_margin_percentage"] = (
    payment_profitability["total_profit"]
    / payment_profitability["total_sales"]
    * 100
).round(2)

payment_profitability = payment_profitability.sort_values(
    "total_sales",
    ascending=False
)

print(payment_profitability)

status_profitability = (
    cleaned_df.groupby("Order_Status")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
)

status_profitability["profit_margin_percentage"] = (
    status_profitability["total_profit"]
    / status_profitability["total_sales"]
    * 100
).round(2)

status_profitability = status_profitability.sort_values(
    "total_sales",
    ascending=False
)

print(status_profitability)

segment_profitability = (
    cleaned_df.groupby("Customer_Segment")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
)

segment_profitability["profit_margin_percentage"] = (
    segment_profitability["total_profit"]
    / segment_profitability["total_sales"]
    * 100
).round(2)

segment_profitability = segment_profitability.sort_values(
    "total_sales",
    ascending=False
)

print(segment_profitability)

city_segment_analysis = (
    cleaned_df.groupby(["City", "Customer_Segment"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["City", "total_sales"],
        ascending=[True, False]
    )
)

print(city_segment_analysis)

monthly_analysis["month_name"] = (
    pd.to_datetime(
        monthly_analysis["month"].astype(str) + "-2025",
        format="%m-%Y"
    )
    .dt.strftime("%B")
)

print(monthly_analysis)

top_orders = (
    cleaned_df[
        ["Order_ID", "City", "Product", "Customer_Segment", "Sales", "Profit"]
    ]
    .sort_values("Sales", ascending=False)
    .head(10)
)

print(top_orders)

top_profit_orders = (
    cleaned_df[
        ["Order_ID", "City", "Product", "Customer_Segment", "Sales", "Profit"]
    ]
    .sort_values("Profit", ascending=False)
    .head(10)
)

print(top_profit_orders)

loss_orders = (
    cleaned_df[
        ["Order_ID", "City", "Product", "Sales", "Cost", "Profit"]
    ]
    .sort_values("Profit")
)

print(loss_orders.head(10))

discount_analysis = (
    cleaned_df.groupby("Discount")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .sort_index()
)

discount_analysis["profit_margin_percentage"] = (
    discount_analysis["total_profit"]
    / discount_analysis["total_sales"]
    * 100
).round(2)

print(discount_analysis)

quantity_analysis = (
    cleaned_df.groupby("Quantity")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .sort_index()
)

print(quantity_analysis)

city_category_analysis = (
    cleaned_df.groupby(["City", "Category"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["City", "total_sales"],
        ascending=[True, False]
    )
)

print(city_category_analysis)

category_product_analysis = (
    cleaned_df.groupby(["Category", "Product"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Category", "total_sales"],
        ascending=[True, False]
    )
)

print(category_product_analysis)

payment_status_analysis = (
    cleaned_df.groupby(["Payment_Method", "Order_Status"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Payment_Method", "total_sales"],
        ascending=[True, False]
    )
)

print(payment_status_analysis)

city_status_analysis = (
    cleaned_df.groupby(["City", "Order_Status"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["City", "total_sales"],
        ascending=[True, False]
    )
)

print(city_status_analysis)

city_category_profitability = (
    cleaned_df.groupby(["City", "Category"])
    .agg(
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
)

city_category_profitability["profit_margin_percentage"] = (
    city_category_profitability["total_profit"]
    / city_category_profitability["total_sales"]
    * 100
).round(2)

city_category_profitability = city_category_profitability.sort_values(
    "total_sales",
    ascending=False
)

print(city_category_profitability)

category_segment_analysis = (
    cleaned_df.groupby(["Category", "Customer_Segment"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Category", "total_sales"],
        ascending=[True, False]
    )
)

print(category_segment_analysis)

city_payment_analysis = (
    cleaned_df.groupby(["City", "Payment_Method"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["City", "total_sales"],
        ascending=[True, False]
    )
)

print(city_payment_analysis)
city_segment_profitability = (
    cleaned_df.groupby(["City", "Customer_Segment"])
    .agg(
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
)

city_segment_profitability["profit_margin_percentage"] = (
    city_segment_profitability["total_profit"]
    / city_segment_profitability["total_sales"]
    * 100
).round(2)

city_segment_profitability = city_segment_profitability.sort_values(
    "total_sales",
    ascending=False
)

print(city_segment_profitability)

segment_payment_analysis = (
    cleaned_df.groupby(["Customer_Segment", "Payment_Method"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Customer_Segment", "total_sales"],
        ascending=[True, False]
    )
)

print(segment_payment_analysis)

category_payment_analysis = (
    cleaned_df.groupby(["Category", "Payment_Method"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Category", "total_sales"],
        ascending=[True, False]
    )
)

print(category_payment_analysis)

year_category_analysis = (
    cleaned_df
    .assign(
        year=cleaned_df["Order_Date"].dt.year
    )
    .groupby(["year", "Category"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["year", "total_sales"],
        ascending=[True, False]
    )
)

print(year_category_analysis)

year_city_analysis = (
    cleaned_df
    .assign(
        year=cleaned_df["Order_Date"].dt.year
    )
    .groupby(["year", "City"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["year", "total_sales"],
        ascending=[True, False]
    )
)

print(year_city_analysis)

product_segment_analysis = (
    cleaned_df.groupby(["Product", "Customer_Segment"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Product", "total_sales"],
        ascending=[True, False]
    )
)

print(product_segment_analysis)

product_status_analysis = (
    cleaned_df.groupby(["Product", "Order_Status"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Product", "total_sales"],
        ascending=[True, False]
    )
)

print(product_status_analysis)

product_city_analysis = (
    cleaned_df.groupby(["Product", "City"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Product", "total_sales"],
        ascending=[True, False]
    )
)

print(product_city_analysis)

segment_status_analysis = (
    cleaned_df.groupby(["Customer_Segment", "Order_Status"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Customer_Segment", "total_sales"],
        ascending=[True, False]
    )
)

print(segment_status_analysis)

discount_category_analysis = (
    cleaned_df.groupby(["Discount", "Category"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Discount", "total_sales"],
        ascending=[True, False]
    )
)

print(discount_category_analysis)

year_segment_analysis = (
    cleaned_df
    .assign(
        year=cleaned_df["Order_Date"].dt.year
    )
    .groupby(["year", "Customer_Segment"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["year", "total_sales"],
        ascending=[True, False]
    )
)

print(year_segment_analysis)

payment_category_analysis = (
    cleaned_df.groupby(["Payment_Method", "Category"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Payment_Method", "total_sales"],
        ascending=[True, False]
    )
)

print(payment_category_analysis)

category_status_analysis = (
    cleaned_df.groupby(["Category", "Order_Status"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Category", "total_sales"],
        ascending=[True, False]
    )
)

print(category_status_analysis)

city_discount_analysis = (
    cleaned_df.groupby(["City", "Discount"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["City", "total_sales"],
        ascending=[True, False]
    )
)

print(city_discount_analysis)

segment_discount_analysis = (
    cleaned_df.groupby(["Customer_Segment", "Discount"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Customer_Segment", "total_sales"],
        ascending=[True, False]
    )
)

print(segment_discount_analysis)

status_city_analysis = (
    cleaned_df.groupby(["Order_Status", "City"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
    .reset_index()
    .sort_values(
        ["Order_Status", "total_sales"],
        ascending=[True, False]
    )
)

print(status_city_analysis)

total_orders = cleaned_df["Order_ID"].nunique()
total_sales = cleaned_df["Sales"].sum()
total_cost = cleaned_df["Cost"].sum()
total_profit = cleaned_df["Profit"].sum()
total_quantity = cleaned_df["Quantity"].sum()

average_order_value = total_sales / total_orders
profit_margin_percentage = (total_profit / total_sales) * 100
average_discount_percentage = cleaned_df["Discount"].mean() * 100

business_kpis = {
    "Total Orders": total_orders,
    "Total Sales": total_sales,
    "Total Cost": total_cost,
    "Total Profit": total_profit,
    "Total Quantity": total_quantity,
    "Average Order Value": average_order_value,
    "Profit Margin (%)": profit_margin_percentage,
    "Average Discount (%)": average_discount_percentage
}

print(business_kpis)

status_kpis = (
    cleaned_df.groupby("Order_Status")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
)

status_kpis["order_percentage"] = (
    status_kpis["total_orders"]
    / status_kpis["total_orders"].sum()
    * 100
).round(2)

status_kpis["sales_percentage"] = (
    status_kpis["total_sales"]
    / status_kpis["total_sales"].sum()
    * 100
).round(2)

status_kpis["profit_margin_percentage"] = (
    status_kpis["total_profit"]
    / status_kpis["total_sales"]
    * 100
).round(2)

print(status_kpis)

category_kpis = (
    cleaned_df.groupby("Category")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum"),
        total_quantity=("Quantity", "sum")
    )
)

category_kpis["sales_percentage"] = (
    category_kpis["total_sales"]
    / category_kpis["total_sales"].sum()
    * 100
).round(2)

category_kpis["profit_margin_percentage"] = (
    category_kpis["total_profit"]
    / category_kpis["total_sales"]
    * 100
).round(2)

category_kpis = category_kpis.sort_values(
    "total_sales",
    ascending=False
)

print(category_kpis)

city_kpis = (
    cleaned_df.groupby("City")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum"),
        total_quantity=("Quantity", "sum")
    )
)

city_kpis["sales_percentage"] = (
    city_kpis["total_sales"]
    / city_kpis["total_sales"].sum()
    * 100
).round(2)

city_kpis["profit_margin_percentage"] = (
    city_kpis["total_profit"]
    / city_kpis["total_sales"]
    * 100
).round(2)

city_kpis = city_kpis.sort_values(
    "total_sales",
    ascending=False
)

print(city_kpis)

product_kpis = (
    cleaned_df.groupby("Product")
    .agg(
        total_orders=("Order_ID", "count"),
        total_quantity=("Quantity", "sum"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
)

product_kpis["sales_percentage"] = (
    product_kpis["total_sales"]
    / product_kpis["total_sales"].sum()
    * 100
).round(2)

product_kpis["profit_margin_percentage"] = (
    product_kpis["total_profit"]
    / product_kpis["total_sales"]
    * 100
).round(2)

product_kpis = product_kpis.sort_values(
    "total_sales",
    ascending=False
)

print(product_kpis)

segment_kpis = (
    cleaned_df.groupby("Customer_Segment")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
)

segment_kpis["sales_percentage"] = (
    segment_kpis["total_sales"]
    / segment_kpis["total_sales"].sum()
    * 100
).round(2)

segment_kpis["profit_margin_percentage"] = (
    segment_kpis["total_profit"]
    / segment_kpis["total_sales"]
    * 100
).round(2)

segment_kpis = segment_kpis.sort_values(
    "total_sales",
    ascending=False
)

print(segment_kpis)

payment_kpis = (
    cleaned_df.groupby("Payment_Method")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
)

payment_kpis["sales_percentage"] = (
    payment_kpis["total_sales"]
    / payment_kpis["total_sales"].sum()
    * 100
).round(2)

payment_kpis["profit_margin_percentage"] = (
    payment_kpis["total_profit"]
    / payment_kpis["total_sales"]
    * 100
).round(2)

payment_kpis = payment_kpis.sort_values(
    "total_sales",
    ascending=False
)

print(payment_kpis)

monthly_kpis = (
    cleaned_df
    .assign(
        year=cleaned_df["Order_Date"].dt.year,
        month=cleaned_df["Order_Date"].dt.month
    )
    .groupby(["year", "month"])
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum"),
        total_quantity=("Quantity", "sum")
    )
    .reset_index()
)

monthly_kpis["profit_margin_percentage"] = (
    monthly_kpis["total_profit"]
    / monthly_kpis["total_sales"]
    * 100
).round(2)

monthly_kpis["average_order_value"] = (
    monthly_kpis["total_sales"]
    / monthly_kpis["total_orders"]
).round(2)

print(monthly_kpis)

business_summary = pd.DataFrame({
    "Metric": [
        "Total Orders",
        "Total Sales",
        "Total Cost",
        "Total Profit",
        "Total Quantity",
        "Average Order Value",
        "Profit Margin (%)",
        "Average Discount (%)"
    ],
    "Value": [
        total_orders,
        total_sales,
        total_cost,
        total_profit,
        total_quantity,
        round(average_order_value, 2),
        round(profit_margin_percentage, 2),
        round(average_discount_percentage, 2)
    ]
})

print(business_summary)

top_products = (
    product_kpis
    .sort_values("total_sales", ascending=False)
    .head(5)
)

top_cities = (
    city_kpis
    .sort_values("total_sales", ascending=False)
    .head(5)
)

print("Top 5 Products:")
print(top_products)

print("\nTop 5 Cities:")
print(top_cities)

top_profit_products = (
    product_kpis
    .sort_values("total_profit", ascending=False)
    .head(5)
)

top_profit_cities = (
    city_kpis
    .sort_values("total_profit", ascending=False)
    .head(5)
)

print("Top 5 Products by Profit:")
print(top_profit_products)

print("\nTop 5 Cities by Profit:")
print(top_profit_cities)

loss_analysis = (
    cleaned_df[cleaned_df["Profit"] < 0]
    .groupby("Product")
    .agg(
        loss_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_cost=("Cost", "sum"),
        total_profit=("Profit", "sum")
    )
    .sort_values("total_profit")
)

print(loss_analysis)

total_orders = cleaned_df["Order_ID"].nunique()

returned_orders = (
    cleaned_df["Order_Status"] == "Returned"
).sum()

cancelled_orders = (
    cleaned_df["Order_Status"] == "Cancelled"
).sum()

returned_rate = (
    returned_orders / total_orders * 100
)

cancelled_rate = (
    cancelled_orders / total_orders * 100
)

return_cancel_summary = {
    "Total Orders": total_orders,
    "Returned Orders": returned_orders,
    "Returned Rate (%)": round(returned_rate, 2),
    "Cancelled Orders": cancelled_orders,
    "Cancelled Rate (%)": round(cancelled_rate, 2)
}

print(return_cancel_summary)

segment_kpis["order_percentage"] = (
    segment_kpis["total_orders"]
    / segment_kpis["total_orders"].sum()
    * 100
).round(2)

segment_kpis["profit_percentage"] = (
    segment_kpis["total_profit"]
    / segment_kpis["total_profit"].sum()
    * 100
).round(2)

segment_kpis = segment_kpis.sort_values(
    "total_profit",
    ascending=False
)

print(segment_kpis)

discount_kpis = (
    cleaned_df.groupby("Discount")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum"),
        total_profit=("Profit", "sum")
    )
)

discount_kpis["sales_percentage"] = (
    discount_kpis["total_sales"]
    / discount_kpis["total_sales"].sum()
    * 100
).round(2)

discount_kpis["profit_margin_percentage"] = (
    discount_kpis["total_profit"]
    / discount_kpis["total_sales"]
    * 100
).round(2)

print(discount_kpis)

city_aov = (
    cleaned_df.groupby("City")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum")
    )
)

city_aov["average_order_value"] = (
    city_aov["total_sales"]
    / city_aov["total_orders"]
).round(2)

city_aov = city_aov.sort_values(
    "average_order_value",
    ascending=False
)

print(city_aov)

segment_aov = (
    cleaned_df.groupby("Customer_Segment")
    .agg(
        total_orders=("Order_ID", "count"),
        total_sales=("Sales", "sum")
    )
)

segment_aov["average_order_value"] = (
    segment_aov["total_sales"]
    / segment_aov["total_orders"]
).round(2)

segment_aov = segment_aov.sort_values(
    "average_order_value",
    ascending=False
)

print(segment_aov)

monthly_growth = monthly_kpis.copy()

monthly_growth["sales_growth_percentage"] = (
    monthly_growth["total_sales"]
    .pct_change()
    * 100
).round(2)

print(monthly_growth)

monthly_profit_growth = monthly_kpis.copy()

monthly_profit_growth["profit_growth_percentage"] = (
    monthly_profit_growth["total_profit"]
    .pct_change()
    * 100
).round(2)

print(monthly_profit_growth)

monthly_cumulative = monthly_kpis.copy()

monthly_cumulative["cumulative_sales"] = (
    monthly_cumulative["total_sales"].cumsum()
)

monthly_cumulative["cumulative_profit"] = (
    monthly_cumulative["total_profit"].cumsum()
)

print(monthly_cumulative)

overall_performance = {
    "Total Orders": total_orders,
    "Total Sales": round(total_sales, 2),
    "Total Cost": round(total_cost, 2),
    "Total Profit": round(total_profit, 2),
    "Total Quantity": total_quantity,
    "Average Order Value": round(average_order_value, 2),
    "Profit Margin (%)": round(profit_margin_percentage, 2),
    "Average Discount (%)": round(average_discount_percentage, 2),
    "Returned Rate (%)": round(returned_rate, 2),
    "Cancelled Rate (%)": round(cancelled_rate, 2)
}

overall_performance_df = pd.DataFrame(
    list(overall_performance.items()),
    columns=["Metric", "Value"]
)

print(overall_performance_df)

best_category = category_kpis["total_sales"].idxmax()
lowest_category = category_kpis["total_sales"].idxmin()

best_city = city_kpis["total_sales"].idxmax()
lowest_city = city_kpis["total_sales"].idxmin()

best_product = product_kpis["total_sales"].idxmax()
lowest_product = product_kpis["total_sales"].idxmin()

best_profit_product = product_kpis["total_profit"].idxmax()
best_profit_city = city_kpis["total_profit"].idxmax()

business_highlights = {
    "Highest Sales Category": best_category,
    "Lowest Sales Category": lowest_category,
    "Highest Sales City": best_city,
    "Lowest Sales City": lowest_city,
    "Highest Sales Product": best_product,
    "Lowest Sales Product": lowest_product,
    "Highest Profit Product": best_profit_product,
    "Highest Profit City": best_profit_city
}

print(business_highlights)

data_quality_findings = {
    "Sales Mismatches": 32,
    "Sales Mismatch Percentage": 3.26,
    "Profit Mismatches": 28,
    "Profit Mismatch Percentage": 2.85,
    "Unknown Cities": int((cleaned_df["City"] == "Unknown").sum()),
    "Unknown Products": int((cleaned_df["Product"] == "Unknown").sum()),
    "Negative Profit Records": int((cleaned_df["Profit"] < 0).sum())
}

print(data_quality_findings)

business_summary.to_csv(
    r"outputs\business_summary.csv",
    index=False
)

monthly_kpis.to_csv(
    r"outputs\monthly_kpis.csv",
    index=False
)

category_kpis.to_csv(
    r"outputs\category_kpis.csv"
)

city_kpis.to_csv(
    r"outputs\city_kpis.csv"
)

product_kpis.to_csv(
    r"outputs\product_kpis.csv"
)

segment_kpis.to_csv(
    r"outputs\segment_kpis.csv"
)

payment_kpis.to_csv(
    r"outputs\payment_kpis.csv"
)

status_kpis.to_csv(
    r"outputs\status_kpis.csv"
)

print("Phase 8 business outputs saved successfully.")

# MATPLOTLIB

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_kpis["month"],
    monthly_kpis["total_sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(monthly_kpis["month"])

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_kpis["month"],
    monthly_kpis["total_profit"],
    marker="o"
)

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.xticks(monthly_kpis["month"])

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.bar(
    city_kpis.index,
    city_kpis["total_sales"]
)

plt.title("City-wise Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

plt.bar(
    product_kpis.index,
    product_kpis["total_profit"]
)

plt.title("Product-wise Profit")
plt.xlabel("Product")
plt.ylabel("Total Profit")
plt.xticks(rotation=60)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.bar(
    category_kpis.index,
    category_kpis["profit_margin_percentage"]
)

plt.title("Profit Margin by Category")
plt.xlabel("Category")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=20)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.bar(
    city_kpis.index,
    city_kpis["profit_margin_percentage"]
)

plt.title("Profit Margin by City")
plt.xlabel("City")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

status_counts = cleaned_df["Order_Status"].value_counts()

plt.bar(
    status_counts.index,
    status_counts.values
)

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

plt.bar(
    segment_kpis.index,
    segment_kpis["total_sales"]
)

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

plt.bar(
    payment_kpis.index,
    payment_kpis["total_sales"]
)

plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_kpis["month"],
    monthly_kpis["total_sales"],
    marker="o",
    label="Sales"
)

plt.plot(
    monthly_kpis["month"],
    monthly_kpis["total_profit"],
    marker="o",
    label="Profit"
)

plt.title("Monthly Sales vs Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(monthly_kpis["month"])
plt.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_kpis["month"],
    monthly_kpis["profit_margin_percentage"],
    marker="o"
)

plt.title("Monthly Profit Margin")
plt.xlabel("Month")
plt.ylabel("Profit Margin (%)")
plt.xticks(monthly_kpis["month"])

plt.tight_layout()
plt.show()

top_profit_products = (
    product_kpis
    .sort_values("total_profit", ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

plt.bar(
    top_profit_products.index,
    top_profit_products["total_profit"]
)

plt.title("Top 10 Products by Profit")
plt.xlabel("Product")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

top_profit_cities = (
    city_kpis
    .sort_values("total_profit", ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

plt.bar(
    top_profit_cities.index,
    top_profit_cities["total_profit"]
)

plt.title("Top 10 Cities by Profit")
plt.xlabel("City")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

top_sales_orders = (
    cleaned_df[
        ["Order_ID", "Sales"]
    ]
    .sort_values("Sales", ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

plt.bar(
    top_sales_orders["Order_ID"],
    top_sales_orders["Sales"]
)

plt.title("Top 10 Orders by Sales")
plt.xlabel("Order ID")
plt.ylabel("Sales")
plt.xticks(rotation=60)

plt.tight_layout()
plt.show()

top_sales_products = (
    product_kpis
    .sort_values("total_sales", ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

plt.bar(
    top_sales_products.index,
    top_sales_products["total_sales"]
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.plot(
    discount_kpis.index * 100,
    discount_kpis["profit_margin_percentage"],
    marker="o"
)

plt.title("Discount vs Profit Margin")
plt.xlabel("Discount (%)")
plt.ylabel("Profit Margin (%)")

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

plt.scatter(
    cleaned_df["Quantity"],
    cleaned_df["Sales"]
)

plt.title("Quantity vs Sales")
plt.xlabel("Quantity")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

total_quantity = cleaned_df["Quantity"].sum()

print("Total Quantity:", total_quantity)