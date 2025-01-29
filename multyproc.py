import os
import time
from multiprocessing import Pool

def read_info(filename):
    all_data = []
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line:
            all_data.append(line)
            line = file.readline().strip()
    return all_data

if __name__ == '__main__':
    files_dir = './data_files/'
    filenames = [os.path.join(files_dir, f) for f in os.listdir(files_dir) if os.path.isfile(os.path.join(files_dir, f))]

    start_time = time.time()

    for filename in filenames:
        data = read_info(filename)

    linear_execution_time = time.time() - start_time
    print(f"Время линейного выполнения: {linear_execution_time:.6f} секунд")

    start_time = time.time()

    with Pool() as pool:
        results = pool.map(read_info, filenames)

    multiprocessing_execution_time = time.time() - start_time
    print(f"Время многопроцессорного выполнения: {multiprocessing_execution_time:.6f} секунд")