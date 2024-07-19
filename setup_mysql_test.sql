-- setup mysql server for testing project
-- more comments
-- create db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- use db
USE hbnb_test_db;
-- create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant user privileges
GRANT ALL on hbnb_test_db.* TO 'hbnb_test'@'localhost' WITH GRANT OPTION;
-- grant user privilege on another db
GRANT USAGE on *.* TO 'hbnb_test'@'localhost'; 
-- USE performance_schema;
GRANT SELECT on performance_schema.* TO 'hbnb_test'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
