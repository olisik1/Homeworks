#1. requests

#Описание библиотеки: Библиотека requests предназначена для выполнения HTTP-запросов на Python. Это позволяет получать данные с удаленных серверов, отправлять данные на сервер и выполнять другие задачи, связанные с HTTP.
#Документация: requests documentation
#Пример кода:
import requests

# Выполним GET запрос к API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Выведем статусный код ответа
print(f"Status Code: {response.status_code}")

# Выведем заголовки ответа
print(f"Headers: {response.headers}")

# Выведем текст ответа в формате JSON
print(f"Content: {response.json()}")

#Возможности:
#DET/POST запросы: возможность отправлять GET, POST, PUT, DELETE и другие типы HTTP-запросов.
#Обработка ответа: автоматическое декодирование ответа, работа с JSON, XML и др.
#Аутентификация: поддержка различных видов аутентификации, таких как API ключи и OAuth.


#2. pandas

#Описание библиотеки: pandas предназначена для обработки данных, предоставляя мощные средства для манипуляции и анализа данных. Это библиотека для работы с таблицами и временными рядами.
#Документация: pandas documentation
#Пример кода:


import pandas as pd

# Считываем данные из CSV файла
data = pd.read_csv('data.csv')

# Печатаем первые 5 строк для просмотра данных
print(data.head())

# Выполним простой анализ: среднее значение одного из столбцов
mean_value = data['some_column'].mean()
print(f"Mean value of some_column: {mean_value}")

# Группировка данных по столбцу и суммирование
grouped_data = data.groupby('group_column').sum()
print(grouped_data)

#Возможности:

#Чтение/Запись данных: поддержка различных форматов данных (CSV, Excel, SQL и др.).
#Манипуляции с данными: сортировка, фильтрация, агрегация и пр.
#Анализ данных: вычисление статистических показателей, объединение данных и т. д.

3. matplotlib

#Описание библиотеки: matplotlib является библиотекой для создания визуализаций данных. Она предоставляет обширные возможности для создания различных типов графиков и диаграмм.

#Документация: matplotlib documentation

#Пример кода:


import matplotlib.pyplot as plt

# Пример данных
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Сюжет (plot)
plt.plot(x, y)
plt.title('Sample plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

# Гистограмма
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
plt.hist(data, bins=5, edgecolor='black')
plt.title('Sample Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Круговая диаграмма (pie chart)
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Sample Pie chart')
plt.show()

#Возможности:
#Графики и диаграммы: поддержка линейных графиков, гистограмм, круговых диаграмм и других типов визуализаций.
#Кастомизация: возможность настройки внешнего вида графиков, добавление меток, легенд и прочего.
#Интеграция: работа с другими библиотеками для данных, например, NumPy и pandas.


