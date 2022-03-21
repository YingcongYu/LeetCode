---A school has students from Asia, Europe, and America.

---Write an SQL query to pivot the continent column in the Student table so that each name is sorted alphabetically and displayed underneath its corresponding continent. 
---The output headers should be America, Asia, and Europe, respectively.

---The test cases are generated so that the student number from America is not less than either Asia or Europe.

# Write your MySQL query statement below
SELECT 
    max(CASE WHEN continent = 'America' THEN name END) AS America,
    max(CASE WHEN continent = 'Asia' THEN name END) AS Asia,
    max(CASE WHEN continent = 'Europe' THEN name END) AS Europe
FROM (SELECT *, row_number() OVER (PARTITION BY continent ORDER BY name) AS row_id FROM Student) a
GROUP BY row_id
