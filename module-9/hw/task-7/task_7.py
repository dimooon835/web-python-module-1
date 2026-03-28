# incident_id|service|severity|duration_min|channel|acknowledged
rows = [
    'INC-100|checkout|critical|12|pager|yes',
    'INC-101|search|high|7|slack|no',
    'INC-102|billing|medium|zero|email|yes',
    'INC-103|video|critical|-3|pager|no',
    'INC-104|feed|warning|5|slack|yes',
    'INC-105|auth|low|2|sms|no',
    'INC-106|cdn|high|4|email|maybe',
    'INC-107|ml|medium|9|slack|no',
]


class IncidentProcessingError(Exception):
    pass


class IncidentFormatError(IncidentProcessingError):
    pass


class SeverityError(IncidentProcessingError):
    pass


class DurationError(IncidentProcessingError):
    pass


class ChannelError(IncidentProcessingError):
    pass


class AcknowledgedFlagError(IncidentProcessingError):
    pass


def parse_incident(row):
    # TODO: split строку по '|'
    # TODO: убрать лишние пробелы у частей через strip()
    # TODO: ожидать 6 частей: incident_id, service, severity, duration_raw, channel, acknowledged_raw
    # TODO: если частей не 6 -> raise IncidentFormatError(...)
    # TODO: duration_raw преобразовать в float
    # TODO: при ошибке преобразования использовать raise DurationError(...) from exc
    # TODO: проверить, что duration > 0
    # TODO: проверить severity в {'low', 'medium', 'high', 'critical'}
    # TODO: проверить channel в {'email', 'slack', 'pager'}
    # TODO: проверить acknowledged_raw в {'yes', 'no'}
    # TODO: превратить acknowledged_raw в bool
    # TODO: вернуть словарь с разобранными полями
    parts = [p.strip() for p in row.split('|')]
    
    if len(parts) != 6:
        raise IncidentFormatError(f"Неправильный формат {len(parts)}")
    
    inc_id, service, severity, duration_raw, channel, ack_raw = parts

    # Duration validation
    try:
        duration = float(duration_raw)
    except ValueError as exc:
        raise DurationError(f"Неверный duration формат: '{duration_raw}'") from exc
    
    if duration <= 0:
        raise DurationError(f"Duration должен быть позитивным {duration}")

    # Category validation
    if severity not in {'low', 'medium', 'high', 'critical'}:
        raise SeverityError(f"Неизвестный severity: '{severity}'")
        
    if channel not in {'email', 'slack', 'pager'}:
        raise ChannelError(f"Неизвестный channel: '{channel}'")
        
    if ack_raw not in {'yes', 'no'}:
        raise AcknowledgedFlagError(f"Неверный ack flag: '{ack_raw}'")

    return {
        'id': inc_id,
        'service': service,
        'severity': severity,
        'duration_min': duration,
        'channel': channel,
        'acknowledged': ack_raw == 'yes'
    }


def process_batch(rows):
    # TODO: создать списки incidents и errors
    # TODO: пройтись по rows циклом
    # TODO: внутри try вызвать parse_incident(row)
    # TODO: валидный incident добавить в incidents
    # TODO: IncidentProcessingError сохранить в errors как (row, error_type, message)
    # TODO: вернуть (incidents, errors)
    incidents = []
    errors = []
    for row in rows:
        try:
            incidents.append(parse_incident(row))
        except IncidentProcessingError as e:
            errors.append((row, type(e).__name__, str(e)))
    return incidents, errors


# TODO: вызвать process_batch(rows)
# TODO: вывести количество валидных инцидентов и количество ошибок
# TODO: собрать error_counts: dict[str, int]
# TODO: собрать unacked_by_channel: dict[str, list[str]] только для acknowledged == False
# TODO: собрать average_duration_by_severity только по валидным строкам
# TODO: найти longest_incident среди валидных инцидентов по duration_min
# TODO: красиво вывести получившиеся структуры

valid_incidents, processing_errors = process_batch(rows)

error_counts = {}
for _, err_type, _ in processing_errors:
    error_counts[err_type] = error_counts.get(err_type, 0) + 1

unacked_by_channel = {}
for inc in valid_incidents:
    if not inc['acknowledged']:
        ch = inc['channel']
        unacked_by_channel.setdefault(ch, []).append(inc['id'])

severity_totals = {}
for inc in valid_incidents:
    sev = inc['severity']
    stats = severity_totals.get(sev, [0.0, 0])
    stats[0] += inc['duration_min']
    stats[1] += 1
    severity_totals[sev] = stats

avg_duration_by_severity = {
    sev: round(total / count, 2) for sev, (total, count) in severity_totals.items()
}

longest_incident = max(valid_incidents, key=lambda x: x['duration_min']) if valid_incidents else None

print(f"Summary: {len(valid_incidents)} valid | {len(processing_errors)} errors")

print("\nError counts:")
for row, e_type, msg in processing_errors:
    print(f"  [{e_type}] {msg} | Row: {row}")

print("\nUnacknowledged by channel:")
for ch, ids in unacked_by_channel.items():
    print(f"  {ch}: {', '.join(ids)}")

print("\nAvg duration by severity:")
for sev, avg in avg_duration_by_severity.items():
    print(f"  {sev}: {avg} min")

if longest_incident:
    print(f"\nLongest incident: {longest_incident['id']} ({longest_incident['duration_min']} min)")