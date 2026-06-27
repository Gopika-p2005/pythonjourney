
create database course_db1;

use course_db1;

-- course [id,name,durasion,fee]

-- batch [id,title,seat_count,course_id,time] 

create table course (
		id int auto_increment primary key,
        name varchar(200) unique not null,
        durasion varchar(10) not null,
        fee decimal(10,2) not null
);


insert into course (name,durasion,fee) values ("mearn stack","6.5 month",75000),
												("ASP.net","6 month",55000),
                                                ("java full stack","6.5 month",55000),
                                                ("PYTHON DJANGO","6.5 month",74000),
                                                ("DATA SCIENCE","7.5 month",85000),
                                                ("data analysis","6 month",45000),
                                                ("soft ware testing","6month",55000);
												
select * from course;

create table batch(
	id int auto_increment primary key,
    title varchar(200) unique not null,
    time enum("8:30am-10:30am","10:30am-12:30pm","1pm-3pm","3pm-5pm") default "10:30am-12:30pm",
    seat_count int not null,
    course_id int not null,
    foreign key (course_id) references course(id)
);

insert into batch (title,time,seat_count,course_id) value("MSjune","8:30am-10:30am",30,1);
insert into batch (title,time,seat_count,course_id) value("MSapr","10:30am-12:30pm",25,1);
insert into batch (title,time,seat_count,course_id) value("ASPjune","8:30am-10:30am",30,2);
insert into batch (title,time,seat_count,course_id) value("ASpjune","10:30am-12:30pm",25,2);

select * from batch;

select course.name,course.fee,batch.title,batch.seat_count from course inner join batch on course.id=batch.course_id;

select course.name,course.fee,batch.title,batch.seat_count from course left join batch on course.id=batch.course_id;

select course.name,course.fee,batch.title,batch.seat_count from course right join batch on course.id=batch.course_id;


-- query for add new colum
-- alter table table_name add column_name data_type;
-- alter table batch add time enum(); 

-- update

update batch set time="3pm-5pm" where id= 4;

select * from batch;

-- delete

delete from batch where id =4;

-- create
-- read(select)
-- update
-- delete

-- join(inner,left,right)