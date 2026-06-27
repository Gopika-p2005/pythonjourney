-- list all databases

show databases ;

-- create database sellit_db

create database sellit_db ;

-- switch to sellit_db

use sellit_db ;


-- create table vehicle
 create table vehicle(

    id int auto_increment PRIMARY KEY,
    name varchar(200) not null,
    price decimal(10,2) not null,
    model varchar(20) not null,
    fuel_type enum("petrol","diesel","ev","cng") default "petrol",
    runnin_km int default 100,
    location varchar(200) not null,
    contact varchar(12) not null,
    owner_type enum("single","second","third","other") default"single"
 );
 
 desc vehicle ;
 
 -- insert record
 
 insert into vehicle(name,price,model,fuel_type,runnin_km,location,contact,owner_type)values("royal",3000,2000,"diesel",200000,"kochi",563637567,"single"),
                                                                                            ("activa",2300,2000,"cng",200000,"palakkad",563637567,"third"),
																							("honda",1000,2000,"ev",1000,"tvm",563637567,"second"),
                                                                                            ( "acer",2500,2000,"diesel",20045,"kottayam",563637567,"single"),
                                                                                             ("tata",3000,2000,"petrol",265000,"calicut",563637567,"other");
																					
select * from vehicle ;