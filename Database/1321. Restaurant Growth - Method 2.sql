---You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

---Write an SQL query to compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). 
---average_amount should be rounded to two decimal places.

---Return result table ordered by visited_on in ascending order.

# Write your MySQL query statement below
SELECT a.visited_on, sum(amount) AS amount, round(sum(amount)/7, 2) AS average_amount 
FROM Customer JOIN 
(SELECT DISTINCT visited_on FROM Customer) a
ON datediff(a.visited_on, Customer.visited_on) BETWEEN 0 AND 6
GROUP BY a.visited_on HAVING count(DISTINCT(Customer.visited_on)) = 7
