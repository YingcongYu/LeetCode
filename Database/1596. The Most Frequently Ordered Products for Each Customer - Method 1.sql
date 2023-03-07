--- Write an SQL query to find the most frequently ordered product(s) for each customer.

--- The result table should have the product_id and product_name for each customer_id who ordered at least one order.

--- Return the result table in any order.


# Write your MySQL query statement below
WITH CTE1 AS (
    SELECT
        Customers.customer_id AS customer_id
        ,product_id
        ,COUNT(*) AS counts
    FROM Customers
    JOIN Orders
    ON Customers.customer_id = Orders.customer_id
    GROUP BY customer_id, product_id
),
CTE2 AS (
    SELECT
        *
        ,RANK() OVER (PARTITION BY customer_id ORDER BY counts DESC) AS rk
    FROM CTE1
)

SELECT
    customer_id
    ,CTE2.product_id AS product_id
    ,product_name
FROM CTE2, Products
WHERE CTE2.product_id = Products.product_id
    AND rk = 1
