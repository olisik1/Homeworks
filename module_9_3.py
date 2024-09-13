first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# first_result: вычисляем разницу длин строк, если они не равны
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# second_result: сравниваем длины строк на одинаковых позициях (без zip)
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результатов
print(list(first_result))  # Ожидаемый вывод: [1, 2]
print(list(second_result))  # Ожидаемый вывод: [False, False, True]