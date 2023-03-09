--- Write an SQL query to find the most recent three orders of each user. If a user ordered less than three orders, return all of their orders.

--- Return the result table ordered by customer_name in ascending order and in case of a tie by the customer_id in ascending order. 
--- If there is still a tie, order them by order_date in descending order.


# Write your MySQL query statement below
WITH CTE AS (
    SELECT
        *
        ,ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rk
    FROM Orders
)

SELECT
    name AS customer_name
    ,CTE.customer_id AS customer_id
    ,order_id
    ,order_date
FROM CTE, Customers
WHERE rk <= 3
    AND CTE.customer_id = Customers.customer_id
ORDER BY customer_name, CTE.customer_id, order_date DESC
