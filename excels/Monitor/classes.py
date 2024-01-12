from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from excels.Monitor import functions
from Configurations import config
import time

path = config.EXCEL_PATH



class ExcelMonitor(FileSystemEventHandler):
    def __init__(self, root, obj_list, path=path):
        self.path = path
        self.observer = Observer()
        self.root = root
        self.obj_list = obj_list
        print('Запуск обсервера')

    def start(self):
        # Настраиваем observer...
        self.observer.schedule(self, path=self.path, recursive=False)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()

    def on_modified(self, event):
        if not event.is_directory:  # проверяем, что это не директория
            functions.on_file_modified(event, self.root, obj_list=self.obj_list)