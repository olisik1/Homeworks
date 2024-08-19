def generate_password(n):
    result = ""

    # Генерируем пары (a, b)
    for a in range(1, 21): # от 1 до 20 включительно
        for b in range(a + 1, 21): # б должен быть больше а, чтобы избежать дублирования
            if a != n and b != n: # исключаем n из пар
                s = a + b
                if n % s == 0: # проверка кратности
                    result += f"{a}{b}" # добавляем пару в результат

    return result

# Пример использования
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Сгенерированный пароль для {n}: {password}")
else:
    print("Введите корректное число от 3 до 20.")