create database haksa;
use haksa;  /*db open*/

create table dept(
	dcode int primary key auto_increment,
		dname varchar(100) not null /*varchar: 들어있는 것 만큼만 자리 차지*/
);

drop database haksa; /*db drop*/

drop table dept; /*나를 참조하고 있는 테이블이 있다면 지울 수 없음!*/

insert into dept(dname) values('컴퓨터정보공학과');
insert into dept(dname) values('전자공학과');
insert into dept(dname) values('건축공학과');

select * from dept;

create table student(
   id char(4) primary key,
    name varchar(50) not null,
   code int not null,
    foreign key(code) references dept(dcode)
);

insert into student(id, name, code) values('2501','홍길동', 1);
insert into student(id, name, code) values('2502','홍길동', 3);
insert into student(id, name, code) values('2503','심청이', 2);
insert into student(id, name, code) values('2504','강감찬', 2);

select * from student;

create view vstudent as
select student.*, dept.dname
from student, dept
where code = dcode;

select  * from vstudent;
commit;