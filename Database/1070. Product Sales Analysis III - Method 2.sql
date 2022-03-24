---Write an SQL query that selects the product id, year, quantity, and price for the first year of every product sold.

---Return the resulting table in any order.

# Write your MySQL query statement below
SELECT product_id, `year` AS first_year, quantity, price 
FROM (SELECT *, rank() over (PARTITION BY product_id ORDER BY `year`) AS ranking FROM Sales) a 
WHERE ranking = 1
