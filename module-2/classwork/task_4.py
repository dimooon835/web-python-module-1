text = "Hello World"
replacements = {"e": 1, "l": 0, "o": 2, "r": 3}

result = ""
for char in text:
    result += str(replacements.get(char, char))
print(result)