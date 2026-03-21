from dataclasses import dataclass
from typing import Optional, Protocol, Sequence, TypedDict


# rows: emp_id, name, department, email, is_active
rows = [
    {'emp_id': 1, 'name': 'Алиса', 'department': 'Data', 'email': 'alice@company.com', 'is_active': True},
    {'emp_id': 2, 'name': 'Боб', 'department': 'Backend', 'email': 'bob@company.com', 'is_active': True},
    {'emp_id': 3, 'name': 'Кира', 'department': 'Data', 'email': 'kira@company.com', 'is_active': False},
    {'emp_id': 4, 'name': 'Лев', 'department': 'QA', 'email': 'lev@company.com', 'is_active': True},
]


class EmployeeRow(TypedDict):
    # TODO: описать все поля структуры строки сотрудника
    # TODO: emp_id -> int
    emp_id: int

    # TODO: name -> str
    name: str

    # TODO: department -> str
    department: str

    # TODO: email -> str
    email: str

    # TODO: is_active -> bool
    is_active: bool


class EmployeeRepository(Protocol):
    def get_all(self) -> Sequence[EmployeeRow]:
        # TODO: аннотировать как -> Sequence[EmployeeRow]
        # TODO: вернуть всю коллекцию записей
        ...

    def get_by_id(self, emp_id: int) -> Optional[EmployeeRow]:
        # TODO: аннотировать как -> Optional[EmployeeRow]
        # TODO: вернуть запись по emp_id или None
        ...


DepartmentMap = dict[str, list[str]]


def build_index(rows: Sequence[EmployeeRow]) -> dict[int, EmployeeRow]:
    # TODO: аннотировать rows как Sequence[EmployeeRow]
    # TODO: аннотировать результат как dict[int, EmployeeRow]
    # TODO: собрать индекс по ключу emp_id
    return {row['emp_id']: row for row in rows}


class InMemoryEmployeeRepository:
    def __init__(self, rows: Sequence[EmployeeRow]):
        # TODO: аннотировать rows как Sequence[EmployeeRow]
        # TODO: сохранить rows внутри объекта
        self._rows = rows

    def get_all(self) -> Sequence[EmployeeRow]:
        # TODO: вернуть все записи
        return self._rows

    def get_by_id(self, emp_id: int) -> Optional[EmployeeRow]:
        # TODO: пройтись циклом по строкам
        # TODO: если row['emp_id'] == emp_id -> вернуть row
        # TODO: если никто не найден -> вернуть None
        for row in self._rows:
            if row['emp_id'] == emp_id:
                return row
        return None


@dataclass
class EmployeeService:
    repo: EmployeeRepository

    def active_names(self) -> list[str]:
        # TODO: аннотировать результат как list[str]
        # TODO: вернуть только имена активных сотрудников
        return [row['name'] for row in self.repo.get_all() if row['is_active']]

    def department_members(self, department: str) -> list[EmployeeRow]:
        # TODO: аннотировать department как str
        # TODO: аннотировать результат как list[EmployeeRow]
        # TODO: вернуть сотрудников нужного отдела
        return [row for row in self.repo.get_all() if row['department'] == department]

    def find_email(self, emp_id: int) -> Optional[str]:
        # TODO: аннотировать emp_id как int
        # TODO: аннотировать результат как Optional[str]
        # TODO: взять row = self.repo.get_by_id(emp_id)
        # TODO: если row is None -> вернуть None
        # TODO: иначе вернуть row['email']
        row = self.repo.get_by_id(emp_id)
        return row['email'] if row else None

    def group_by_department(self) -> DepartmentMap:
        # TODO: аннотировать результат как DepartmentMap
        # TODO: собрать dict department -> list[name]
        result: DepartmentMap = {}
        for row in self.repo.get_all():
            dept = row['department']
            result.setdefault(dept, []).append(row['name'])
        return result


repo = InMemoryEmployeeRepository(rows)
service = EmployeeService(repo)

# TODO: вывести build_index(rows)
print("Index:", build_index(rows))

# TODO: вывести service.active_names()
print("Active names:", service.active_names())

# TODO: вывести service.department_members('Data')
print("Data dept members:", service.department_members('Data'))

# TODO: вывести service.find_email(2)
print("Email for ID 2:", service.find_email(2))

# TODO: вывести service.group_by_department()
print("Grouped by dept:", service.group_by_department())