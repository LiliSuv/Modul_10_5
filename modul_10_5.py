from multiprocessing import Pool
from time import sleep
from datetime import datetime
def read_info(name):
    all_data=[]
    for file_name in name:
        with open (file_name, mode='r', encoding='UTF-8') as file:
            while True:
                text = file.readline ()
                if not text:
                    break
    all_data.append (text)
files = ['file 1.txt','file 2.txt','file 3.txt','file 4.txt']
start = datetime.now ()
(read_info (files))
time_1_end = datetime.now ()
print(f'Время срабатывания линейного вывода  {time_1_end-start}')
if __name__ == '__main__':
    start = datetime.now ()
    with Pool (4) as pool:
        pool.map (read_info, files)
    time_2_end = datetime.now ()
    print (f'Многопроцессный вызов: {time_2_end - start}')

