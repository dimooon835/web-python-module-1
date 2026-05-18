<DOSTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>HTML и CSS </title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header>
    <h1>ТЕСТ HTML и CSS</h1>
    <p>ТЕКСТ ТЕКСТ ТЕКСТ</P>
  </header>

  <main>
    <section class="box">


## 1. База данных

### `CREATE`
Создаёт объект: Таблица, база, индекс
```
CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NUlL,
  salary NUMERIC
)
```

### `TABLE`
Указывает, что создаётся или изменяется таблица
```
CREATE TABLE department (
  id SERIAL PRIMARY KEY,
  name TEXT
)
```

### `ALTER`
Изменяет существующий объект
```
ALTER TABLE employees
ADD COLUMN email TEXT;
```

### `ADD`
Добавляет колонку, ограничение
```
ALTER TABLE employees
ADD COLUMN phone TEXT;
```

### `DROP`
Удаляет объект(таблицу)
```
DROP TABLE projects;
```

### `IF EXISTS`
Позволяет избежать ошибки, если объекта нет
```
DROP TABLE IF EXISTS old_projects;
```

### `IF NOT EXISTS`
Создаёт объект только если его не существует
```
CREATE TABLE IF NOT EXISTS department (
  id SERIAL PRIMARY KEY,
  name TEXT
);
```

### `RENAME`
Переименовывает объект
```
ALTER TABLE employees
RENAME COLUMN name to full_name;
```

### `TRUNCATE`
Быстро очищает таблицу
```
TRUNCATE TABLE projects;
```

## 2. Работа с данными

### `SELECT`
Указывает источник данных
```
SELECT name, salary FROM employees;
```

### `INSERT`
Добавляет строки
```
INSERT INTO departments(name)
VALUES ('it'), ('HR'), ('finance');
```

### `INTO`
Указывает, куда вставлять данные
```
INSERT INTO employees(name, salary, department_id)
VALUES ('Анна', 12000, 1);
```

### `VALUES`
Передаёт конкретные значения
```
INSERT INTO projects(name, employee_id, budget)
VALUES ('CRM System', 1, 500000);
```

### `UPDATE`
Обновляет строки
```sql
UPDATE employees
SET salary = salary * 1.10
WHERE department_id = 1;
```

### `SET`
Задаёт новые значения при `UPDATE`
```sql
UPDATE projects
SET is_active = FALSE
WHERE budget = 100000;
```

### `DELETE`
Удаляет строки
```sql
DELETE FROM employees
WHERE salary < 50000;
```

## 3. Фильтрация данных

### `WHERE`
Фильтрует строки
```sql
SELECT *
FROM employees
WHERE salary = 100000;
```

### `AND`
Оба условия должны быть истинными
```sql
SELECT *
FROM employees
WHERE salary > 100000
    AND department_id = 1;
```

### `OR`
Хотя бы одно условие должно быть истинным
```sql
SELECT *
FROM employees
WHERE salary > 100000
    OR department_id = 1;
```

### `NOT`
Отрицание условия
```sql
SELECT *
FROM projects
WHERE NOT is_active;
```

### `IN`
Проверяет, входит ли значение в список
```sql
SELECT *
FROM employees
WHERE department_id IN (1, 2);
```

### `NOT IN`
Проверяет, что значения нет в списке
```sql
SELECT *
FROM employees
WHERE department_id NOT IN (1, 2);
```

### `BETWEEN`
Проверяет диапазон
```sql
SELECT *
FROM employees
WHERE salary BETWEEN 80000 AND 150000;
```

### `LIKE`
Поиск по шаблону
```sql
SELECT *
FROM employees
WHERE name LIKE "A%";
```

### `ILIKE`
Поиск по шаблону
```sql
SELECT *
FROM employees
WHERE name ILIKE "a%";
```

### `IS NULL`
Проверяет значение на `NULL`
```sql
SELECT *
FROM employees
WHERE department_id IS NULL;
```

### `IS NOT NULL`
Проверяет, что значение не `NULL`
```sql
SELECT *
FROM employees
WHERE department_id IS NOT NULL;
```

### `EXISTS`
Проверяет существование
```sql
SELECT *
FROM departments AS d
WHERE EXISTS (
    SELECT 1
    FROM employees AS e
    WHERE e.departments_id = d.id
)
```

