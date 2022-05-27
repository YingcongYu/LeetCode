---Write an SQL query to find the most recent three orders of each user. If a user ordered less than three orders, return all of their orders.

---Return the result table ordered by customer_name in ascending order and in case of a tie by the customer_id in ascending order. 
---If there is still a tie, order them by order_date in descending order.


# Write your MySQL query statement below
SELECT Customers.name AS customer_name, 
       a.customer_id AS customer_id, 
       a.order_id AS order_id, 
       a.order_date AS order_date 
FROM
(SELECT *, count(*) over (PARTITION BY customer_id ORDER BY order_date DESC) AS latest FROM Orders) a
JOIN Customers
ON a.customer_id = Customers.customer_id
WHERE latest <= 3 
ORDER BY customer_name ASC, customer_id ASC, order_date DESC
