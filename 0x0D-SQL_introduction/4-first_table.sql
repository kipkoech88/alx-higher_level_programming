-- create table first_table in current db
-- if the table already exists it should not fail

CREATE TABLE IF NOT EXISTS `first_table` (`id` INT,`name` VARCHAR(256));
