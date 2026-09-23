# Retail Sales Analytics

An end-to-end Retail Sales Analytics project built to analyze sales, profit, customers, products, cities, payments, and order trends.

## Project Overview

This project follows a professional data analytics workflow from raw data to business dashboard.

### Business Objectives

- Analyze overall sales and profit
- Identify top-performing products and cities
- Analyze customer segments
- Understand payment methods and order status
- Analyze monthly sales and profit trends
- Calculate business KPIs
- Identify and document data-quality issues
- Build an interactive Power BI dashboard

## Technology Stack

- Python
- Pandas
- Matplotlib
- MySQL
- SQL
- Power BI
- Git & GitHub

## Project Workflow

1. Project setup and data organization
2. Data loading and profiling
3. Data cleaning
4. Data validation
5. MySQL database management
6. SQL business analysis
7. Pandas exploratory data analysis
8. KPI calculation and business insights
9. Data visualization with Matplotlib
10. Power BI dashboard
11. Git/GitHub version control
12. Portfolio presentation

## Dataset

The project uses a synthetic retail sales dataset containing 1,012 original records and 15 columns.

Main fields:

- Order_ID
- Order_Date
- Customer_ID
- City
- Category
- Product
- Quantity
- Unit_Price
- Discount
- Sales
- Cost
- Profit
- Customer_Segment
- Payment_Method
- Order_Status

After cleaning, 982 records remained.

## Data Cleaning & Validation

The dataset contained missing values, duplicate records, inconsistent text values, invalid numeric values, and date-format inconsistencies.

Cleaning included:

- Removing duplicate records
- Handling missing values
- Converting numeric columns
- Converting dates
- Standardizing text values
- Removing invalid quantities
- Removing invalid discounts
- Removing negative sales

Negative-profit records were retained because they may represent legitimate business losses.

Validation identified:

- 32 sales calculation mismatches
- 28 profit calculation mismatches
- 18 Unknown City records
- 12 Unknown Product records
- 5 negative-profit records

These issues were documented rather than changed without business confirmation.

## Key Business KPIs

| KPI | Result |
| Total Orders | 982 |
| Total Sales | 22,990,853.63 |
| Total Cost | 16,841,196.88 |
| Total Profit | 6,228,301.06 |
| Total Quantity | 4,463 |
| Average Order Value | 23,412.27 |
| Profit Margin | 27.09% |

## Key Findings

- Electronics generated the highest total sales among the categories.
- Delhi recorded the highest total sales among the cities.
- Laptop was the highest-selling product by total sales.
- Consumer, Small Business, and Corporate segments all contributed significant sales.
- Completed orders represented the largest order-status group.
- Monthly sales and profit were analyzed across the complete 2025 period.

## Power BI Dashboard

The Power BI report contains four dashboard pages:

1. **Executive Overview**
   - KPI cards
   - Monthly Sales Trend
   - Sales by Category

2. **Sales & Profit Analysis**
   - Sales & Profit by Category
   - Top 10 Products by Sales
   - Top 10 Cities by Sales
   - Monthly Sales vs Profit

3. **Customer & Order Analysis**
   - Sales by Customer Segment
   - Orders by Status
   - Sales by Payment Method
   - Sales by Order Status

4. **Detailed Analysis**
   - Profit by City
   - Profit by Product
   - Profit Margin by Category
   - Quantity by Category
   - Interactive slicers

## Project Structure

```text
Retail_Sales_Analytics/
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── processed/
├── python/
├── sql/
├── powerbi/
├── outputs/
└── docs/
```

## Important Note

This is a synthetic dataset created for learning and portfolio purposes. It does not represent real company data.

## Future Improvements

- Automate the data-cleaning pipeline
- Add scheduled data updates
- Add automated data-quality reports
- Add more historical sales data
- Add customer-level segmentation
- Connect Power BI directly to MySQL
- Improve dashboard interactivity
