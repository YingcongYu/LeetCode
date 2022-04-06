---You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

---Write an SQL query to compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). 
---average_amount should be rounded to two decimal places.

---Return result table ordered by visited_on in ascending order.

# Write your MySQL query statement below
SELECT DISTINCT visited_on, amount, round(amount/7, 2) AS average_amount FROM
(SELECT 
 visited_on, 
 sum(amount) over (ORDER BY visited_on RANGE BETWEEN INTERVAL '6' DAY PRECEDING AND CURRENT ROW) AS amount
 FROM Customer) a
WHERE visited_on IN (SELECT date_sub(visited_on, INTERVAL -6 DAY) FROM Customer)
