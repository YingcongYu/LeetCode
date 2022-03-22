---Write an SQL query to report the managers with at least five direct reports.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT name FROM Employee
WHERE id IN (SELECT managerId FROM Employee GROUP BY managerId HAVING count(*) >= 5)
