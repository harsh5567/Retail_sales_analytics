# Retail Sales Analytics Project

## 1. Project Overview

This project analyzes retail sales data to understand sales,
profitability, customer behavior, product performance, and
business trends.

## 2. Business Objective

The main objectives of this project are:

- Analyze overall sales and profit
- Identify top-performing products
- Compare city-wise performance
- Analyze customer segments
- Understand payment methods
- Analyze order status
- Identify monthly sales and profit trends
- Identify data-quality issues
- Build business-ready visualizations and dashboards

## 3. Dataset

Dataset: Retail Sales Dataset

Original Records: 1012

Cleaned Records: 982

Columns: 15

Main fields include:

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

## 4. Technology Stack

- Python
- Pandas
- Matplotlib
- MySQL
- SQL
- Power BI
- Git / GitHub

## 5. Data Cleaning

The dataset contained missing values, duplicate records,
inconsistent text values, invalid numeric values, and
inconsistent date formats.

The cleaning process included:

- Removing duplicate records
- Handling missing values
- Converting numeric columns
- Converting dates
- Standardizing text values
- Removing invalid quantities
- Removing invalid discounts
- Removing negative sales records

Negative profit records were retained because they can represent
legitimate business losses.

## 6. Data Validation

The cleaned dataset was validated using:

- Missing-value checks
- Duplicate checks
- Numeric validation
- Date validation
- Sales calculation validation
- Profit calculation validation
- Order_ID uniqueness checks
- Product-category consistency checks

## 7. Database

The cleaned dataset was loaded into MySQL.

Database:

retail_sales_db

Table:

retail_sales

## 8. Analysis

Business analysis was performed using SQL and Pandas.

Major analysis areas:

- Category performance
- City performance
- Product performance
- Customer segment performance
- Payment method analysis
- Order status analysis
- Monthly trends
- Profit margin analysis
- Top orders
- Discount analysis

## 9. Visualization

Matplotlib was used to create business charts including:

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

## 10. Data Quality Findings

The validation identified:

- 32 sales calculation mismatches
- 28 profit calculation mismatches
- 18 records with Unknown City
- 12 records with Unknown Product
- 5 negative-profit records

These issues were documented rather than automatically changing
potentially legitimate business data.

## 11. Project Outputs

The project produces:

- Cleaned dataset
- SQL database
- SQL analysis results
- Pandas analysis outputs
- Business KPI files
- Visualization charts
- Business documentation

## 12. KPI Results & Key Business Findings

### Overall Business KPIs

| KPI                 |        Result |
| ------------------- | ------------: |
| Total Orders        |           982 |
| Total Sales         | 22,990,853.63 |
| Total Cost          | 16,841,196.88 |
| Total Profit        |  6,228,301.06 |
| Total Quantity      |         4,463 |
| Average Order Value |     23,412.27 |
| Profit Margin       |        27.09% |

### Key Business Findings

* Electronics generated the highest total sales among the categories.
* Delhi recorded the highest total sales among the cities.
* Laptop was the highest-selling product by total sales.
* Consumer, Small Business, and Corporate segments all contributed significant sales.
* Completed orders represented the largest order-status group.
* Monthly sales and profit were analyzed across the complete 2025 period.

### Data Quality Observations

* 32 records had sales calculation mismatches.
* 28 records had profit calculation mismatches.
* 18 records contained Unknown City values.
* 12 records contained Unknown Product values.
* 5 records had negative profit values.
* Several products were associated with multiple categories and were flagged for further business review.

## 13. Limitations & Future Improvements

### Current Limitations

* The dataset is a synthetic retail dataset created for analytics practice.
* Some records contain data-quality issues that require business confirmation before correction.
* Sales and profit calculation mismatches were identified during validation.
* The current analysis is based on data from the year 2025.
* Real-time data integration is not included in the current version.

### Future Improvements

The project can be further improved by:

* Connecting Power BI directly to the MySQL database.
* Adding interactive business dashboards.
* Automating the data-cleaning pipeline.
* Adding scheduled data updates.
* Creating automated data-quality reports.
* Adding more historical sales data.
* Adding customer-level analysis and segmentation.
* Deploying the project as a complete business analytics solution.

## 14. Project Workflow

The project followed an end-to-end data analytics workflow:

1. **Project Setup**
   Created a professional folder structure and separated raw, cleaned, and processed data.

2. **Data Loading & Profiling**
   Loaded the raw CSV using Pandas and analyzed its structure, data types, missing values, duplicates, and inconsistencies.

3. **Data Cleaning**
   Cleaned missing values, duplicates, inconsistent text, dates, and invalid numeric records.

4. **Data Validation**
   Validated calculations, data types, unique identifiers, dates, quantities, discounts, and product-category relationships.

5. **Database Management**
   Loaded the cleaned dataset into MySQL and created a structured retail sales table.

6. **Business Analysis**
   Used SQL and Pandas to analyze sales, profit, products, cities, customers, payments, order status, and monthly trends.

7. **Business Metrics**
   Calculated KPIs such as total sales, total profit, average order value, profit margin, and sales/profit percentages.

8. **Data Visualization**
   Created analytical charts using Matplotlib to communicate important business trends and comparisons.

9. **Documentation**
   Documented the project process, findings, KPIs, data-quality issues, and limitations.

10. **Dashboard & Portfolio**
    The next stage is to build the Power BI dashboard and prepare the project for GitHub and portfolio presentation.


## 15. Conclusion

This Retail Sales Analytics project demonstrates an end-to-end data analytics workflow, starting from raw data and progressing through data cleaning, validation, database management, business analysis, KPI calculation, and visualization.

Python and Pandas were used for data preparation and analysis, MySQL was used for structured data storage and SQL analysis, and Matplotlib was used for data visualization.

The project also identified several data-quality issues and documented them instead of making unsupported business assumptions.

The next stage of the project is to build an interactive Power BI dashboard and prepare the project for version control and portfolio presentation.
