---Write an SQL query to report all the duplicate emails.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT email AS Email FROM Person GROUP BY email HAVING count(*) > 1
