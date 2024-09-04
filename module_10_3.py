import time
import random
import threading

lock = threading.Lock()

class Bank:
    # def __init__(self, balance, lock):
    def __init__(self):
        self.balance = 0

    def deposit(self):
        for _ in range(100):
            add = random.randint(50, 500)
            self.balance +=add
            print(f'ПОПОЛНЕНИЕ {add}. Баланс: {self.balance}')
            if self.balance<=500 and lock.locked():
                lock.release()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            add_back = random.randint(50, 500)
            print(f'Запрос на СНЯТИЕ {add_back}')
            if add_back <= self.balance:
                self.balance -= add_back
                print(f'Снятие: {add_back}. Баланс: {self.balance}')
            else:
                print('- '*30) # метка для визуального контроля данной ситуации в консоли
                print(f'Недостаточно средств. Запрошенные {add_back} больше остатка {self.balance}')
                print('- ' * 30)
                lock.acquire()

            time.sleep(0.001)

bank = Bank()
print('- '*20)
thr_deposite = threading.Thread(target=bank.deposit)
thr_take = threading.Thread(target=bank.take)

thr_deposite.start()
thr_take.start()

thr_deposite.join()
thr_take.join()
print(F' "Итоговый баланс: {bank.balance}')

