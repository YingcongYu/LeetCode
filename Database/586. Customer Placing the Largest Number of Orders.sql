---Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.

---The test cases are generated so that exactly one customer will have placed more orders than any other customer.

# Write your MySQL query statement below
SELECT customer_number FROM Orders 
GROUP BY customer_number HAVING count(*) ORDER BY count(*) DESC LIMIT 1
