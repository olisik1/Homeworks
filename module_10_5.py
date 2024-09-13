import os
import time
from multiprocessing import Pool


def readinfo(file_name):
    alldata = []
    try:
        with open(file_name, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                alldata.append(line)
    except FileNotFoundError:
        print(f"Файл не найден: {file_name}")
    return alldata

file_names = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]

def linear_read(files):
    start_time = time.time()
    for file_name in files:
        readinfo(file_name)
    end_time = time.time()
    print(f"Время линейного выполнения: {end_time - start_time} секунд")

def multiprocess_read(files):
    start_time = time.time()
    with Pool() as pool:
        pool.map(readinfo, files)
    end_time = time.time()
    print(f"Время многопроцессного выполнения: {end_time - start_time} секунд")

if __name__ == "__main__":
  
    existing_files = [file for file in file_names if os.path.exists(file)]
    if not existing_files:
        print("Ни один из указанных файлов не найден.")
    else:
        
        multiprocess_read(existing_files)
