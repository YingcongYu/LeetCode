---Write an SQL query to evaluate the boolean expressions in Expressions table.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT left_operand, operator, right_operand,
    CASE WHEN operator = '<' AND L.value < R.value THEN 'true'
         WHEN operator = '>' AND L.value > R.value THEN 'true'
         WHEN operator = '=' AND L.value = R.value THEN 'true'
         ELSE 'false' END AS value
FROM Expressions
JOIN Variables AS L
JOIN Variables AS R
ON L.name = Expressions.left_operand AND R.name = Expressions.right_operand
