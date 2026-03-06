rows = [
    ("Алиса", "Python Meetup", "Mon", "registered"),
    ("Алиса", "Python Meetup", "Mon", "attended"),
    ("Боб", "Data Talk", "Tue", "registered"),
    ("Кира", "Data Talk", "Tue", "attended"),
    ("Данил", "Design Review", "Wed", "cancelled"),
    ("Ева", "Python Meetup", "Thu", "waiting"),
    ("Боб", "Data Talk", "Tue", "registered")
]


class AttendanceRecord:
    # TODO:
    # реализуй __init__(person, event_name, day, status)
    def __init__(self, person, event_name, day, status):
        self.person = person
        self.event_name = event_name
        self.day = day
        self.status = status

    def to_dict(self):
        # TODO:
        # вернуть словарь с полями person, event_name, day, status
        return {
            "person": self.person,
            "event_name": self.event_name,
            "day": self.day,
            "status": self.status,
        }

    @classmethod
    def from_tuple(cls, row):
        # TODO:
        # 1) проверить длину row
        # 2) распаковать значения
        # 3) проверить статус
        # 4) вернуть (record, "") или (None, reason)
        if len(row) != 4:
            return None, "bad format"

        person, event_name, day, status = row
        allowed_statuses = {"registered", "attended", "cancelled"}

        if status not in allowed_statuses:
            return None, "bad status"

        return cls(person, event_name, day, status), ""


class AttendanceRegistry:
    def __init__(self):
        # TODO:
        self.records = []
        self.invalid_rows = []
        self.duplicates = []

    def add_record(self, record):
        # TODO:
        # проверить, есть ли уже запись с теми же person, event_name, day
        # если да:
        #    добавить (record.person, record.event_name, record.day) в self.duplicates
        #    не добавлять запись
        # иначе добавить record в self.records
        is_duplicate = any(
            r.person == record.person and
            r.event_name == record.event_name and
            r.day == record.day
            for r in self.records
        )

        if is_duplicate:
            self.duplicates.append((record.person, record.event_name, record.day))
        else:
            self.records.append(record)

    def load_rows(self, rows):
        # TODO:
        # пройти по rows
        # вызвать AttendanceRecord.from_tuple(row)
        # если запись невалидна -> self.invalid_rows.append((row, reason))
        # иначе -> self.add_record(record)
        for row in rows:
            record, reason = AttendanceRecord.from_tuple(row)
            if record is None:
                self.invalid_rows.append((row, reason))
            else:
                self.add_record(record)

    def event_stats(self):
        # TODO:
        # вернуть словарь статистики по мероприятиям и статусам
        stats = {}
        for r in self.records:
            if r.event_name not in stats:
                stats[r.event_name] = {}
            stats[r.event_name][r.status] = stats[r.event_name].get(r.status, 0) + 1
        return stats

    def person_history(self, person):
        # TODO:
        # вернуть список записей выбранного участника
        return [r.to_dict() for r in self.records if r.person == person]

    def active_events(self):
        # TODO:
        # вернуть множество событий, где есть хотя бы один status == 'attended'
        return {r.event_name for r in self.records if r.status == "attended"}

    def build_report(self):
        # TODO:
        # вернуть словарь с ключами:
        # total_valid_records, total_invalid_rows,
        # total_duplicates, event_stats, active_events
        return {
            "total_valid_records": len(self.records),
            "total_invalid_rows": len(self.invalid_rows),
            "total_duplicates": len(self.duplicates),
            "event_stats": self.event_stats(),
            "active_events": self.active_events()
        }


registry = AttendanceRegistry()
registry.load_rows(rows)
report = registry.build_report()

print("Корректных записей:", report["total_valid_records"])
print("Ошибок:", report["total_invalid_rows"])
print("Дублей:", report["total_duplicates"])
print("Статистика мероприятий:", report["event_stats"])
print("Активные мероприятия:", report["active_events"])