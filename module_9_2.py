first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список длин строк в `first_strings`, где длина строки не менее 5
first_result = [len(s) for s in first_strings if len(s) >= 5]

# 2. Список пар слов (кортежей) одинаковой длины из `first_strings` и `second_strings`
second_result = [(first_word, second_word)
                 for first_word in first_strings
                 for second_word in second_strings
                 if len(first_word) == len(second_word)]

# 3. Словарь строк и их длины для строк с четной длиной из объединенных списков `first_strings` и `second_strings`
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}


print(first_result)
print(second_result)
print(third_result)