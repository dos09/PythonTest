SET NAMES 'utf8' COLLATE 'utf8_general_ci';

CREATE TABLE IF NOT EXISTS `orcs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clan` varchar(100) DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `kills` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;

load data local infile 'orcs.csv' replace into table orcs character set utf8 columns terminated by ',' lines terminated by '\n' ignore 1 rows (
clan,name,kills);

/*
- columns in the file are terminated by ','
- lines are terminated by '\n' (Linux) and '\r\n' (Windows)
- ignore 1 rows (clan,name,kills):
    ingore the first, row and specify which fields you want to match with the table.
    This is done because the table has id column and the csv file has no id field.
*/