-- 109-rating_genres.sql - list genres ordered by sum of ratings
SELECT tv_genres.name, SUM(rate) AS 'rating'
FROM tv_genres, tv_show_ratings, tv_show_genres
WHERE tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY SUM(rate) DESC;
