---Write an SQL query to find all numbers that appear at least three times consecutively.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT DISTINCT num AS consecutiveNums FROM
    (SELECT num, sum(consecutive) over (ORDER BY id) AS sum FROM
        (SELECT id, num, (CASE WHEN lag(num) over (ORDER BY id) - num = 0 THEN 0 ELSE 1 END) 
         AS consecutive FROM `Logs`) a
    ) b
GROUP BY num, sum HAVING count(*) >= 3
