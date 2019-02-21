-- 22-cities_by_state_join.sql - list all database cities in specific format
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
/*INNER JOIN cities ON vehicles.car_owner = users.user_id*/
