CREATE TABLE JOBS (
    id        INTEGER      PRIMARY KEY AUTOINCREMENT,
    title     VARCHAR (50) NOT NULL,
    minsalary INTEGER
);

insert into jobs(title,minsalary) values('Python Programmer',300000)
insert into jobs(title,minsalary) values('Data Scientist',800000)