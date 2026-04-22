tree = {
    "name": "app",
    "build_minutes": 4,
    "children": [
        {
            "name": "api",
            "build_minutes": 8,
            "children": [
                {"name": "auth", "build_minutes": 11, "children": []},
                {"name": "payments", "build_minutes": 6, "children": []},
            ],
        },
        {
            "name": "frontend",
            "build_minutes": 7,
            "children": [
                {"name": "ui-kit", "build_minutes": 3, "children": []},
                {"name": "charts", "build_minutes": 9, "children": []},
            ],
        },
    ],
}

limit = 8

stack = [(tree, [tree["name"]])]
total_build_minutes = 0
leaf_modules = []
slow_modules = []

# TODO 1: пока stack не пуст, извлекайте элемент через pop()
# TODO 2: распакуйте его в node и path
while stack:
    node, path = stack.pop()

# TODO 3: увеличьте total_build_minutes на node['build_minutes']
    total_build_minutes += node["build_minutes"]

# TODO 4: если node['build_minutes'] > limit,
#   добавьте в slow_modules словарь:
#   {'module': node['name'], 'minutes': node['build_minutes'], 'path': ' -> '.join(path)}
    if node["build_minutes"] > limit:
        slow_modules.append({
            'module': node["name"],
            'minutes': node["build_minutes"],
            'path': ' -> '.join(path)
    })

# TODO 5: если у node нет детей, добавьте node['name'] в leaf_modules
# TODO 6: если дети есть, положите каждого ребёнка в stack
# TODO 7: для ребёнка соберите новый путь child_path = path + [child['name']]
# TODO 8: добавляйте в stack кортеж (child, child_path)
    if not node["children"]:
        leaf_modules.append(node["name"])
    else:
        for child in node["children"]:
            child_path = path + [child["name"]]
            stack.append((child, child_path))


print("Общее время сборки:", total_build_minutes)
print("Листовые модули:", leaf_modules)
print("Модули дольше лимита:", slow_modules)
