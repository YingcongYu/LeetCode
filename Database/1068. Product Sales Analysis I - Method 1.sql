---Write an SQL query that reports the product_name, year, and price for each sale_id in the Sales table.

---Return the resulting table in any order.


# Write your MySQL query statement below
SELECT product_name, year, price 
FROM Sales JOIN Product
ON Sales.product_id = Product.product_id
