---A telecommunications company wants to invest in new countries. 
---The company intends to invest in the countries where the average call duration of the calls in this country is strictly greater than the global average call duration.

---Write an SQL query to find the countries where this company can invest.

---Return the result table in any order.

# Write your MySQL query statement below
SELECT Country.name AS country FROM
Person JOIN Country JOIN Calls
ON left(phone_number, 3) = Country.country_code
AND Person.id IN (Calls.caller_id, Calls.callee_id)
GROUP BY country
HAVING avg(duration) > (SELECT avg(duration) FROM Calls)
