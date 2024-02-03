/*
write SQL script that creates a table users with
 the requirements:
 - id - integer, never null, auto increment and primary key
 - emaail - string(255 chars), never null and unique
 - name - string(255 chars)
if table already exist, table should not fail
script should execute on any database
make attribute unique directly in the table
*/

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
    );