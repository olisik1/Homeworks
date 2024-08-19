def single_root_words(root_word, *other_words):
    # Приводим корневое слово к нижнему регистру для учета регистра
    root_word_lower = root_word.lower()
    # Создаем пустой список для хранения подходящих слов
    same_words = []

    # Перебираем остальные слова
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()
        # Проверяем, содержится ли корневое слово в текущем слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            # Если условие выполняется, добавляем слово в список
            same_words.append(word)

    # Возвращаем результат
    return same_words

# Пример использования функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

