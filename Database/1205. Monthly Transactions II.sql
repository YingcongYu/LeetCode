---Write an SQL query to find for each month and country: the number of approved transactions and their total amount, the number of chargebacks, and their total amount.

---Note: In your query, given the month and country, ignore rows with all zeros.

---Return the result table in any order.


# Write your MySQL query statement below
WITH combine AS
(SELECT c.trans_id AS id, 
        t.country AS country, 
        'chargeback' AS state, 
        t.amount AS amount, 
        c.trans_date AS trans_date 
 FROM Chargebacks c 
 JOIN Transactions t ON c.trans_id = t.id
 UNION ALL
 SELECT * FROM Transactions
 WHERE state = 'approved')

SELECT left(trans_date, 7) AS month, 
       country, 
       sum(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
       sum(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_amount,
       sum(CASE WHEN state = 'chargeback' THEN 1 ELSE 0 END) AS chargeback_count,
       sum(CASE WHEN state = 'chargeback' THEN amount ELSE 0 END) AS chargeback_amount
FROM combine
GROUP BY month, country
