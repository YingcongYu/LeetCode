---A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:

---Hiring the largest number of seniors.
---After hiring the maximum number of seniors, use the remaining budget to hire the largest number of juniors.

---Write an SQL query to find the number of seniors and juniors hired under the mentioned criteria.

---Return the result table in any order.

# Write your MySQL query statement below
WITH budget AS (SELECT *, sum(salary) over (PARTITION BY experience ORDER BY salary) AS total FROM Candidates)

SELECT IFNULL(experience, 'Senior') AS experience, count(*) AS accepted_candidates FROM budget 
    WHERE experience = 'Senior' AND total <= 70000
UNION
SELECT IFNULL(experience, 'Junior') AS experience, count(*) AS accepted_candidates FROM budget
    WHERE experience = 'Junior' 
    AND total <= (SELECT 70000 - IFNULL(max(total), 0) 
                  FROM budget WHERE experience = 'Senior' AND total <= 70000)
