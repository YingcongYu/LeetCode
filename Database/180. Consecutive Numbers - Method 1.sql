---Write an SQL query to find all numbers that appear at least three times consecutively.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT a.num AS ConsecutiveNums FROM `Logs` a, `Logs` b, `Logs` c
WHERE (a.id, a.num) = (b.id-1, b.num) AND (b.id-1, b.num) = (c.id-2, c.num)
GROUP BY a.num, b.num, c.num
