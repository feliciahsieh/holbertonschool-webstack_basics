-- 26-count_shows_by_genre.sql
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number of shows'
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY COUNT(tv_show_genres.genre_id) DESC;
