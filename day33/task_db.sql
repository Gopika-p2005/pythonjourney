-- create task_db
create database task_db ;
use task_db;

-- user [id,name,phone]
create table user(
id int auto_increment PRIMARY KEY,
name varchar(200) not null,
phone int not null
);

alter table user modify phone varchar(15);

insert into user (name,phone) value("hari","4874384"),("aravind","846893"),("aswin",'68933'),('manu','753168');

select* from user;

-- task[id,title,status[pending

create table task (
id int primary key auto_increment,
title varchar(100) not null,
status enum("pending","complete") default "pending",
owner int not null
);

insert into task (title,status,owner)value("admission_fee","pending",2),
										  ("grocer","pending",8),
                                          ("credit card bill","pending",3),
							              ("car wash","pending",1),
                                          ("boke challan","pending",11);
                                          
select * from task;
-- inner join
select user.name,task.title,task.status from user inner join task on user.id= task.owner;

-- left join
select user.name,task.title,task.status from user left join task on user.id= task.owner;

-- right join
select user.name,task.title,task.status from user right join task on user.id= task.owner;

