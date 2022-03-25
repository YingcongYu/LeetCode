---A telecommunications company wants to invest in new countries. 
---The company intends to invest in the countries where the average call duration of the calls in this country is strictly greater than the global average call duration.

---Write an SQL query to find the countries where this company can invest.

---Return the result table in any order.

# Write your MySQL query statement below
WITH CTE AS (SELECT Country.name, duration FROM Person JOIN Country JOIN 
             (SELECT caller_id AS id, duration FROM Calls UNION SELECT callee_id AS id, duration FROM Calls) a
             ON Person.id = a.id AND left(Person.phone_number, 3) = Country.country_code)

SELECT name AS country FROM CTE GROUP BY name HAVING avg(duration) > (SELECT avg(duration) FROM Calls)
