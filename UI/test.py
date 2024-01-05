import os
from Configurations import config

import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ExcelUpdateHandler(FileSystemEventHandler):
    def __init__(self, file_path, callback):
        self.file_path = file_path

        self.callback = callback

    def on_modified(self, event):
        # Реагировать только на изменения в интересующем нас файле
        if event.src_path == self.file_path:
            # Читаем файл
            df = pd.read_excel(self.file_path)

            # Получаем последние 10 строк из заданных колонок
            last_rows = df.tail(5)
            print(last_rows)

            # Вызов функции обратного вызова с новыми данными
            self.callback(last_rows)


class ExcelMonitor:
    def __init__(self, file_path):
        self.file_path = file_path

        self.last_rows = None
        self.event_handler = ExcelUpdateHandler(self.file_path,  self.update_last_rows)
        self.observer = Observer()

    def update_last_rows(self, new_rows):
        # Здесь устанавливаем новое значение переменной
        self.last_rows = new_rows
        # Оповещаем о том, что файл был обновлён
        print(f"File {self.file_path} has been updated. New rows received.")

    def start(self):
        # Получаем путь к каталогу и добавляем наблюдателя
        directory = os.path.dirname(self.file_path)

        # Настраиваем наблюдатель за изменениями в файле
        self.observer.schedule(self.event_handler, path=directory, recursive=False)
        self.observer.start()
        print(f"Monitoring started on {self.file_path}")

    def stop(self):
        self.observer.stop()
        self.observer.join()
        print("Monitoring stopped.")

# Пример использования


file_path_to_monitor = config.EXCEL_PATH
columns_to_monitor = ["A", "B"]
excel_monitor = ExcelMonitor(file_path_to_monitor)

try:
    excel_monitor.start()
    # Поместите в этот цикл свои собственные условия завершения или действия,
    # которые должны выполняться одновременно с мониторингом.
    while excel_monitor.observer.is_alive():
        # Здесь может быть ваш код...
        excel_monitor.observer.join(1)  # Проверяем истекший таймаут (1 секунда)
except KeyboardInterrupt:
    excel_monitor.stop()
finally:
    excel_monitor.stop()




