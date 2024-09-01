# import requests
from threading import Thread
import time

print(f'\n{' однопоточная запись в файлы ':*^60}')
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        cnt=1
        for _ in range(0, word_count):
            f.write(f'Какое-то слово № {cnt}\n')
            cnt += 1
    time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


t1=time.time()
write_words(10, 'example1')
write_words(30, 'example2')
write_words(200, 'example3')
write_words(100, 'example4')
print(f'Время работы программы: {round(time.time()-t1, 3)}')

print(f'\n{' многопоточная запись в файлы ':*^60}')
t1=time.time()
thr5 = Thread(target=write_words, args=(10, 'example5'))
thr6 = Thread(target=write_words, args=(30, 'example6'))
thr7 = Thread(target=write_words, args=(200, 'example7'))
thr8 = Thread(target=write_words, args=(100, 'example8'))

thr5.start(), thr6.start(), thr7.start(), thr8.start()
thr5.join(), thr6.join(), thr7.join(), thr8.join()
print(f'Время работы программы: {round(time.time()-t1, 3)}')
