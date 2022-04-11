---Write an SQL query to find the npv of each query of the Queries table.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT Queries.id, Queries.year, IFNULL(npv, 0) AS npv FROM NPV
RIGHT JOIN Queries
ON Queries.id = NPV.id AND Queries.year = NPV.year
