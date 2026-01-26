# def func_1():
#     result = []
#     for i in range(5):
#         result.append(i)
#     return result

# print(func_1())


# def func_2():
#     for i in range(5):
#         yield i
#     # for i in func_2():
#     #     print(i)

# gen = func_2()

# print(gen)
# print(next(gen))
# print(next(gen))


# def factorial(n):
#     # Базовый случай
#     if n <= 1:
#         return 1
#     # Рекурсивный шаг
#     # 9! = 9 * 8 * 7 * 6 * 5 ...
#     return n * factorial(n - 1)

# print(factorial(5))


# def power(x, n):
#     # Базовый случай
#     if n == 1:
#         return x
#     # Рекурсивный шаг
#     return x * power(x, n - 1)

# print(power(2, 3))


# def func_2(a, b):
#     if a >= b:
#         return 0
#     return a + func(a + 1, b)
# start = int(input("Введите число a: "))
# end = int(input("Введите число b: "))
# result = func(start, end)

# print(f"Сумма чисел: {result}")


# def func_3(n):
#     if n <= 0:
#         return 0
#     print("*", end="")
#     func_3(n - 1)

# func_3(5)


# import random

# board = [" " for _ in range(9)]
# wins = [
#     (0, 1, 2), (3, 4, 5), (6, 7, 8),
#     (0, 3, 6), (1, 4, 7), (2, 5, 8),
#     (0, 4, 8), (2, 4, 6)
# ]

# def print_board():
#     print(f"{board[0]} | {board[1]} | {board[2]}")
#     print(f"--+---+--")
#     print(f"{board[3]} | {board[4]} | {board[5]}")
#     print(f"--+---+--")
#     print(f"{board[6]} | {board[7]} | {board[8]}")

# def is_draw():
#     return " " not in board

# def check_wins(s):
#     for a,b,c in wins:
#         if board[a] == board[b] == board[c] == s:
#             return True
#     return False

# def computer_move():
#     empty_cells = [i for i in range(9) if board[i] == " "]
#     if not empty_cells:
#         return
#     move = random.choice(empty_cells)
#     board[move] = "O"

# def tic_tac_toe(board):
#     while True:
#         print_board()
#         move = int(input("Ход(0-9):"))

#         if move < 0 or move > 8 or board[move] != " ":
#             print("Неверный ход.")
#             continue

#         board[move] = "X"

#         if check_wins("X"):
#             print_board()
#             print("Победа")
#             break

#         if is_draw():
#             print_board()
#             print("Ничья")
#             break

#         computer_move()

#         if check_wins("O"):
#             print_board()
#             print("Поражение")
#             break

#         if is_draw():
#             print_board()
#             print("Ничья")
#             break

# tic_tac_toe(board)


# import random

# best_position = 0
# best_sum = None
# nums = [random.randint(-50, 50) for _ in range(100)]

# def func_5_1(i, nums):
#     for i,_ in enumerate(nums):
#         if i + 10 > len(nums):
#             break
    
#     summ = sum(nums[i: i + 10])
#     if best_sum == None or summ < best_sum:
#         best_sum = summ
#         best_position = i

# print(f"Минимальная последовательность: {nums[best_position: best_position + 10]}")

import random

nums = [random.randint(-50, 50) for _ in range(100)]

def func_5_2(i, best_pos=0, best_sum=None):
    if i + 10 > len(nums):
        return best_pos
    
    summ = sum(nums[i:i + 10])
    if best_sum == None or summ < best_sum:
        best_sum = summ
        best_pos = i
    return func_5_2(i + 1, best_pos, best_sum)

best_pos = func_5_2(0)
print(f"Минимальная последовательность: {nums[best_pos:best_pos + 10]}")