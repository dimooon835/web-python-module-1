# service|max_retries|timeout_sec|environment|enabled
rows = [
    'auth|3|1.5|prod|on',
    'billing|0|2.0|stage|on',
    'search|two|0.8|dev|off',
    'media|5|-1|prod|on',
    'chat|4|1.2|test|off',
    'mail|2|0.5|stage|maybe',
    'worker|1|3.4|prod|on',
]


class DeployConfigError(Exception):
    pass


class RowFormatError(DeployConfigError):
    pass


class RetriesError(DeployConfigError):
    pass


class TimeoutError(DeployConfigError):
    pass


class EnvironmentError(DeployConfigError):
    pass


class EnabledFlagError(DeployConfigError):
    pass


def parse_config(row):
    # TODO: распарсить строку и провалидировать max_retries, timeout_sec, environment, enabled
    # TODO: при ошибках конвертации использовать raise ... from ...
    # TODO: enabled вернуть как bool
    parts = row.split('|')
    if len(parts) != 5:
        raise RowFormatError(f"Неправильный формат: {row}")
    
    srv, retries, timeout, env, enabled = parts

    try:
        max_retries = int(retries)
    except ValueError as e:
        raise RetriesError(f"Некорректные попытки: {retries}") from e
    
    try:
        timeout_sec = float(timeout)
        if timeout_sec < 0:
            raise TimeoutError(f"Отрицательное время: {timeout}")
    except ValueError:
        raise TimeoutError(f"Некорректное время: {timeout}") from e
    
    if env not in ['prod', 'stage', 'dev', 'test']:
        raise EnvironmentError(f"Неизвестное значение: {env}")
    
    if enabled not in ['off', 'on']:
        raise EnabledFlagError(f"Неправильное значение: {enabled}")
    
    return {
        "service": srv,
        "max_retries": max_retries,
        "timeout_sec": timeout_sec,
        "environment": env,
        "enabled": enabled == 'on'
    }

def load_configs(rows):
    # TODO: вернуть (configs, errors)
    configs, errors = [], []
    for r in rows:
        try:
            res = parse_config(r)
            configs.append(res)
        except DeployConfigError as e:
            errors.append(e)
    return configs, errors

# TODO: вызвать load_configs(rows)
configs, errors = load_configs(rows)

# TODO: вывести число валидных конфигов и число ошибок
print(f"Валидные конфиги: {len(configs)}. Ошибки: {len(errors)}")

# TODO: вывести ошибки по типам
print(f"\nОшибки по типам:")
for err in errors:
    print(f"- {type(err).__name__}: {err}")

# TODO: собрать enabled_by_environment: dict[str, list[str]]
enabled_by_env = {}
active_timeouts = []

for c in configs:
    if c['enabled']:
        env = c['environment']
        enabled_by_env.setdefault(env, []).append(c['service'])
        active_timeouts.append(c['timeout_sec'])

# TODO: посчитать average_timeout только по enabled=True
print(f"\nВключенные от env: {enabled_by_env}")
if active_timeouts:
    print(f"\nСредний timeout: {sum(active_timeouts)/len(active_timeouts):.2f}")