-- 104-top_city.sql - list top 3 cities' temperates during July / Aug
SELECT city, AVG(value)
FROM temperatures
WHERE month=7 OR month=8
GROUP BY city
ORDER BY AVG(value) DESC LIMIT 3;
