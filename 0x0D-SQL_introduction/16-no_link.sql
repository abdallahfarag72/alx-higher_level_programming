-- Describes a sql query
-- lists all records of the table second_table that has a name
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
