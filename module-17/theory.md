# 1. База данных

### `CREATE`
Создаёт объект: Таблица, база, индекс

```sql
CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NUlL,
  salary NUMERIC
)
```

### `TABLE`
Указывает, что создаётся или изменяется таблица

```sql
CREATE TABLE department (
  id SERIAL PRIMARY KEY,
  name TEXT
)
```

### `ALTER`
Изменяет существующий объект

```sql
ALTER TABLE employees
ADD COLUMN email TEXT;
```

### `ADD`
Добавляет колонку, ограничение

```sql
ALTER TABLE employees
ADD COLUMN phone TEXT;
```

### `DROP`
Удаляет объект(таблицу)

```sql
DROP TABLE projects;
```

### `IF EXISTS`
Позволяет избежать ошибки, если объекта нет

```sql
DROP TABLE IF EXISTS old_projects;
```

### `IF NOT EXISTS`
Создаёт объект только если его не существует

```sql
CREATE TABLE IF NOT EXISTS department (
  id SERIAL PRIMARY KEY,
  name TEXT
);
```

### `RENAME`
Переименовывает объект

```sql
ALTER TABLE employees
RENAME COLUMN name to full_name;
```

### `TRUNCATE`
Быстро очищает таблицу

```sql
TRUNCATE TABLE projects;
```

## 2. Работа с данными
### `SELECT`
Указывает источник данных

```sql
SELECT name, salary FROM employees;
```

### `INSERT`
Добавляет строки

```sql
INSERT INTO departments(name)
VALUES ('it'), ('HR'), ('finance');
```

### `INTO`
Указывает, куда вставлять данные

```sql
INSERT INTO employees(name, salary, department_id)
VALUES ('Анна', 12000, 1);
```

### `VALUES`
Передаёт конкретные значения

```sql
INSERT INTO projects(name, employee_id, budget)
VALUES ('CRM System', 1, 500000);
```