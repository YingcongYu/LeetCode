---Write an SQL query that reports all the projects that have the most employees.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT project_id FROM
(SELECT project_id, rank() over (ORDER BY total DESC) AS ranking 
FROM (SELECT project_id, count(*) AS total FROM Project GROUP BY project_id) a) b
WHERE ranking = 1
