import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.warriors = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.warriors >0:
            time.sleep(1)
            self.days += 1
            self.warriors -= self.power
            print(f'{self.name} сражается {self.days} дней, осталось {100-self.days*self.power} количество воинов.')

        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()
print('Все битвы закончились!')