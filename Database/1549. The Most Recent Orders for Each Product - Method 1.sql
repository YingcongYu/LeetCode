--- Write an SQL query to find the most recent order(s) of each product.

--- Return the result table ordered by product_name in ascending order and in case of a tie by the product_id in ascending order. 
--- If there still a tie, order them by order_id in ascending order.


# Write your MySQL query statement below
WITH CTE AS (
    SELECT
        product_name
        ,Orders.product_id AS product_id
        ,order_id
        ,order_date
        ,RANK() OVER (PARTITION BY product_name ORDER BY order_date DESC) AS rk
    FROM Products
    JOIN Orders
    ON Orders.product_id = Products.product_id
)

SELECT
    product_name
    ,product_id
    ,order_id
    ,order_date
FROM CTE
WHERE rk = 1
ORDER BY product_name, product_id, order_id
