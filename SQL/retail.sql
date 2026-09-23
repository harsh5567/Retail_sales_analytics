CREATE DATABASE retail_sales_db;

USE retail_sales_db;

CREATE TABLE retail_sales (
    Order_ID VARCHAR(20),
    Order_Date DATE,
    Customer_ID VARCHAR(20),
    City VARCHAR(50),
    Category VARCHAR(50),
    Product VARCHAR(100),
    Quantity INT,
    Unit_Price DECIMAL(12,2),
    Discount DECIMAL(5,2),
    Sales DECIMAL(12,2),
    Cost DECIMAL(12,2),
    Profit DECIMAL(12,2),
    Customer_Segment VARCHAR(30),
    Payment_Method VARCHAR(30),
    Order_Status VARCHAR(30)
);
SELECT COUNT(*) AS total_records
FROM retail_sales;

SELECT *
FROM retail_sales
LIMIT 5;

SELECT COUNT(DISTINCT Order_ID) AS unique_orders
FROM retail_sales;

SELECT
    Order_ID,
    Order_Date,
    Customer_ID,
    Quantity,
    Unit_Price,
    Discount,
    Sales,
    Cost,
    Profit
FROM retail_sales
LIMIT 5;

SELECT
    SUM(Sales) AS total_sales,
    SUM(Cost) AS total_cost,
    SUM(Profit) AS total_profit,
    AVG(Sales) AS average_sales
FROM retail_sales;

SELECT
    Category,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM retail_sales
GROUP BY Category
ORDER BY total_sales DESC;

SELECT
    City,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM retail_sales
GROUP BY City
ORDER BY total_sales DESC;

SELECT
    Customer_Segment,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit,
    COUNT(Order_ID) AS total_orders
FROM retail_sales
GROUP BY Customer_Segment
ORDER BY total_sales DESC;

SELECT
    Payment_Method,
    COUNT(Order_ID) AS total_orders,
    SUM(Sales) AS total_sales
FROM retail_sales
GROUP BY Payment_Method
ORDER BY total_sales DESC;

SELECT
    Order_Status,
    COUNT(Order_ID) AS total_orders,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM retail_sales
GROUP BY Order_Status
ORDER BY total_sales DESC;

SELECT
    MONTH(Order_Date) AS month_number,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM retail_sales
GROUP BY MONTH(Order_Date)
ORDER BY month_number;

SELECT
    City,
    SUM(Sales) AS total_sales
FROM retail_sales
GROUP BY City
HAVING SUM(Sales) > 3000000
ORDER BY total_sales DESC;

SELECT
    Order_ID,
    Sales,
    CASE
        WHEN Sales < 10000 THEN 'Low'
        WHEN Sales <= 30000 THEN 'Medium'
        ELSE 'High'
    END AS sales_category
FROM retail_sales
LIMIT 20;

SELECT
    CASE
        WHEN Sales < 10000 THEN 'Low'
        WHEN Sales <= 30000 THEN 'Medium'
        ELSE 'High'
    END AS sales_category,
    COUNT(*) AS total_orders,
    SUM(Sales) AS total_sales
FROM retail_sales
GROUP BY
    CASE
        WHEN Sales < 10000 THEN 'Low'
        WHEN Sales <= 30000 THEN 'Medium'
        ELSE 'High'
    END
ORDER BY total_sales DESC;

SELECT
    Order_ID,
    Sales,
    City,
    Product
FROM retail_sales
WHERE Sales > (
    SELECT AVG(Sales)
    FROM retail_sales
)
ORDER BY Sales DESC;

SELECT
    COUNT(*) AS orders_above_average
FROM retail_sales
WHERE Sales > (
    SELECT AVG(Sales)
    FROM retail_sales
);

SELECT
    r.Order_ID,
    r.City,
    r.Sales
FROM retail_sales r
WHERE r.Sales > (
    SELECT AVG(r2.Sales)
    FROM retail_sales r2
    WHERE r2.City = r.City
)
ORDER BY r.City, r.Sales DESC

WITH ranked_orders AS (
    SELECT
        Order_ID,
        City,
        Product,
        Sales,
        RANK() OVER (
            PARTITION BY City
            ORDER BY Sales DESC
        ) AS sales_rank
    FROM retail_sales
)
SELECT
    Order_ID,
    City,
    Product,
    Sales,
    sales_rank
FROM ranked_orders
WHERE sales_rank <= 3
ORDER BY City, sales_rank;

SELECT
    City,
    Customer_Segment,
    COUNT(Order_ID) AS total_orders,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM retail_sales
GROUP BY
    City,
    Customer_Segment
ORDER BY
    City,
    total_sales DESC;
    
    SELECT
    City,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit,
    ROUND(
        (SUM(Profit) / SUM(Sales)) * 100,
        2
    ) AS profit_margin_percentage
FROM retail_sales
GROUP BY City
ORDER BY profit_margin_percentage DESC;

SELECT
    YEAR(Order_Date) AS order_year,
    MONTH(Order_Date) AS month_number,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit,
    ROUND(
        (SUM(Profit) / SUM(Sales)) * 100,
        2
    ) AS profit_margin_percentage
FROM retail_sales
GROUP BY
    YEAR(Order_Date),
    MONTH(Order_Date)
ORDER BY
    order_year,
    month_number;
    
    SELECT
    Product,
    SUM(Quantity) AS total_quantity,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit,
    ROUND(
        (SUM(Profit) / SUM(Sales)) * 100,
        2
    ) AS profit_margin_percentage
FROM retail_sales
GROUP BY Product
ORDER BY total_sales DESC;

SELECT
    Order_Status,
    COUNT(Order_ID) AS total_orders,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit,
    ROUND(
        (SUM(Profit) / SUM(Sales)) * 100,
        2
    ) AS profit_margin_percentage
FROM retail_sales
GROUP BY Order_Status
ORDER BY total_sales DESC;