## 4. Сортировка и ограничение результата

### `ORDER BY`
Сортирует результат
```sql
SELECT *
FROM employees
ORDER BY salary;
```

### `ASC`
Сортировка по возрастанию
```sql
SELECT *
FROM employees
ORDER BY salary ASC;
```

### `DESC`
Сортировка по убыванию
```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

### `LIMIT`
Ограничивает количество строк
```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 5;
```

### `OFFSET`
Пропускает указанное количество строк
```sql
SELECT *
FROM employees
ORDER BY id
LIMIT 10 OFFSET 20;
```

## 5. Группировка и агрегаты

### `GROUP BY`
Группирует строки
```sql
SELECT department_id, COUNT(*) as employee_count
FROM employees
GROUP BY department_id;
```

### `HAVING`
Фильтрует группы после `GROUP BY`
```sql
SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 100000;
```

### `COUNT`
Считает строки
```sql
SELECT COUNT(*)
FROM employees;
```

### `SUM`
Суммирует значения
```sql
SELECT SUM(budget)
FROM projects;
```

### `AVG`
Считает среднее значение
```sql
SELECT AVG(salary)
FROM employees;
```

### `MIN`
Минимальное значение
```sql
SELECT MIN(salary)
FROM employees;
```

### `MAX`
Максимальное значение
```sql
SELECT MAX(salary)
FROM employees;
```

### `DISTINCT`
Убирает дубликаты
```sql
SELECT DISTINCT department_id
FROM employees;
```

## 6. Соединение таблиц

### `JOIN`
Соединяет таблицы
```sql
SELECT e.name, d.name AS department
FROM employees AS e
JOIN department d ON e.department_id = d.id;
```

### `INNER JOIN`
То же, что и обычный JOIN: показывает только совпавшие строки
```sql
SELECT e.name, p.name AS project
FROM employees AS e
INNER JOIN projects p ON p.employee_id = e.id;
```

### `LEFT JOIN`
Показывает все строки из левой таблицы, даже если справа нет совпадений
```sql
SELECT e.name, p.name AS project
FROM employees AS e
LEFT JOIN projects p ON p.employee_id = e.id;
```

### `RIGHT JOIN`
Показывает все строки из правой таблицы, даже если слева нет совпадений
```sql
SELECT e.name, p.name AS project
FROM employees AS e
RIGHT JOIN projects p ON p.employee_id = e.id;
```

### `FULL JOIN`
Показывает все строки из обеих таблиц
```sql
SELECT e.name, p.name AS project
FROM employees AS e
FULL JOIN projects p ON p.employee_id = e.id;
```

### `ON`
Условие соединения
```sql
SELECT *
FROM employees AS e
JOIN department d ON e.department_id = d.id;
```

## 7. Алиасы

### `AS`
Даёт псевдоним колонке или таблице
```sql
SELECT name AS employee_name.
    salary AS monthly_salary
FROM employees AS e;
```

```sql
SELECT e.name
FROM employees e;
```

## 8. Ограничение таблиц

### `PRIMARY KEY`
Главный ключ
```sql
CREATE TABLE departments(
    id SERIAL PRIMARY KEY,
    name TEXT;
)
```

### `FOREIGN KEY`
Внешний ключ
```sql
CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    name TEXT,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id),
)
```

### `REFERNCES`
Указывает, на какую таблицу и колонку ссылается ключ
```sql
department_id INT REFERENCES departments(id);
```

### `NOT NULL`
Запрещает `NULL`
```sql
name TEXT NOT NULL;
```

### `NULL`
Отсутвует значение
```sql
INSERT INTO employees (name, salary, department_Id)
VALUES ('Иван', NULL, 1);
```

### `UNIQUE`
Значение должно быть уникальным
```sql
ALTER TABLE employees
ADD CONSTRAINT unique_employee_email UNIQUE (email); 
```

### `CONSTRAINT`
Даёт имя ограничению
```sql
ALTER TABLE employees
ADD CONSTRAINT salary_positive CHECK (salary > 0); 
```

### `CHECK`
Проверяет условие
```sql
ALTER TABLE employees
ADD CONSTRAINT salary_positive CHECK (salary > 0); 
```

### `DEFAULT`
Значение по умолчанию
```sql
ALTER TABLE projects
ALTER COLUMN is_active SET DEFAULT TRUE; 
```