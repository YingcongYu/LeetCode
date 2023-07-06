-- Write an SQL query to report the name of the winning candidate (i.e., the candidate who got the largest number of votes).

-- The test cases are generated so that exactly one candidate wins the elections.


# Write your MySQL query statement below
SELECT
    name
FROM Candidate
JOIN Vote
ON Candidate.id = Vote.candidateId
GROUP BY candidateId
ORDER BY COUNT(*) DESC
LIMIT 1
