# Создаём переменную calls для отслеживания количества вызовов
calls = 0

# Функция count_calls для инкрементации счётчика вызовов
def count_calls():
    global calls
    calls += 1

# Функция string_info для обработки строки
def string_info(string):
    count_calls()  # Увеличить счётчик вызовов
    return (len(string), string.upper(), string.lower())

# Функция is_contains для проверки наличия строки в списке
def is_contains(string, list_to_search):
    count_calls()  # Увеличить счётчик вызовов
    string = string.lower()  # Привести строку к нижнему регистру
    list_to_search = [s.lower() for s in list_to_search]  # Привести все элементы списка к нижнему регистру
    return string in list_to_search

# Вызовы функций с произвольными данными и вывод результатов
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

# Вывод значения переменной calls на экран
print(calls)