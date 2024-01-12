from Functions import functions
from Functions.set_values import first_run
from Functions.start_program import *
from Functions.button_panel import create_button_panel
from Functions.create_box import create_box
from excels.Monitor import excel_monitor
from excels.Monitor import functions as f
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

while True:
    if mode == 'setting':


        first_run()
        functions.calculate_zones()
        root, inside_left_frame, inside_right_frame = create_box()

        source_water, technological_parameters, construction_parameters, consts, output = \
            start_program_setting_mode(inside_left_frame, inside_right_frame)

        calculate_button, save_button, load_button, close_button = \
            create_button_panel(inside_right_frame, source_water, technological_parameters,
                                construction_parameters, consts, output)

        load_button['command'] = lambda: functions.load_aerotank(root)

        root.mainloop()

    elif mode == 'work':

        excel_monitoring_thread = threading.Thread(target=monitor_filesystem, daemon=True)

        first_run()
        functions.calculate_zones()
        root, inside_left_frame, inside_right_frame = create_box()

        work_frame, output = \
            start_program_work_mode(inside_left_frame, inside_right_frame)
        excel_monitor = excel_monitor.ExcelMonitor(obj_list=[work_frame, output], root=root, )
        # calculate_button, save_button, load_button, close_button = \
        #     create_button_panel(inside_right_frame, source_water, technological_parameters,
        #                         construction_parameters, consts, output)

        # load_button['command'] = lambda: functions.load_aerotank(root)

        excel_monitoring_thread.start()
        root.mainloop()

