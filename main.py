from Functions import functions
from Functions.set_values import first_run
from Functions.start_program import start_program
from Functions.button_panel import create_button_panel
from Functions.create_box import create_box
import sys

while True:

    first_run()
    functions.calculate_zones()
    root, inside_left_frame, inside_right_frame = create_box()

    source_water, technological_parameters, construction_parameters, consts, output = \
        start_program(inside_left_frame, inside_right_frame)

    calculate_button, save_button, load_button, close_button = \
        create_button_panel(inside_right_frame, source_water, technological_parameters,
                            construction_parameters, consts, output)

    load_button['command'] = lambda: functions.load_aerotank(root)
    # consts.load()

    root.mainloop()
