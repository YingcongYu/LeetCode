---Write an SQL query to:

---Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
---Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.


# Write your MySQL query statement below
WITH output_user AS
(SELECT Users.user_id, name, count(*) AS rated_movies FROM Users JOIN MovieRating
ON Users.user_id = MovieRating.user_id
GROUP BY name ORDER BY rated_movies DESC, name ASC LIMIT 1),

output_movies AS
(SELECT Movies.movie_id, title, avg(rating) AS avg_rating FROM Movies JOIN MovieRating
ON Movies.movie_id = MovieRating.movie_id
WHERE left(created_at, 7) = '2020-02'
GROUP BY title ORDER BY avg_rating DESC, title ASC LIMIT 1)

SELECT name AS results FROM output_user
UNION
SELECT title AS results FROM ouTput_movies
