---Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.

---Return the result table in any order.

# Write your MySQL query statement below
DELETE p2 FROM Person AS p1, Person AS p2
WHERE p1.email = p2.email AND p1.id < p2.id
