from tkinter import *

from InputData import input_data
from OutputData import output_data
from Functions import functions
from Functions.set_values import first_run
from UI.classes import OutputFrame, InputFrame

first_run()
functions.calculate_zones()
root = Tk()
root.title('Главное окно')
root.update_idletasks()
s = root.geometry()
s = s.split('+')
s = s[0].split('x')
width_root = int(s[0])
height_root = int(s[1])

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

button = Button(inside_right_frame,
                text='Расчитать',
                command=lambda: functions.calculate(source_water, consts,
                                                    construction_parameters,
                                                    technological_parameters,
                                                    output),
                activebackground='gray'
                )
button.pack(side='top', anchor='w')


root.mainloop()
