Create Table Company(
  id int,
  name varchar(50),
  salary int,
  place text
);

Insert Into Company(id,name,salary,place) values
(1,"Employee 1",100000,"India"),
(2,"Employee 2",2500000,"America"),
(3,"Employee 3",450000,"London"),
(4,"Employee 4", 6500000,"India"),
(5,"Employee 5",270000,"Africa"),
(6,"Employee 6", 55500,"Austrailia"),
(7,"Employee 7",780000,"India"),
(4,"Employee 4", 6500000,"India"),
(6,"Employee 6", 55500,"Austrailia"),
(2,"Employee 8",2500000,"America");

select * from Company;
select distinct* from Company;
select sum(salary) as total from Company;
select avg(salary) as total from Company;
select count(salary) as total from Company;
select max(salary) as moresalary from Company;
select min(salary) as lesssalary from Company;
