create database social_media_db;

use social_media_db;

create table post(
id int auto_increment primary key,
title varchar(200) not null,
user varchar(200) not null,
description varchar(200)not null
);

create table comments(
id int auto_increment primary key,
message varchar(200) not null,
post_id int  not null
);