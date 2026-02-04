def numbers(num1, num2):
    if num2 == 0:
        return num1
    return numbers(num2, num1 % num2)

num1 = 15
num2 = 5
result = numbers(num1, num2)
print(f"Наибольший общий делитель чисел {num1} и {num2} равен {result}")