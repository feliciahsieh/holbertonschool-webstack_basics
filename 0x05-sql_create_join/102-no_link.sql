-- 102-no_link.sql - list rows with a 'name' value from second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
