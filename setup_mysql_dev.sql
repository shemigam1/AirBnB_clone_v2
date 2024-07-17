-- setup mysql server for project
-- more comments
-- create db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- use db
USE hbnb_dev_db;
-- create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant user privileges
GRANT ALL on hbnb_dev_db TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
-- grant privilege on another db
GRANT USAGE on *.* TO 'hbnb_dev'@'localhost'; 
-- USE performance_schema;
GRANT SELECT on performance_schema.* TO 'hbnb_dev'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
