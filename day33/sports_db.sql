create database sports_db;

use sports_db ;

create table player (

id int auto_increment PRIMARY KEY,
sport enum("football","cricket","badminton") not null,
age int not null,
country varchar(200) not null,
player_num int not null,
world_cup_apperence int not null,
name varchar(200) not null,
gender enum("male","female","other") not null

);

desc player ;