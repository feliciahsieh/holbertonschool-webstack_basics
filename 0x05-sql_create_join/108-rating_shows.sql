-- 108-rating_shows.sql - list shows by their rating
SELECT tv_shows.title, SUM(rate) AS 'rating'
FROM tv_show_ratings
JOIN tv_shows
ON tv_shows.id=tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY SUM(rate) DESC;
