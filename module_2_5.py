
def get_matrix(n, m, value):
    # Если количество строк или столбцов 0 или меньше, возвращаем пустой список
    if n <= 0 or m <= 0:
        return []

    # Создаем пустой список matrix
    matrix = []

    # Внешний цикл для создания строк
    for i in range(n):
        # Создаем пустую строку
        row = []

        # Внутренний цикл для заполнения строки значениями
        for j in range(m):
            row.append(value)

        # Добавляем заполненную строку в матрицу
        matrix.append(row)

    # Возвращаем готовую матрицу
    return matrix

# Пример результатов выполнения функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
