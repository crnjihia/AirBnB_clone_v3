-- Script to set up MySQL server for testing
-- Creates database hbnb_test_db and user hbnb_test

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create new user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES
ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';

-- Grant select privilege on performance_schema to hbnb_test
GRANT SELECT
ON performance_schema.*
TO 'hbnb_test'@'localhost';

-- Apply the new privileges
FLUSH PRIVILEGES;
