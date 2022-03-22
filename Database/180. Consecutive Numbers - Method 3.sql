---Write an SQL query to find all numbers that appear at least three times consecutively.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT DISTINCT num as ConsecutiveNums FROM
(SELECT num, id - cast(row_number() over (ORDER BY num, id) AS SIGNED) AS row_id FROM `Logs`) a
GROUP BY num, row_id HAVING count(*) >= 3
