---Write an SQL query to report the nth highest salary from the Employee table. If there is no nth highest salary, the query should report null.

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    set N = N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT IFNULL((SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET N), null)
  );
END
