# d = {
#     "a": 1
#     "b": [1,2,3]
#     "bool": True
#     "nested": {
#         "a": 1
#     }
# }
# d_1 = dict(a=1)
# print(d, d_1)


# keys = ["a", "b", "c"]
# d = dict.fromkeys(keys, 1)

# # 1 способ
# print(d["d"])

# # 2 способ
# print(d.get("a"), d.get("d"))

# # 3 способ
# value = d.setdefault("a", 0)
# print(value)


# fr = ["apple", "banana", "apple"]
# d = {}

# for word in fr:
#     d.setdefault(word, 0)
#     d[word] += 1

# print(word)


# d = {"a": 1}
# d.update({"a": 2, "b": 3})
# d.update(c = 4, d = 5)

# # 1 способ
# d.pop("d")

# # 2 способ
# del d["c"]

# # 3 способ
# key, value = d.popitem()

# d.clear()

# print(d)


# d_1 = {"a": 1}
# d_1.update({"a": 2, "b": 3})
# d_1.update(c = 4, d = 5)

# if "e" not in d_1:
#     print("Ok")

# print(d_1.keys(), d_1.values())

# print(d_1.items())

# for key, value in d_1.items():
#     print(f"{key}={value}")

