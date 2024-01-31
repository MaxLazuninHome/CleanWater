import time
from Functions.functions import calculate


def on_file_modified(event, root, obj_list):
    # Это функция будет вызвана при изменении файла.
    # Заметьте, что мы не обновляем GUI напрямую здесь!
    # print(f"File {event.src_path} has been modified.")
    # Используем метод after для обновления GUI в главном потоке.
    root.after(0, update_ui(obj_list), event.src_path)


def update_ui(obj_list):
    obj_list = obj_list
    # Обновите элементы Tkinter здесь безопасным образом.
    calculate(obj_list[0], obj_list[1])


def monitor_filesystem(excel_monitor):
    excel_monitor.start()
    try:
        while excel_monitor.observer.is_alive():
            # sleep for a while and then check again
            time.sleep(1)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        excel_monitor.stop()
