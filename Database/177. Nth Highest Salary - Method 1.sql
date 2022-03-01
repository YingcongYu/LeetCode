---Write an SQL query to report the nth highest salary from the Employee table. If there is no nth highest salary, the query should report null.

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT salary FROM
      (SELECT salary, dense_rank() over (ORDER BY salary DESC) AS ranking FROM Employee) a
      WHERE ranking = N
  );
END
