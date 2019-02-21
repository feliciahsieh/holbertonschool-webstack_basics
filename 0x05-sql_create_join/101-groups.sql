-- 101-groups.sql - list number of records in table second_table
SELECT score, COUNT(score) AS 'number'
FROM second_table
GROUP BY score
ORDER BY COUNT(score) DESC;
