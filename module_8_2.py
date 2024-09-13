def personalsum(numbers):
    result = 0
    incorrectdata = 0

    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrectdata += 1
            print(f'Некорректный тип данных для подсчёта суммы - {number}')

    return result, incorrectdata


def calculateaverage(numbers):
    try:
        total, incorrectdata = personalsum(numbers)
        valid_count = len(numbers) - incorrectdata
        return total / valid_count if valid_count > 0 else 0
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Пример вызовов функции calculateaverage
print(f'Результат 1: {calculateaverage("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculateaverage([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculateaverage(567)}')  # Передана не коллекция
print(f'Результат 4: {calculateaverage([42, 15, 36, 13])}')  # Всё должно работать
