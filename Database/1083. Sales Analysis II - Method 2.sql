---Write an SQL query that reports the buyers who have bought S8 but not iPhone. Note that S8 and iPhone are products present in the Product table.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT buyer_id FROM Product
JOIN Sales ON Product.product_id = Sales.product_id
GROUP BY buyer_id 
HAVING sum(product_name = 'S8') > 0 AND sum(product_name = 'iPhone') = 0
