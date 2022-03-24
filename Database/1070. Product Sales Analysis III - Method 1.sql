---Write an SQL query that selects the product id, year, quantity, and price for the first year of every product sold.

---Return the resulting table in any order.

# Write your MySQL query statement below
SELECT product_id, `year` AS first_year, quantity, price FROM Sales
WHERE (product_id, `year`) IN (SELECT product_id, min(`year`) AS yr FROM Sales GROUP BY product_id)
