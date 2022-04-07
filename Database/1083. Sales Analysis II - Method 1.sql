---Write an SQL query that reports the buyers who have bought S8 but not iPhone. Note that S8 and iPhone are products present in the Product table.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT buyer_id FROM
(SELECT DISTINCT buyer_id FROM Sales 
 WHERE product_id IN 
 (SELECT product_id FROM Product WHERE product_name = 'S8')) a
WHERE buyer_id NOT IN
(SELECT DISTINCT buyer_id FROM Sales 
 WHERE product_id IN 
 (SELECT product_id FROM Product WHERE product_name = 'iPhone'))
