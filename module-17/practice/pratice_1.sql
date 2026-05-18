create table departments (
	id serial primary key,
	name text not null unique
);

create table employees (
	id serial primary key,
	name text not null,
	salary numeric(10, 2) check (salary > 0),
	department_id int references departments(id),
	hired_at date default current_date
);

create table projects (
	id serial primary key,
	name text not null,
	employee_id int references employees(id),
	budget numeric(12, 2) check (budget >= 0),
	is_active boolean default true
);

-- -------------------------

insert into departments (name)
values
	('IT'),
	('HR'),
	('Finance'),
	('Marketing');

insert into employees (name, salary, department_id, hired_at)
values
	('Анна Ивановна', 150000, 1, '2023-01-15'),
	('Иван Петров', 90000, 1, '2023-03-10'),
	('Мария Смирнова', 110000, 2, '2022-11-20'),
	('Олег Кузнецов', 130000, 3, '2021-06-05'),
	('Алексей Орлов', 70000, null, '2024-02-01'),
	('Елена Соколова', 160000, 1, '2020-09-12');

insert into projects (name, employee_id, budget, is_active)
values
	('CRM System', 1, 500000, true),
	('Website Redesign', 2, 200000, true),
	('Hiring Platform', 3, 300000, true),
	('Accounting Automation', 4, 350000, false),
	('Internal Chat', 1, 150000, true);