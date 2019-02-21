-- 105-max_state.sql - list max temperature of each state
SELECT state, MAX(value) AS 'max_temp'
FROM temperatures
GROUP BY state
ORDER BY MAX(value) DESC, state ASC;
