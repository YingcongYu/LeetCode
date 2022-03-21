---Write an SQL query to report the respective department name and number of students majoring in each department for all departments in the Department table (even ones with no current students).

---Return the result table ordered by student_number in descending order. In case of a tie, order them by dept_name alphabetically.

# Write your MySQL query statement below
SELECT Department.dept_name, IF(a.num IS Null, 0, a.num) AS student_number FROM Department
LEFT JOIN
(SELECT dept_id, count(*) AS num FROM Student GROUP BY dept_id) a
ON a.dept_id = Department.dept_id ORDER BY student_number DESC
