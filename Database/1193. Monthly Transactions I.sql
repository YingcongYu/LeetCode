---Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT 
    date_format(trans_date, '%Y-%m') AS month, 
    country, 
    count(*) AS trans_count, 
    count(CASE WHEN state = 'approved' THEN TRUE END) AS approved_count, 
    sum(amount) AS trans_total_amount, 
    sum(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount 
FROM Transactions 
GROUP BY country, month
