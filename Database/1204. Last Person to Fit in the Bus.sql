---There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms, so there may be some people who cannot board.

---Write an SQL query to find the person_name of the last person that can fit on the bus without exceeding the weight limit. 
---The test cases are generated such that the first person does not exceed the weight limit.


# Write your MySQL query statement below
SELECT person_name FROM
(SELECT *, sum(weight) over (ORDER BY turn) AS total_weight FROM Queue) a
WHERE total_weight <= 1000 ORDER BY turn DESC LIMIT 1
