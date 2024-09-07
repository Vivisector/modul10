import time
from multiprocessing import Pool

#lined execution
def read_info(name):
    with open (name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break

files = [f'./10_5/file {number}.txt' for number in range(1,5)]
start = time.time()
# for f in files:
#     read_info(f)
#
# print(f'Line reading: {time.time()-start}') # 1.78
# exit()

#multiproc execution
def process_file(file):
    # full_path = file
    return read_info(file)  # Читаем файл


if __name__ == '__main__':
    start = time.time()

    # Многопроцессорное выполнение - 0.74 s
    with Pool(4) as p:
        p.map(process_file, files)

    print(f'Multiproc reading: {time.time() - start}')



