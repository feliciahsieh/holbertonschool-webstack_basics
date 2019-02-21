-- 21-cities_of_california_subquery.sql - list CA cities in database
SELECT cities.id, cities.name from cities, states
WHERE cities.state_id = states.id
AND states.name="California"
ORDER BY cities.id ASC;
