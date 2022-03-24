---Write a SQL query to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest course_id.

---Return the result table ordered by student_id in ascending order.

# Write your MySQL query statement below
SELECT student_id, min(course_id) AS course_id, grade FROM Enrollments 
WHERE (student_id, grade) IN (SELECT student_id, max(grade) FROM Enrollments GROUP BY student_id) 
GROUP BY student_id ORDER BY student_id
