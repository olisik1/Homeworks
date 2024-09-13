import threading
import time

# Общее количество врагов для всех рыцарей
total_enemies = 100

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        global total_enemies
        days = 0
        print(f"{self.name}, на нас напали!")
        while total_enemies > 0:
            days += 1
            time.sleep(1)  # Задержка в 1 секунду, имитирующая 1 день сражения
            if total_enemies <= 0:
                break
            total_enemies -= self.power
            if total_enemies < 0:
                total_enemies = 0
            print(f"{self.name}, сражается {days} день(дня)..., осталось {total_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

def main():
    # Создание экземпляров рыцарей
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight('Sir Galahad', 20)

    # Запуск потоков
    first_knight.start()
    second_knight.start()

    # Ожидание завершения потоков
    first_knight.join()
    second_knight.join()

    # Вывод строки об окончании битв
    print("Все битвы закончились!")

if __name__ == "__main__":
    main()