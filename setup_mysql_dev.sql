-- setup mysql server for project
-- more comments
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL on hbnb_dev_db TO 'hbnb_dev'@'localhost';
USE performance_schema;
GRANT SELECT on performance_schema TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
