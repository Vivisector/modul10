import queue
import threading
import random
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self): #ожидание (еда)
        wait_sec = random.randint(3, 11)
        print(f'{self.name} ест')
        time.sleep(wait_sec)

class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        # Перебираем каждого прибывающего гостя
        for guest in guests:
            # Пытаемся найти свободный стол
            free_table = None
            for table in self.tables:
                if table.guest is None:
                    free_table = table
                    break

            if free_table:
                # Если есть свободный стол, сажаем гостя
                free_table.guest = guest
                print(f'{guest.name} сел за стол номер {free_table.number}')
                guest.start()  # Запускаем поток гостя
            else:
                # Если свободных столов нет, добавляем гостя в очередь
                self.queue.put(guest)
                print(f'{guest.name} ждет в очереди')

    def discuss_guests(self):
        # Обслуживаем гостей, пока очередь не пустая или хотя бы один стол занят
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    # Если гость закончил кушать, освобождаем стол
                    print(f'{table.guest.name} (стол {table.number}) поел и ушёл')
                    print(f'Стол {table.number}(из {len(tables)}) свободен')
                    table.guest = None

                    # Проверяем, есть ли кто-то в очереди
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        print(f'{next_guest.name} вышел из очереди и сел за стол {table.number}')
                        next_guest.start()  # Запускаем поток гостя из очереди

            time.sleep(1)  # Проверяем столы и очередь с задержкой


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Armen',
'Viktoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
print('Кафе обслужило всю очередь и закончило работу...')