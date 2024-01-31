from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from excels.Monitor import functions
from Configurations import config
import time

path_to_watch = config.EXCEL_PATH + '\In'
path_to_file = path_to_watch + '\check.xlsx'


class ExcelMonitor(FileSystemEventHandler):
    def __init__(self, root, obj_list, path_to_watch=path_to_watch, ):
        self.path_to_watch = path_to_watch
        self.observer = Observer()
        self.root = root
        self.obj_list = obj_list

        print('Запуск обсервера')

    def start(self):
        # Настраиваем observer...
        self.observer.schedule(self, path=self.path_to_watch, recursive=False)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()

    def on_modified(self, event):
        print('Запуск on_modified')
        if not event.is_directory:  # проверяем, что это не директория
            if event.src_path == config.EXCEL_PATH + '\In\check.xlsx':
                functions.on_file_modified(event, self.root, obj_list=self.obj_list)
                # self.callback(event.src_path)