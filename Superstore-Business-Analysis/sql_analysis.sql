-- =========================================================
-- 🛒 PROJECT: SUPERSTORE SALES DATA ANALYSIS
-- =========================================================
-- Objective:
-- Analyze sales, profit, and customer trends to identify
-- business opportunities and loss-making areas.
-- =========================================================


-- =========================================================
-- DATABASE SETUP
-- =========================================================

CREATE DATABASE IF NOT EXISTS sales_project;
USE sales_project;
DESCRIBE orders;

-- Preview Data
SELECT * FROM orders LIMIT 10;

-- Total Records
SELECT COUNT(*) AS total_orders FROM orders;

-- =========================================================
-- 1. TOTAL SALES & PROFIT OVERVIEW
-- =========================================================
-- Business Question: What is the overall business performance?

SELECT 
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_percent
FROM orders;

-- Insight:
-- Provides a high-level view of business health.
-- A low profit margin may indicate high discounting or operational inefficiencies.

-- =========================================================
-- 2. SALES BY CATEGORY
-- =========================================================
-- Business Question: Which category generates the most revenue?

SELECT 
    Category,
    ROUND(SUM(Sales), 2) AS total_sales
FROM orders
GROUP BY Category
ORDER BY total_sales DESC;

-- Insight:
-- Helps identify high-performing categories contributing to revenue.

-- =========================================================
-- 3. PROFIT BY CATEGORY
-- =========================================================
-- Business Question: Which category is most profitable?

SELECT 
    Category,
    ROUND(SUM(Profit), 2) AS total_profit
FROM orders
GROUP BY Category
ORDER BY total_profit DESC;

-- Insight:
-- High sales does not always mean high profit.
-- Some categories may require pricing strategy adjustments.


-- =========================================================
-- 4. TOP 5 SUB-CATEGORIES BY SALES
-- =========================================================
-- Business Question: Which products perform best?

SELECT 
    `Sub-Category`,
    ROUND(SUM(Sales), 2) AS total_sales
FROM orders
GROUP BY `Sub-Category`
ORDER BY total_sales DESC
LIMIT 5;

-- Insight:
-- Top-performing sub-categories drive major revenue.
-- These should be prioritized in marketing and inventory.


-- =========================================================
-- 5. LOSS-MAKING SUB-CATEGORIES
-- =========================================================
-- Business Question: Which sub-categories are causing losses?

SELECT 
    `Sub-Category`,
    ROUND(SUM(Profit), 2) AS total_profit
FROM orders
GROUP BY `Sub-Category`
HAVING SUM(Profit) < 0
ORDER BY total_profit ASC;

-- Insight:
-- Some sub-categories generate revenue but are not profitable.
-- Requires cost optimization or pricing revision.


-- =========================================================
-- 6. YEAR-WISE SALES TREND
-- =========================================================
-- Business Question: How is the business growing over time?

SELECT 
    YEAR(`Order Date`) AS year,
    ROUND(SUM(Sales), 2) AS total_sales
FROM orders
GROUP BY year
ORDER BY year;

-- Insight:
-- Shows growth trends and helps identify business expansion or decline.


-- =========================================================
-- 7. TOP 10 STATES BY SALES
-- =========================================================
-- Business Question: Which regions contribute most to revenue?

SELECT 
    State,
    ROUND(SUM(Sales), 2) AS total_sales
FROM orders
GROUP BY State
ORDER BY total_sales DESC
LIMIT 10;

-- Insight:
-- High-performing states can be targeted for expansion strategies.


-- =========================================================
-- 8. DISCOUNT IMPACT ON PROFIT (ADVANCED)
-- =========================================================
-- Business Question: How do discounts affect profitability?

SELECT 
    Discount,
    ROUND(AVG(Profit), 2) AS avg_profit,
    ROUND(SUM(Sales), 2) AS total_sales
FROM orders
GROUP BY Discount
ORDER BY Discount;

-- Insight:
-- Higher discounts tend to reduce profit margins.
-- Indicates need for optimized discount strategies.


-- =========================================================
-- 9. SHIPPING PERFORMANCE ANALYSIS (ADVANCED)
-- =========================================================
-- Business Question: How efficient is shipping?

SELECT 
    `Ship Mode`,
    ROUND(AVG(DATEDIFF(`Ship Date`, `Order Date`)), 2) AS avg_shipping_days
FROM orders
GROUP BY `Ship Mode`
ORDER BY avg_shipping_days;

-- Insight:
-- Faster shipping improves customer experience but may increase cost.


-- =========================================================
-- 10. TOP 10 PRODUCTS BY SALES
-- =========================================================
-- Business Question: Which products generate the most revenue?

SELECT 
    `Product Name`,
    ROUND(SUM(Sales), 2) AS total_sales
FROM orders
GROUP BY `Product Name`
ORDER BY total_sales DESC
LIMIT 10;

-- Insight:
-- Top products contribute significantly to revenue and should be prioritized.


-- =========================================================
-- 11. LOSS-MAKING PRODUCTS
-- =========================================================
-- Business Question: Which products should be reviewed?

SELECT 
    `Product Name`,
    ROUND(SUM(Profit), 2) AS total_profit
FROM orders
GROUP BY `Product Name`
HAVING SUM(Profit) < 0
ORDER BY total_profit ASC;

-- Insight:
-- Products with consistent losses should be re-evaluated or discontinued.


-- =========================================================
-- END OF PROJECT
-- =========================================================

