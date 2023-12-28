from tkinter import *

from InputData import input_data
from OutputData import output_data
from Functions import functions
from Functions.set_values import first_run
from UI.classes import OutputFrame
import sys


def start_program(inside_left_frame, inside_right_frame):
    source_water = OutputFrame(inside_left_frame,
                               anchor='w',
                               calc='get',
                               side='top',
                               text='Вода, поступающая в аэротэнк',
                               appointment='in',
                               obj=input_data.source_water,
                               obj_name='source_water')
    technological_parameters = OutputFrame(inside_left_frame,
                                           anchor='w',
                                           calc='get',
                                           side='top',
                                           text='Технологические параметры',
                                           appointment='in',
                                           obj=input_data.technological_parameters,
                                           obj_name='technological_parameters')
    construction_parameters = OutputFrame(inside_left_frame,
                                          anchor='w',
                                          calc='get',
                                          side='top',
                                          text='Конструктивные параметры сооружения',
                                          appointment='in',
                                          obj=input_data.construction_parameters,
                                          obj_name='construction_parameters')
    consts = OutputFrame(inside_left_frame,
                         anchor='w',
                         calc='get',
                         side='top',
                         text='Кинетические константы',
                         appointment='in',
                         obj=input_data.constants,
                         obj_name='constants')

    output = OutputFrame(inside_right_frame,
                         anchor='n',
                         calc='set',
                         side='top',
                         text='Выходные параметры',
                         appointment='out',
                         label_heigh=400,
                         obj=output_data.output_data,
                         obj_name='output')

    return source_water, technological_parameters, construction_parameters, consts, output
