def apply_all_func(int_list, *functions):
    # Создаем пустой словарь для хранения результатов
    results = {}

    # Перебираем все переданные функции
    for func in functions:
        try:
            # Вызываем функцию с переданным списком и записываем результат в словарь
            results[func.__name__] = func(int_list)
        except Exception as e:
            # В случае ошибки, записываем её в словарь
            results[func.__name__] = str(e)

    # Возвращаем словарь с результатами
    return results

# Примеры использования
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))