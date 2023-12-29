from InputData import input_data
from OutputData import output_data
from UI.classes import InputFrame, OutputFrame


def start_program(inside_left_frame, inside_right_frame):
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

    return source_water, technological_parameters, construction_parameters, consts, output
