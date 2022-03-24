---Write a SQL query to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest course_id.

---Return the result table ordered by student_id in ascending order.

# Write your MySQL query statement below
SELECT student_id, course_id, grade FROM 
(SELECT *, rank() over (PARTITION BY student_id ORDER BY grade DESC, course_id) AS best FROM Enrollments) a
WHERE best = 1
