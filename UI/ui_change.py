from tkinter import *
from Functions.to_from_json import *
from Functions import create_box
from Functions.set_values import first_run
from copy import deepcopy
import pandas as pd
from InputData import input_data
from OutputData import output_data
import time
from InputData.Constants import constants
import pprint
from InputData.SourceWater import source_water as sow


class MainFrame:
    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    @staticmethod
    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"

    @staticmethod
    def focus_previous_widget(event):
        event.widget.tk_focusPrev().focus()
        return "break"

    # def show_graph(value):  # <- Добавить метод show_graph
    #     # здесь ваш код для отображения графика в зависимости от значения
    #     print(f'Showing graph for value: {value}')

    def __init__(self, master, anchor, obj, side='top', text='Главное окно программы'):
        self.obj = deepcopy(obj['value'])
        self.obj_for_save = obj['value']
        self.obj_name = obj['name']
        self.main_frame = LabelFrame(master, text=text, width=600, height=150)
        self.main_frame.pack(side=side, anchor=anchor, expand=True, fill='both')
        self.main_frame.pack_propagate(0)

        # Create canvas
        self.canvas = Canvas(self.main_frame)
        self.canvas.pack(side='left', fill='both', expand=True)

        # Create vertical scrollbar and link it to the canvas
        self.scrollbar = Scrollbar(self.main_frame, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')

        # Configure the canvas so it will use the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)  # bind to this specific widget

        self.inner_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor='nw', width=600)
        self.inner_frame.bind('<Configure>', lambda x: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

    # def load(self):
    #     print('uhei')
    #     if self.obj_name == 'constants':
    #         self.obj = constants

    def show_output(self):
        pass

    def set_new_values(self):
        pass


class InputFrame(MainFrame):

    def __init__(self, master, anchor, obj, side, text):
        super().__init__(master, anchor, obj, side, text)

        for el, params in self.obj.items():
            if params['mod']:
                frame = Frame(self.inner_frame, height=30)
                frame.pack(anchor='w')

                value = Entry(frame, width=20)
                value.insert(0, round(float(params['value']), 3))
                value.bind("<Down>", self.focus_next_widget)
                value.bind("<Up>", self.focus_previous_widget)
                value.pack(side='left')
                params['ui_element'] = value
                description = Label(frame, anchor='w', text=params['description'])
                description.pack(side='left', expand=True)

    def set_new_values(self):
        print('set_new_values  в ', self.obj_name)
        for el, params in self.obj.items():
            if params['mod']:
                new_value = float(params['ui_element'].get())
                if new_value == 0:
                    params['value'] = 1e-8
                    self.obj_for_save[el]['value'] = 1e-8
                else:
                    params['value'] = new_value
                    self.obj_for_save[el]['value'] = new_value
        to_json([self.obj_for_save], self.obj_name)


class OutputFrame(MainFrame):
    def __init__(self, master, anchor, obj, side, text):
        super().__init__(master, anchor, obj, side, text)
        self.values_list_old = []
        for el, params in self.obj.items():
            if params['mod']:
                frame = Frame(self.inner_frame, height=30)
                frame.pack(anchor='w')

                value_old = Label(frame, width=10, text='-')
                value_old.pack(side='left')

                value = Label(frame, width=10, text=round(float(params['value']), 2))
                value.pack(side='left')

                params['ui_element'] = value
                params['ui_element_old'] = value_old

                # graph_btn = Button(frame, text='Show Graph', command=lambda v=value: self.show_graph(v))  # <- Добавить кнопку

                description = Label(frame, anchor='w', text=params['description'])

                #     graph_btn.pack(side='left')
                description.pack(side='left', expand=True)

    def show_output(self):
        for el, params in self.obj.items():
            params['value_old'] = float(params['ui_element']['text'])
            params['ui_element_old']['text'] = params['ui_element']['text']
            params['ui_element']['text'] = round(params['value'], 2)

            if round(params['value'], 2) > round(params['value_old'], 2):
                params['ui_element'].config(fg='green')
            elif round(params['value'], 2) < round(params['value_old'], 2):
                params['ui_element'].config(fg='red')
            else:
                params['ui_element'].config(fg='black')


    # def change_slider(self, scale):
    #     self.obj['bod_full_source']['value'] = float(scale.get())


# class WorkFrame(MainFrame):
#     def __init__(self, master, anchor, obj, calc, side, text, exl_file, time_update=2, rows=10):
#         super().__init__(master, anchor, obj, calc, side, text)
#         self.exl_file = exl_file  # Путь к отслеживаемому exel-файлу
#         self.time_update = time_update  # Время обновления
#         self.rows = rows  # Количество обновляемых строк (для постройки графика
#         self.changeble_parameters = []  # Изменяемые параметры (Названия столбцов exel-файла)
#         for i in range(len(self.names)):
#             frame = Frame(self.inner_frame, height=30)
#             frame.pack(anchor='w')
#
#             value = Label(frame, width=10, text=round(float(self.values[i]), 2))
#             setattr(self, f'label_{self.names[i]}', value)
#             # graph_btn = Button(frame, text='Show Graph', command=lambda v=value: self.show_graph(v))  # <- Добавить кнопку
#
#             self.labels_list.append(value)
#             description = Label(frame, anchor='w', text=self.descriptions[i])
#             value.pack(side='left')
#             setattr(self, f'label_{self.names[i]}', value)
#             # if appointment == 'out':
#             #     graph_btn.pack(side='left')
#             description.pack(side='left', expand=True)
#
#     def set_new_values(self):
#         tmp_df = pd.read_excel(self.exl_file)
#         self.changeble_parameters = tmp_df.keys()
#         for i in range(self.rows):
#             for name in self.changeble_parameters:
#                 print(self.labels_list[i], self.obj[self.names[i]]['value'])
#                 setattr(self, f'label_{name}', tmp_df[name][i])
#
#             time.sleep(2)#

#
if __name__ == '__main__':
    first_run()
    root, inside_left_frame, inside_right_frame = create_box.create_box()
    fr = OutputFrame(inside_left_frame,
                    anchor='w',
                    side='top',
                    text='Вода, поступающая в аэротенк',
                    obj=output_data.output_data,
)

    save_button = Button(root,
                         text='Сохранить',
                         command=lambda: fr.check(),

                         activebackground='gray'
                         )
    save_button.pack(side='left', anchor='w')
    root.mainloop()
