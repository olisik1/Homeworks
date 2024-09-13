def add_everything_up(a, b):
    try:
        # Попробуем сложить a и b как числа
        return a + b
    except TypeError:
        # Если возникло исключение TypeError, значит переменные разных типов
        return str(a) + str(b)

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))       # Вывод: яблоко4215
print(add_everything_up(123.456, 7))           # Вывод: 130.456
