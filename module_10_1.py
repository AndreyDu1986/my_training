import time
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time_functions = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time_functions = time.time()

print(f'Работа функций заняла: {end_time_functions - start_time_functions:.6f} секунд')

start_time_threads = time.time()

threads = []
for count, filename in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = Thread(target=write_words, args=(count, filename))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = time.time()

print(f'Работа потоков заняла: {end_time_threads - start_time_threads:.6f} секунд')