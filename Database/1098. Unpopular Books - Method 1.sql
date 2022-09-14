---Write an SQL query that reports the books that have sold less than 10 copies in the last year, 
---excluding books that have been available for less than one month from today. Assume today is 2019-06-23.

---Return the result table in any order.


# Write your MySQL query statement below
SELECT Books.book_id, name
FROM Books LEFT JOIN Orders
ON Books.book_id = Orders.book_id
WHERE available_from < DATE_SUB('2019-06-23', INTERVAL 1 MONTH)
GROUP BY Books.book_id
HAVING sum(CASE WHEN dispatch_date > DATE_SUB('2019-06-23', INTERVAL 1 YEAR) THEN quantity ELSE 0 END) < 10
