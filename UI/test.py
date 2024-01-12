# import os
# from Configurations import config
#
# import pandas as pd
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
#
#
# class ExcelUpdateHandler(FileSystemEventHandler):
#     def __init__(self, file_path, callback):
#         self.file_path = file_path
#
#         self.callback = callback
#
#     def on_modified(self, event):
#         # Реагировать только на изменения в интересующем нас файле
#         if event.src_path == self.file_path:
#             # Читаем файл
#             df = pd.read_excel(self.file_path)
#
#             # Получаем последние 10 строк из заданных колонок
#             last_rows = df.tail(5)
#             print(last_rows)
#
#             # Вызов функции обратного вызова с новыми данными
#             self.callback(last_rows)
#
#
# class ExcelMonitor:
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#         self.last_rows = None
#         self.event_handler = ExcelUpdateHandler(self.file_path,  self.update_last_rows)
#         self.observer = Observer()
#
#     def update_last_rows(self, new_rows):
#         # Здесь устанавливаем новое значение переменной
#         self.last_rows = new_rows
#         # Оповещаем о том, что файл был обновлён
#         print(f"File {self.file_path} has been updated. New rows received.")
#
#     def start(self):
#         # Получаем путь к каталогу и добавляем наблюдателя
#         directory = os.path.dirname(self.file_path)
#
#         # Настраиваем наблюдатель за изменениями в файле
#         self.observer.schedule(self.event_handler, path=directory, recursive=True)
#         self.observer.start()
#         print(f"Monitoring started on {self.file_path}")
#
#     def stop(self):
#         self.observer.stop()
#         self.observer.join()
#         print("Monitoring stopped.")
#
# # Пример использования
#
#
# file_path_to_monitor = config.EXCEL_PATH
# columns_to_monitor = ["A", "B"]
# excel_monitor = ExcelMonitor(file_path_to_monitor)
#
# try:
#     excel_monitor.start()
#     # Поместите в этот цикл свои собственные условия завершения или действия,
#     # которые должны выполняться одновременно с мониторингом.
#     while excel_monitor.observer.is_alive():
#         # Здесь может быть ваш код...
#         excel_monitor.observer.join(1)  # Проверяем истекший таймаут (1 секунда)
# except KeyboardInterrupt:
#     excel_monitor.stop()
# finally:
#     excel_monitor.stop()

import threading
from tkinter import Tk, Label
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import pandas as pd


def on_file_modified(event):
    # Это функция будет вызвана при изменении файла.
    # Заметьте, что мы не обновляем GUI напрямую здесь!
    # print(f"File {event.src_path} has been modified.")
    # Используем метод after для обновления GUI в главном потоке.
    root.after(0, update_ui, event.src_path)


class Check:
    def __init__(self):
        self.q = 1
        self.q_h = 2

check = Check()
class ExcelMonitor(FileSystemEventHandler):
    def __init__(self):
        self.observer = Observer()

    def start(self):
        # Настраиваем observer...
        self.observer.schedule(self, path='D:\Max\CleanWaterMain\excels', recursive=False)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()

    def on_modified(self, event):
        if not event.is_directory:  # проверяем, что это не директория
            on_file_modified(event)


def update_ui(file_path, obj=check):
    # # Обновите элементы Tkinter здесь безопасным образом.
    # row = pd.read_excel('D:\Max\CleanWaterMain\excels\check.xlsx').tail(1)
    # print(f'До obj.q={type(obj.q)}, obj.q_h={obj.q_h}')
    # for el in list(row.columns):
    #     setattr(obj, el, row[el].values[-1])
    # # print(f'После obj.q={obj.q}, SSSSSS obj.q_h={obj.q_h}')
    # label_1.config(text=obj.q)
    # label_2.config(text=obj.q_h)
    print('UI updated')


def monitor_filesystem():
    excel_monitor.start()
    try:
        while excel_monitor.observer.is_alive():
            # sleep for a while and then check again
            time.sleep(1)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        excel_monitor.stop()

excel_monitor = ExcelMonitor()

root = Tk()
label_1 = Label(root, text="Waiting for file changes...")
label_1.pack()
label_2 = Label(root, text="Waiting for file changes...")
label_2.pack()
# Запускаем файловый монитор в отдельном потоке.
threading.Thread(target=monitor_filesystem, daemon=True).start()
root.mainloop()




