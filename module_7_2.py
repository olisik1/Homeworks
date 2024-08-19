
def custom_write(file_name, strings):
    strings_positions = {}  # Создаем пустой словарь для хранения позиций строк

    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            start_byte = file.tell()  # Получаем текущую позицию указателя в файле
            file.write(string + '\\n')  # Записываем строку и добавляем '\\n' в конец
            strings_positions[(line_number, start_byte)] = string  # Добавляем данные в словарь

    return strings_positions

# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
