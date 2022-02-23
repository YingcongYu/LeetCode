---Write an SQL query to report all the duplicate emails.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT email AS Email FROM
(SELECT email, count(*) AS nums FROM Person GROUP BY email) a
WHERE nums > 1
