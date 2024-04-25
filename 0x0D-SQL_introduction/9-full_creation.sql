-- create table second_table in the database
-- which has id, name and score
-- if the table exist, the script should not fail
-- the script should add few records

CREATE TABLE IF NOT EXISTS `second_table` (`id` INT, `name` VARCHAR(256), `score` INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "BOb", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
