---A quiet student is the one who took at least one exam and did not score the high or the low score.

---Write an SQL query to report the students (student_id, student_name) being quiet in all exams. Do not return the student who has never taken any exam.

---Return the result table ordered by student_id.


# Write your MySQL query statement below
WITH exams AS
(SELECT *, 
        CASE WHEN score = max(score) over (PARTITION BY exam_id) 
               OR score = min(score) over (PARTITION BY exam_id) 
             THEN 1 ELSE 0 END AS performance 
 FROM Exam)

SELECT * FROM Student
WHERE student_id IN (SELECT student_id FROM exams 
                     GROUP BY student_id 
                     HAVING sum(performance) = 0)
