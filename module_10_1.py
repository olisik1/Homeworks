
import time
from time import sleep
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(word_count):
            f.write(f"Какое-то слово № {i + 1}\\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Взятие текущего времени
start_time = time.time()

# Запуск функций с аргументами из задачи (последовательно)
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
end_time = time.time()

# Вывод разницы начала и конца работы функций
print(f'Работа функций {end_time - start_time}')

# Взятие текущего времени перед запуском потоков
start_time = time.time()

# Создание и запуск потоков с аргументами из задачи
threads = []
thread_args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

for args in thread_args:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

# Взятие текущего времени после завершения потоков
end_time = time.time()

# Вывод разницы начала и конца работы потоков
print(f'Работа потоков {end_time - start_time}')