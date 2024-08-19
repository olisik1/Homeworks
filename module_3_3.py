def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызов функции с разными аргументами
print_params()                      # Вывод: 1 строка True
print_params(10, 'другая строка')   # Вывод: 10 другая строка True
print_params(b=25)                  # Вывод: 1 25 True
print_params(c=[1, 2, 3])           # Вывод: 1 строка [1, 2, 3]

# Создаем список с тремя элементами разных типов
values_list = [42, 'example', False]

# Создаем словарь с тремя ключами и значениями разных типов
values_dict = {'a': 42, 'b': 'example', 'c': False}

# Передаем values_list и values_dict в функцию print_params
print_params(*values_list)          # Вывод: 42 example False
print_params(**values_dict)         # Вывод: 42 example False

# Создаем список с двумя элементами
values_list_2 = [54.32, 'Строка']

# Передаем распакованный список и отдельный параметр в функцию
print_params(*values_list_2, 42)    # Вывод: 54.32 'Строка' 42


def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Демонстрация работы функции с различными вызовами
print_params()                      # Вывод: 1 строка True
print_params(10, 'другая строка')   # Вывод: 10 другая строка True
print_params(b=25)                  # Вывод: 1 25 True
print_params(c=[1, 2, 3])           # Вывод: 1 строка [1, 2, 3]

# Работа с распаковкой
values_list = [42, 'example', False]
values_dict = {'a': 42, 'b': 'example', 'c': False}
print_params(*values_list)          # Вывод: 42 example False
print_params(**values_dict)         # Вывод: 42 example False

# Работа с распаковкой + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)    # Вывод: 54.32 'Строка' 42