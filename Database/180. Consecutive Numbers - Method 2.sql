---Write an SQL query to find all numbers that appear at least three times consecutively.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums FROM `Logs`
WHERE (id+1, num) IN (SELECT * FROM `Logs`) 
    AND (id+2, num) IN (SELECT * FROM `Logs`) 
