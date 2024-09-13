def all_variants(text):
    length = len(text)
    # Внешний цикл по началу подстроки
    for start in range(length):
        # Внутренний цикл по концу подстроки (от start до конца строки)
        for end in range(start + 1, length + 1):
            yield text[start:end]

# Пример использования функции-генератора
a = all_variants("abc")
for i in a:
    print(i)