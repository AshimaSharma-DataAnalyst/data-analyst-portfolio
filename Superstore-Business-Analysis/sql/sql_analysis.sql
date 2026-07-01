-- =========================================================
-- 🛒 PROJECT: SUPERSTORE SALES & PROFIT ANALYSIS
-- =========================================================
-- Objective:
-- Analyze sales, profit, customer behavior, and operational
-- efficiency to identify growth opportunities and risks.
-- =========================================================


-- =========================================================
-- DATABASE SETUP
-- =========================================================

CREATE DATABASE IF NOT EXISTS sales_project;
USE sales_project;

-- Preview Data
SELECT * FROM orders LIMIT 10;

-- Total Records
SELECT COUNT(*) AS total_orders FROM orders;


-- =========================================================
-- 1. OVERALL BUSINESS PERFORMANCE
-- =========================================================

SELECT 
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_percent
FROM orders;


-- =========================================================
-- 2. SALES BY CATEGORY
-- =========================================================

SELECT 
    Category,
    ROUND(SUM(Sales), 2) AS total_sales
FROM orders
GROUP BY Category
ORDER BY total_sales DESC;


-- =========================================================
-- 3. PROFIT BY CATEGORY
-- =========================================================

SELECT 
    Category,
    ROUND(SUM(Profit), 2) AS total_profit
FROM orders
GROUP BY Category
ORDER BY total_profit DESC;


-- =========================================================
-- 4. PROFIT MARGIN ANALYSIS BY CATEGORY
-- =========================================================

SELECT 
    Category,
    ROUND(SUM(Sales), 2) AS sales,
    ROUND(SUM(Profit), 2) AS profit,
    ROUND((SUM(Profit)/SUM(Sales))*100, 2) AS profit_margin
FROM orders
GROUP BY Category
ORDER BY profit_margin ASC;


-- =========================================================
-- 5. TOP 5 SUB-CATEGORIES BY SALES
-- =========================================================

SELECT 
    `Sub-Category`,
    ROUND(SUM(Sales), 2) AS total_sales
FROM orders
GROUP BY `Sub-Category`
ORDER BY total_sales DESC
LIMIT 5;


-- =========================================================
-- 6. LOSS-MAKING SUB-CATEGORIES
-- =========================================================

SELECT 
    `Sub-Category`,
    ROUND(SUM(Profit), 2) AS total_profit
FROM orders
GROUP BY `Sub-Category`
HAVING SUM(Profit) < 0
ORDER BY total_profit ASC;


-- =========================================================
-- 7. YEAR-WISE SALES TREND
-- =========================================================

SELECT 
    YEAR(`Order Date`) AS year,
    ROUND(SUM(Sales), 2) AS total_sales
FROM orders
GROUP BY year
ORDER BY year;


-- =========================================================
-- 8. REGIONAL PERFORMANCE
-- =========================================================

SELECT 
    Region,
    ROUND(SUM(Sales), 2) AS sales,
    ROUND(SUM(Profit), 2) AS profit
FROM orders
GROUP BY Region
ORDER BY profit ASC;


-- =========================================================
-- 9. TOP 10 STATES BY SALES
-- =========================================================

SELECT 
    State,
    ROUND(SUM(Sales), 2) AS total_sales
FROM orders
GROUP BY State
ORDER BY total_sales DESC
LIMIT 10;


-- =========================================================
-- 10. DISCOUNT VS PROFITABILITY ANALYSIS
-- =========================================================

SELECT 
    Discount,
    COUNT(*) AS total_orders,
    ROUND(AVG(Profit), 2) AS avg_profit,
    ROUND(SUM(Profit), 2) AS total_profit
FROM orders
GROUP BY Discount
ORDER BY Discount;


-- =========================================================
-- 11. SHIPPING PERFORMANCE
-- =========================================================

SELECT 
    `Ship Mode`,
    ROUND(AVG(DATEDIFF(`Ship Date`, `Order Date`)), 2) AS avg_shipping_days
FROM orders
GROUP BY `Ship Mode`
ORDER BY avg_shipping_days;


-- =========================================================
-- 12. CUSTOMER SEGMENTATION ANALYSIS
-- =========================================================

SELECT 
    `Customer Name`,
    COUNT(*) AS total_orders,
    ROUND(SUM(Sales),2) AS total_spent,
    CASE 
        WHEN SUM(Sales) > 10000 THEN 'High Value'
        WHEN SUM(Sales) > 5000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS customer_segment
FROM orders
GROUP BY `Customer Name`
ORDER BY total_spent DESC;


-- =========================================================
-- 13. REPEAT CUSTOMERS (RETENTION)
-- =========================================================

SELECT 
    `Customer Name`,
    COUNT(DISTINCT `Order ID`) AS order_count
FROM orders
GROUP BY `Customer Name`
HAVING order_count > 1
ORDER BY order_count DESC;


-- =========================================================
-- 14. TOP 10 PRODUCTS BY SALES
-- =========================================================

SELECT 
    `Product Name`,
    ROUND(SUM(Sales), 2) AS total_sales
FROM orders
GROUP BY `Product Name`
ORDER BY total_sales DESC
LIMIT 10;


-- =========================================================
-- 15. LOSS-MAKING PRODUCTS
-- =========================================================

SELECT 
    `Product Name`,
    ROUND(SUM(Profit), 2) AS total_profit
FROM orders
GROUP BY `Product Name`
HAVING SUM(Profit) < 0
ORDER BY total_profit ASC;


-- =========================================================
-- FINAL BUSINESS RECOMMENDATIONS
-- =========================================================

-- 1. Reduce high discount levels as they negatively impact profitability
-- 2. Focus on high-margin categories instead of just high sales categories
-- 3. Re-evaluate loss-making sub-categories and products
-- 4. Retain high-value customers through targeted strategies
-- 5. Improve performance in low-profit regions
-- 6. Optimize shipping strategies balancing speed and cost

-- =========================================================
-- END OF PROJECT
-- =========================================================