def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if result == 1:
            print("Число 1 не является ни простым, ни составным")
        elif result < 1:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")

        return result

    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

# Пример использования
result = sum_three(2, 3, 6)
print(result)

result = sum_three(1, 0, 0)  # Проверка для числа 1
print(result)

result = sum_three(2, 2, 2)
print(result)
