-- SQL script that creates a table users

USE hbtn_0d_tvshows

DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users(
    id INT UNSIGNED  NOT NULL  AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US','CO','TN') NOT NULL DEFAULT 'US'
);
