-- 103-avg_temperatures.sql - list avg temperature by city ordered by temp descending
SELECT city, AVG(value) AS 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
