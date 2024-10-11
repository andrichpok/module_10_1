import threading
import time
from datetime import datetime
from threading import Thread
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


def func():
    start_func = datetime.now()


    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")


    end_func = datetime.now()
    res_func = end_func - start_func

    print(f'Работа функций {res_func}')


    start_thread = datetime.now()

    thr_first = threading.Thread(target = write_words, args = (10, 'example5.txt'))
    thr_second = threading.Thread(target = write_words, args = (30, 'example6.txt'))
    thr_third = threading.Thread(target = write_words, args = (200, 'example7.txt'))
    thr_fourth = threading.Thread(target = write_words, args = (100, 'example8.txt'))

    thr_first.start()
    thr_second.start()
    thr_third.start()
    thr_fourth.start()

    thr_first.join()
    thr_second.join()
    thr_third.join()
    thr_fourth.join()

    end_thread = datetime.now()
    res_thread = end_thread - start_thread

    print(f'Работа потоков {res_thread}')

if __name__ == '__main__':
    func()


