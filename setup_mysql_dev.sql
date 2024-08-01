-- setup mysql server for project
-- more comments

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
-- GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost'

-- -- cat user.sql | mysql -hlocalhost -uroot -p
-- CREATE DATABASE IF NOT EXISTS tyrell_corp;
-- USE tyrell_corp;
-- CREATE TABLE IF NOT EXISTS nexus6(id INT, name VARCHAR(256));
-- INSERT INTO nexus6 (id, name) VALUES (1, 'Leon')
-- GRANT SELECT ON `nexus6`.* TO 'holberton_user'@'localhost'

-- cat replica.sql | sudo mysql -hlocalhost -uroot -p