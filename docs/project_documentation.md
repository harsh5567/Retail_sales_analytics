# Retail Sales Analytics Project

## 1. Project Overview

This project is an end-to-end Retail Sales Analytics solution built to analyze sales, profit, customer behavior, product performance, city performance, payment methods, order status, and monthly business trends.

The project follows a professional data analytics workflow from raw data cleaning to SQL analysis, visualization, Power BI dashboarding, documentation, and GitHub version control.

## 2. Business Objective

- Analyze overall sales, cost, and profit
- Identify top-performing products
- Compare city-wise performance
- Analyze customer segments
- Understand payment methods and order status
- Identify monthly sales and profit trends
- Calculate important business KPIs
- Identify and document data-quality issues
- Build business-ready dashboards

## 3. Dataset

**Dataset:** Retail Sales Dataset

- Original Records: 1012
- Cleaned Records: 982
- Columns: 15
- Data Period: 2025

Main fields:

`Order_ID, Order_Date, Customer_ID, City, Category, Product, Quantity, Unit_Price, Discount, Sales, Cost, Profit, Customer_Segment, Payment_Method, Order_Status`

> **Important:** This is a synthetic dataset created for learning and portfolio purposes.

## 4. Technology Stack

- Python
- Pandas
- Matplotlib
- MySQL
- SQL
- Power BI
- Git
- GitHub

## 5. Project Structure

```text
Retail_Sales_Analytics/
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── processed/
├── python/
├── SQL/
├── Powerbi/
├── outputs/
└── docs/
```

## 6. Data Cleaning

The raw dataset contained missing values, duplicate records, inconsistent text values, invalid numeric values, and inconsistent date formats.

The cleaning process included:

- Removing duplicate records
- Handling missing values
- Converting numeric columns
- Converting dates to proper date format
- Standardizing city and product names
- Removing invalid quantities
- Removing invalid discount values
- Removing negative sales records
- Preserving negative-profit records because they may represent legitimate business losses

## 7. Data Validation

Validation included:

- Missing-value checks
- Duplicate checks
- Numeric validation
- Date validation
- Sales calculation validation
- Profit calculation validation
- Order_ID uniqueness checks
- Product-category consistency checks
- Order status validation

Important findings:

- Sales calculation mismatches: 32 records
- Profit calculation mismatches: 28 records
- Unknown City: 18 records
- Unknown Product: 12 records
- Negative Profit: 5 records

These issues were documented instead of making unsupported business assumptions.

## 8. MySQL Database

**Database:** `retail_sales_db`

**Table:** `retail_sales`

SQL analysis covered:

- Category performance
- City performance
- Product performance
- Customer segment analysis
- Payment method analysis
- Order status analysis
- Monthly sales and profit
- Profit margin analysis
- Top orders
- Discount analysis

## 9. Python & Pandas Analysis

Python and Pandas were used for:

- Data profiling
- Data cleaning
- Data validation
- Exploratory Data Analysis
- KPI calculations
- Business summaries
- Grouped analysis
- Trend analysis
- Output generation

## 10. Matplotlib Visualizations

Charts included:

- Monthly Sales Trend
- Monthly Profit Trend
- Category Sales
- Product Profit
- Profit Margin by Category
- Profit Margin by City
- Order Status Distribution
- Customer Segment Sales
- Payment Method Sales
- Monthly Sales vs Profit
- Top Products by Profit
- Top Cities by Profit
- Top Products by Sales
- Discount vs Profit Margin
- Quantity vs Sales

## 11. Power BI Dashboard

### Page 1 — Executive Overview

- Total Sales
- Total Profit
- Total Orders
- Average Order Value
- Monthly Sales Trend
- Sales by Category

### Page 2 — Sales & Profit Analysis

- Sales & Profit by Category
- Top 10 Products by Sales
- Top 10 Cities by Sales
- Monthly Sales vs Profit

### Page 3 — Customer & Order Analysis

- Sales by Customer Segment
- Orders by Status
- Sales by Payment Method
- Sales by Order Status

### Page 4 — Detailed Analysis

- Profit by City
- Profit by Product
- Profit Margin by Category
- Quantity by Category
- City, Category, and Order Status slicers

## 12. Overall Business KPIs

| KPI | Result |
|---|---:|
| Total Orders | 982 |
| Total Sales | 22,990,853.63 |
| Total Cost | 16,841,196.88 |
| Total Profit | 6,228,301.06 |
| Total Quantity | 4,463 |
| Average Order Value | 23,412.27 |
| Profit Margin | 27.09% |

## 13. Key Business Findings

- Electronics generated the highest total sales among the categories.
- Delhi recorded the highest total sales among the cities.
- Laptop generated the highest total sales among products.
- Consumer, Small Business, and Corporate segments all contributed significant sales.
- Completed orders represented the largest order-status group.
- Monthly sales and profit were analyzed across the complete 2025 period.

## 14. Limitations

- The dataset is synthetic and created for learning and portfolio purposes.
- Some records contain data-quality issues that require business confirmation before correction.
- Sales and profit calculation mismatches were identified during validation.
- The analysis is based on 2025 data.
- Real-time data integration is not included.

## 15. Future Improvements

- Automate the data-cleaning pipeline
- Add scheduled data updates
- Add automated data-quality reports
- Add more historical sales data
- Add customer-level segmentation
- Connect Power BI directly to MySQL
- Improve dashboard interactivity
- Deploy the project as a complete analytics solution

## 16. End-to-End Workflow

1. Project setup and folder structure
2. Raw data preservation
3. Data loading and profiling
4. Data cleaning
5. Data validation
6. MySQL database creation
7. SQL business analysis
8. Pandas EDA
9. KPI calculation
10. Matplotlib visualization
11. Power BI dashboard development
12. Documentation
13. Git version control
14. GitHub portfolio publishing

## 17. Conclusion

This project demonstrates an end-to-end data analytics workflow starting from raw retail data and progressing through data cleaning, validation, database management, SQL analysis, Python/Pandas analysis, KPI calculation, visualization, Power BI dashboarding, documentation, and GitHub version control.

The project also demonstrates the importance of identifying and documenting data-quality issues instead of making unsupported assumptions about business data.
