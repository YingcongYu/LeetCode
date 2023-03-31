--- A school has students from Asia, Europe, and America.

--- Write an SQL query to pivot the continent column in the Student table 
--- so that each name is sorted alphabetically and displayed underneath its corresponding continent. 
--- The output headers should be America, Asia, and Europe, respectively.

--- The test cases are generated so that the student number from America is not less than either Asia or Europe.


/* Write your T-SQL query statement below */
SELECT
    [America] AS 'America'
    ,[Asia] AS 'Asia'
    ,[Europe] AS 'Europe'
FROM (SELECT
        *
        ,ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) AS rk
        FROM Student) AS SourceTable
PIVOT (MAX(name) FOR continent IN ([America], [Asia], [Europe])) AS PivotTable
