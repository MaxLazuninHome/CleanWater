from InputData import input_data
from OutputData import output_data
from UI.classes import InputFrame, OutputFrame, WorkFrame
from Configurations import config


def start_program_setting_mode(inside_left_frame, inside_right_frame):
    source_water = InputFrame(inside_left_frame,
                              anchor='w',
                              side='top',
                              calc='get',
                              text='Вода, поступающая в аэротэнк',
                              obj=input_data.source_water)
    technological_parameters = InputFrame(inside_left_frame,
                                          anchor='w',
                                          side='top',
                                          calc='get',
                                          text='Технологические параметры',
                                          obj=input_data.technological_parameters)
    construction_parameters = InputFrame(inside_left_frame,
                                         anchor='w',
                                         side='top',
                                         calc='get',
                                         text='Конструктивные параметры сооружения',
                                         obj=input_data.construction_parameters)
    consts = InputFrame(inside_left_frame,
                        anchor='w',
                        side='top',
                        text='Кинетические константы',
                        calc='get',
                        obj=input_data.constants)

    output = OutputFrame(inside_right_frame,
                         anchor='n',
                         side='top',
                         calc='set',
                         text='Выходные параметры',
                         obj=output_data.output_data)

    return source_water, technological_parameters, construction_parameters, consts, output


def start_program_work_mode(inside_left_frame, inside_right_frame):

    work_frame = WorkFrame(inside_left_frame,
                           exl_file=config.EXCEL_PATH + '\check.xlsx',
                           anchor='w',
                           calc='get',
                           side='top',
                           text='Вода, поступающая в аэротенк',
                           obj=input_data.source_water,
)

    output = OutputFrame(inside_right_frame,
                         anchor='n',
                         side='top',
                         calc='set',
                         text='Выходные параметры',
                         obj=output_data.output_data)

    return work_frame, output
