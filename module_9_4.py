#Lambda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'

# Lambda функция, которая проверяет совпадение символов в той же позиции
result = list(map(lambda x, y: x == y, first, second))

print(result)

#Результат:


[False, True, True, False, False, False, False, False, True, False, False, False, False, False]

#Замыкание

def getadvancedwriter(filename):
    def writeeverything(*dataset):
        with open(filename, 'a', encoding='utf-8') as f:
            for data in dataset:
                f.write(str(data) + '\\n')
    return writeeverything

write = getadvancedwriter('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Этот код создаст или откроет файл example.txt и добавит в него данные в указанном формате.


#Класс MysticBall

from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

firstball = MysticBall('Да', 'Нет', 'Наверное')

print(firstball())
print(firstball())
print(firstball())

#Этот класс создает объект MysticBall, который при каждом вызове (firstball()) случайным образом возвращает одну из переданных строк.


#Объединяем все задания в один модуль:


# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)

# Замыкание
def getadvancedwriter(filename):
    def writeeverything(*dataset):
        with open(filename, 'a', encoding='utf-8') as f:
            for data in dataset:
                f.write(str(data) + '\\n')
    return writeeverything

write = getadvancedwriter('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Класс MysticBall
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

firstball = MysticBall('Да', 'Нет', 'Наверное')

print(firstball())
print(firstball())
print(firstball())
