from Functions import functions, graph
from Functions.set_values import first_run
from Functions.start_program import *
from Functions.button_panel import create_setting_button_panel, create_work_button_panel
from Functions.create_box import create_box
from excels.Monitor import excel_monitor
import threading
import time


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


mode = 'work'
# mode = 'setting'

if mode == 'setting':    # Для отладочного режима работы
    first_run()          # Загрузка значений из JSON-файлов
    functions.calculate_zones()        # Первый расчёт для вывода основного окна

    root, inside_left_frame, inside_right_frame = create_box()     # Создаём основное окно программы и внутренние рамки

    source_water, technological_parameters, construction_parameters, consts, output = \
        start_program_setting_mode(inside_left_frame, inside_right_frame)    # Создаём рамки под параметры

    calculate_button, graph_button = create_setting_button_panel(inside_right_frame,   # Создаём панель кнопок
                                                                 source_water,
                                                                 technological_parameters,
                                                                 construction_parameters, consts, output)
    graph_button['command'] = lambda: graph.choose_columns_and_plot(root)
    # load_button['command'] = lambda: functions.load_aerotank(root)

    root.mainloop()

elif mode == 'work':    # Для рабочего режима

    excel_monitoring_thread = threading.Thread(target=monitor_filesystem,    # Создаём поток
                                               daemon=True)                  # для мониторщика событий ФС

    first_run()     # Загрузка значений из JSON-файлов
    functions.calculate_zones()    # Первый расчёт для вывода основного окна
    root, inside_left_frame, inside_right_frame = create_box()   # Создаём основное окно программы и внутренние рамки

    source_water, technological_parameters, output = start_program_work_mode(inside_left_frame, inside_right_frame)   # Создаём рамки под параметры

    excel_monitor = excel_monitor.ExcelMonitor(obj_list=[source_water, technological_parameters, output],   # Создаем мониторщиека событий ФС
                                               root=root, )

    graph_button = create_work_button_panel(inside_right_frame)     # СОздаём панель кнопок
    graph_button['command'] = lambda: graph.choose_columns_and_plot(root)

    # load_button['command'] = lambda: functions.load_aerotank(root)

    excel_monitoring_thread.start()    # Активация поток мониторщика событий
    root.mainloop()

