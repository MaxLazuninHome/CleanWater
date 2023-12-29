from Functions import functions
from Functions.set_values import first_run
<<<<<<< HEAD
from UI.classes import OutputFrame, InputFrame
=======
from Functions.start_program import start_program
from Functions.button_panel import create_button_panel
from Functions.create_box import create_box
import sys
>>>>>>> ui_modifications

while True:

<<<<<<< HEAD
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w = w - width_root // 2
h = h - height_root // 2
root.geometry('1550x750+200+100'.format(w, h))
inside_left_frame = Frame()
inside_right_frame = Frame()
inside_left_frame.pack(side='left', anchor='n', padx=20, fill='both', expand=True)
inside_right_frame.pack(side='left', anchor='n', fill='both', expand=True)
source_water = InputFrame(inside_left_frame,
                          anchor='w',
                          calc='get',
                          side='top',
                          text='Вода, поступающая в аэротэнк',
                          obj=input_data.source_water)
technological_parameters = InputFrame(inside_left_frame,
                                      anchor='w',
                                      calc='get',
                                      side='top',
                                      text='Технологические параметры',
                                      obj=input_data.technological_parameters)
construction_parameters = InputFrame(inside_left_frame,
                                     anchor='w',
                                     calc='get',
                                     side='top',
                                     text='Конструктивные параметры сооружения',
                                     obj=input_data.construction_parameters)
consts = InputFrame(inside_left_frame,
                    anchor='w',
                    calc='get',
                    side='top',
                    text='Кинетические константы',
                    obj=input_data.constants)

output = OutputFrame(inside_right_frame,
                     anchor='n',
                     calc='set',
                     side='top',
                     text='Выходные параметры',
                     obj=output_data.output_data)
=======
    first_run()
    functions.calculate_zones()
    root, inside_left_frame, inside_right_frame = create_box()

    source_water, technological_parameters, construction_parameters, consts, output = \
        start_program(inside_left_frame, inside_right_frame)
>>>>>>> ui_modifications

    calculate_button, save_button, load_button, close_button = \
        create_button_panel(inside_right_frame, source_water, technological_parameters,
                            construction_parameters, consts, output)

    load_button['command'] = lambda: functions.load_aerotank(root)
    # consts.load()

    root.mainloop()
