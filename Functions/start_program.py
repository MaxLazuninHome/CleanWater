from InputData import input_data
from OutputData import output_data
from UI.ui_change import InputFrame, OutputFrame, WorkFrame
from Configurations import config


def start_program_setting_mode(inside_left_frame, inside_right_frame):
    source_water = InputFrame(inside_left_frame,
                              anchor='w',
                              side='top',
                              text='Вода, поступающая в аэротэнк',
                              obj=input_data.source_water)
    technological_parameters = InputFrame(inside_left_frame,
                                          anchor='w',
                                          side='top',
                                          text='Технологические параметры',
                                          obj=input_data.technological_parameters)
    construction_parameters = InputFrame(inside_left_frame,
                                         anchor='w',
                                         side='top',
                                         text='Конструктивные параметры сооружения',
                                         obj=input_data.construction_parameters)
    consts = InputFrame(inside_left_frame,
                        anchor='w',
                        side='top',
                        text='Кинетические константы',
                        check_value= False,
                        obj=input_data.constants)

    output = OutputFrame(inside_right_frame,
                         anchor='n',
                         side='top',
                         text='Выходные параметры',
                         obj=output_data.output_data)

    return source_water, technological_parameters, construction_parameters, consts, output


def start_program_work_mode(inside_left_frame, inside_right_frame):

    source_water = WorkFrame(inside_left_frame,
                             exl_file=config.INPUT_DATA,
                             anchor='w',
                             side='top',
                             text='Вода, поступающая в аэротенк',
                             obj=input_data.source_water)

    technological_parameters = WorkFrame(inside_left_frame,
                                         exl_file=config.INPUT_DATA,
                                         anchor='w',
                                         side='top',
                                         text='Технологические параметры',
                                         obj=input_data.technological_parameters)

    output = OutputFrame(inside_right_frame,
                         anchor='n',
                         side='top',
                         text='Выходные параметры',
                         obj=output_data.output_data)

    return source_water, technological_parameters, output
