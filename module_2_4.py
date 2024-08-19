# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебираем каждый элемент в списке numbers
for num in numbers:
    if num <= 1:
        # Пропускаем число 1, так как оно не является простым или составным
        continue

    is_prime = True  # Предполагаем, что число простое

    # Проверяем число на простоту
    for divisor in range(2, int(num**0.5) + 1):  # Оптимизация: проверяем до корня числа
        if num % divisor == 0:
            is_prime = False  # Найден делитель, число не простое
            break  # Прерываем цикл, так как нашли делитель

    # Записываем число в соответствующий список
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим результаты
print("Primes:", primes)
print("Not Primes:", not_primes)