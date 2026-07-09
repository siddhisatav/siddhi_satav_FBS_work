create database septjp25;
create table student (rollno int , name varchar(20),marks int , cnamr varchar(20));

show tables;

desc student;
create table employee (rollno int , name varchar(20) , salary int , address varchar(50) , gender char(10));

create table book (bno int , name varchar(20));

alter table book
add column price int;

alter table book
change column name bookname varchar(200);

show tables;
desc book;





alter table book
modify column price float;



alter table book
ADD primary key(bno);

insert into book (bno , bookname)
values(1,"ABC");


alter table book
modify column price float unique;

insert into book(bno,bookname,price) values
		    (2,"sss",233);
table book;

alter table book
modify column bookname varchar(200) not null;

insert into book(bno,price) values 
                (4,343);
                
alter table book
modify column price float default 55;
                
insert into book(bno,bookname) values 
                (5,"aaa");
alter table book 
modify column bookname varchar(200) check( bookname != "aa");
insert into book(bno , bookname,price)values
 (12,"aaa",234);
 
 show create table book;
 
 alter table book 
modify column bookname varchar(200) check(price in(233,234,343,233,55));

insert into book(bno , bookname,price)values
 (12,"aaa",234);



create table Product (pid int,price float ,status varchar(20) , quality varchar(200),mdate date);
alter table Product
add primary key (Pid);

table product;

alter table product
change column status statuss varchar(20);
insert into Product(pid,price,statuss,quality,mdate)values
(1,111,"pending","good","24-3-3");
SET SQL_SAFE_UPDATES = 0;




ALTER TABLE product 
MODIFY COLUMN price float CHECK(price > 100);

insert into Product(pid,price,statuss,quality,mdate)values
(4,110,"A","good","24-4-3");


alter table product
modify column  statuss varchar(20) check( statuss = 'A' or statuss = 'NA');

update product
set pid = 3
Where pid is  null and statuss = 'A';

ALTER TABLE product 
MODIFY COLUMN quality varchar(200) not null;



