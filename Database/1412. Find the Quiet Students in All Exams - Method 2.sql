--- A quiet student is the one who took at least one exam and did not score the high or the low score.

---Write an SQL query to report the students (student_id, student_name) being quiet in all exams. Do not return the student who has never taken any exam.

---Return the result table ordered by student_id.


# Write your MySQL query statement below
WITH exams AS
(SELECT *, 
        rank() over (PARTITION BY exam_id ORDER BY score ASC) AS ascending,
        rank() over (PARTITION BY exam_id ORDER BY score DESC) AS descending
 FROM Exam)

SELECT * FROM Student
WHERE student_id NOT IN (SELECT student_id FROM exams 
                         WHERE ascending = 1 OR descending = 1)
  AND student_id IN (SELECT student_id FROM exams)
