# def func_1():
#     print("Function")

# def func_2():
#     return "Hello"

# def func_3():
#     pass

# def func_4(name, age, city):
#     print(f"{name}-{age}-{city}")

# func_1()
# print(func_2())
# func_4(name="Dima", age="21", city="Cheboksary")


# def func_5(*args):
#     total = 0
#     for num in args:
#         total += num
#     print(total)

# func_5(1,2,3,4,5)


# def func_6(**kwargs):
#     print(kwargs)

# func_6(name=1, age=2)


# def func_7(num1, num2, *args, **kwargs):
#     print(f"{num1}, {num2}")
#     print(args)
#     print(kwargs)

# func_7(1, 2, 3, 4, 5, name=1)


# def func_8(obj):
#     print(obj)

# func_8({"a": 1, "b": 2})


# def func_1(num1, num2):
#     min_num = min(num1, num2)
#     max_num = max(num1, num2)

#     for num in range(min_num, max_num):
#         if num % 2 != 0:
#             print(num)

# func_1(1, 10)


# def func_2(length, direction, symbol):
#     if direction == "h":
#         print(symbol * length)
#     elif direction == "v":
#         for _ in range(length):
#             print(symbol)

# func_2(10, "h", "*")
# func_2(10, "v", "#")


# def func_3(num1, num2, num3, num4):
#     return max(num1, num2, num3, num4)

# result = func_3(4, 9, 6, 3)
# print(result)


# def func_4(num1, num2):
#     return sum(range(num1, num2))

# result = func_4(5, 9)
# print(result)


def func_5(number):
    num = str(number)

    if len(num) != 6:
        return False
    
    sum1 = int(num[0]) + int(num[1]) + int(num[2])
    sum2 = int(num[3]) + int(num[4]) + int(num[5])

    return sum1 == sum2

print(func_5(123420))
print(func_5(723422))