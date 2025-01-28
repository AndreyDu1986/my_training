import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days_fought = 0

    def run(self):
        global enemies_left

        print(f"{self.name}, на нас напали!")

        while enemies_left > 0:
            self.days_fought += 1
            enemies_left -= self.power

            if enemies_left <= 0:
                break

            print(f"{self.name} сражается {self.days_fought} день(дня)..., осталось {enemies_left} воинов.")
            time.sleep(1)

        print(f"{self.name} одержал победу спустя {self.days_fought} дней(дня)!")

enemies_left = 100

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")