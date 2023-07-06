-- The answer rate for a question is the number of times a user answered the question by the number of times a user showed the question.

-- Write an SQL query to report the question that has the highest answer rate. 
--   If multiple questions have the same maximum answer rate, report the question with the smallest question_id.


# Write your MySQL query statement below
SELECT
    question_id AS survey_log
FROM SurveyLog
GROUP BY question_id
ORDER BY COUNT(CASE WHEN action = "answer" THEN 1 END) / COUNT(CASE WHEN action = "show" THEN 1 END) DESC, question_id
LIMIT 1
