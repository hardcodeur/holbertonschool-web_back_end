-- SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.

USE hbtn_0d_tvshows

-- DROP INDEX idx_name_first_score ON names;

CREATE INDEX idx_name_first_score ON names(name,score);