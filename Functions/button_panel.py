from tkinter import *
from Functions import functions


def create_button_panel(inside_right_frame, source_water, consts, construction_parameters,
                        technological_parameters, output, mode='work'):
    buttons_frame = Frame(inside_right_frame)
    buttons_frame.pack(anchor='w')
    # mode_button = Button(buttons_frame,
    #                      text='Сменить режим',
    #
    #                      command=sys.exit,
    #                      activebackground='gray'
    #                      )
    # mode_button.pack(side='left', anchor='w')
    calculate_button = Button(buttons_frame,
                              text='Расчитать',
                              command=lambda: functions.calculate(source_water, consts,
                                                                  construction_parameters,
                                                                  technological_parameters,
                                                                  output),
                              activebackground='gray'
                              )
    calculate_button.pack(side='left', anchor='w')

    save_button = Button(buttons_frame,
                         text='Сохранить',
                         command=lambda: functions.save_aerotank(source_water, consts,
                                                                 construction_parameters,
                                                                 technological_parameters
                                                                 ),
                         activebackground='gray'
                         )
    save_button.pack(side='left', anchor='w')

    load_button = Button(buttons_frame,
                         text='Загрузить',
                         command='',
                         activebackground='gray'
                         )
    load_button.pack(side='left', anchor='w')

    close_button = Button(buttons_frame,
                          text='Закрыть',
                          command=sys.exit,
                          activebackground='gray'
                          )
    close_button.pack(side='left', anchor='w')

    return calculate_button, save_button, load_button, close_button
