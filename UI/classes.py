# from tkinter import *
# from Functions.to_from_json import *
# from Functions import create_box
# import pandas as pd
# from InputData import input_data
# import openpyxl
# import pprint
# from InputData.SourceWater import source_water as sow
# import datetime
# from InputData.Constants import constants
#
#
# class MainFrame:
#     def on_mousewheel(self, event):
#         self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
#
#     @staticmethod
#     def focus_next_widget(event):
#         event.widget.tk_focusNext().focus()
#         return "break"
#
#     @staticmethod
#     def focus_previous_widget(event):
#         event.widget.tk_focusPrev().focus()
#         return "break"
#
#     # def show_graph(value):  # <- Добавить метод show_graph
#     #     # здесь ваш код для отображения графика в зависимости от значения
#     #     print(f'Showing graph for value: {value}')
#
#     def __init__(self, master, anchor,  obj, calc=None,
#                  side='top', text='Главное окно программы'):
#         self.obj = obj['value']
#         self.obj_name = obj['name']
#         self.calc = calc
#         self.main_frame = LabelFrame(master, text=text, width=600, height=150)
#         self.main_frame.pack(side=side, anchor=anchor, expand=True, fill='both')
#         self.main_frame.pack_propagate(0)
#
#         # Create canvas
#         self.canvas = Canvas(self.main_frame)
#         self.canvas.pack(side='left', fill='both', expand=True)
#
#         # Create vertical scrollbar and link it to the canvas
#         self.scrollbar = Scrollbar(self.main_frame, orient='vertical', command=self.canvas.yview)
#         self.scrollbar.pack(side='right', fill='y')
#
#         # Configure the canvas so it will use the scrollbar
#         self.canvas.configure(yscrollcommand=self.scrollbar.set)
#         self.canvas.bind("<MouseWheel>", self.on_mousewheel)  # bind to this specific widget
#
#         self.inner_frame = Frame(self.canvas)
#         self.canvas.create_window((0, 0), window=self.inner_frame, anchor='nw', width=600)
#         self.inner_frame.bind('<Configure>', lambda x: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
#
#         self.names = []
#         self.values = []
#         self.descriptions = []
#         self.labels_list = []
#         self.values_list_old = []
#         self.mod = []
#         self.tmp_names = list(self.obj.keys())
#         for i in range(len(self.tmp_names)):
#
#             if list(self.obj.values())[i]['mod'] != '':
#                 self.names.append(self.tmp_names[i])
#                 self.values.append(list(self.obj.values())[i]['value'])
#                 self.descriptions.append(list(self.obj.values())[i]['description'])
#                 self.mod.append(list(self.obj.values())[i]['mod'])
#
#     def set_new_values(self):
#         if self.calc == 'get':
#             for name in self.names:
#                 new_value = float(getattr(self, f'{name}').get())
#                 if new_value == 0:
#                     self.obj[name]['value'] = 1e-8
#                 else:
#                     self.obj[name]['value'] = new_value
#         # print(self.obj_for_save, self.obj_name)
#
#         to_json([self.obj], self.obj_name)
#
#     # def load(self):
#     #     print('uhei')
#     #     if self.obj_name == 'constants':
#     #         self.obj = constants
#
#     def show_output(self):
#         pass
#
#
# class InputFrame(MainFrame):
#
#     def __init__(self, master, anchor,  obj,  calc, side, text):
#         super().__init__(master, anchor,  obj,  calc, side, text)
#         for i in range(len(self.names)):
#             frame = Frame(self.inner_frame, height=30)
#             frame.pack(anchor='w')
#
#             value = Entry(frame, width=20)
#             value.insert(0, round(float(self.values[i]), 3))
#             value.bind("<Down>", self.focus_next_widget)
#             value.bind("<Up>", self.focus_previous_widget)
#
#             self.labels_list.append(value)
#             description = Label(frame, anchor='w', text=self.descriptions[i])
#             value.pack(side='left')
#             setattr(self, f'{self.names[i]}', value)
#             description.pack(side='left', expand=True)
#
#
# class OutputFrame(MainFrame):
#     def __init__(self, master, anchor,  obj,  calc, side, text):
#         super().__init__(master, anchor,  obj,  calc, side, text)
#         for i in range(len(self.names)):
#             frame = Frame(self.inner_frame, height=30)
#             frame.pack(anchor='w')
#
#             value_old = Label(frame, width=10, text='-')
#             self.values_list_old.append(value_old)
#             value_old.pack(side='left')
#             value = Label(frame, width=10, text=round(float(self.values[i]), 2))
#             setattr(self, f'{self.names[i]}', value)
#             setattr(self, f'{self.names[i]}_old', value_old)
#             # graph_btn = Button(frame, text='Show Graph', command=lambda v=value: self.show_graph(v))  # <- Добавить кнопку
#
#             self.labels_list.append(value)
#             description = Label(frame, anchor='w', text=self.descriptions[i])
#             value.pack(side='left')
#             setattr(self, f'{self.names[i]}', value)
#             # if appointment == 'out':
#             #     graph_btn.pack(side='left')
#             description.pack(side='left', expand=True)
#
#     def set_new_values(self):
#         print('Запуск show_output')
#         new_row = [datetime.datetime.now().date(), datetime.datetime.now().time()]
#         for el, values in self.obj.items():
#             new_row.append(round(values['value'], 2))
#         workbook = openpyxl.load_workbook(config.EXCEL_PATH + '/Out/output.xlsx')
#         sheet = workbook.active
#         last_row = sheet.max_row
#         while (last_row > 0) and all(cell.value is None for cell in sheet[last_row]):
#             last_row -= 1
#
#         # Теперь 'last_row' содержит номер последней непустой строки.
#         # Теперь вставляем данные в следующую строку
#         new_data = ['Значение1', 'Значение2', 'Значение3']  # Замените это вашими данными
#         next_row = last_row + 1
#
#         for col, entry in enumerate(new_row, start=1):
#             sheet.cell(row=next_row, column=col, value=entry)
#         workbook.save(config.EXCEL_PATH + '/Out/output.xlsx')
#
#     def show_output(self):
#         if self.calc == 'set':
#             for i in range(len(self.labels_list)):
#                 self.values_list_old[i]['text'] = self.labels_list[i]['text']
#                 self.labels_list[i]['text'] = round(self.obj[self.names[i]]['value'], 2)
#                 if float(self.labels_list[i]['text']) > float(self.values_list_old[i]['text']):
#                     self.labels_list[i].config(fg='green')
#                 elif float(self.labels_list[i]['text']) < float(self.values_list_old[i]['text']):
#                     self.labels_list[i].config(fg='red')
#                 else:
#                     self.labels_list[i].config(fg='black')
#
#     def change_slider(self, scale):
#         self.obj['bod_full_source']['value'] = float(scale.get())
#
#
# class WorkFrame(MainFrame):
#     def __init__(self, master, anchor,  obj,  calc, side, text, exl_file, time_update=2, rows=10):
#         super().__init__(master, anchor,  obj,  calc, side, text)
#         self.exl_file = exl_file                  # Путь к отслеживаемому exel-файлу
#         self.time_update = time_update            # Время обновления
#         self.rows = rows                          # Количество обновляемых строк (для постройки графика
#         self.changeble_parameters = []            # Изменяемые параметры (Названия столбцов exel-файла)
#         for i in range(len(self.names)):
#             frame = Frame(self.inner_frame, height=30)
#             frame.pack(anchor='w')
#
#             value = Label(frame, width=10, text=round(float(self.values[i]), 2))
#             setattr(self, f'{self.names[i]}', value)
#
#             self.labels_list.append({self.names[i]: value})
#             description = Label(frame, anchor='w', text=self.descriptions[i])
#             value.pack(side='left')
#             setattr(self, f'{self.names[i]}', value)
#             # if appointment == 'out':
#             #     graph_btn.pack(side='left')
#             description.pack(side='left', expand=True)
#         print(self.labels_list)
#
#     def set_new_values(self):
#         row = pd.read_excel(self.exl_file).tail(1)
#         for el in list(row.columns):
#             for i in range(len(self.labels_list)):
#                 if el == list(self.labels_list[i].keys())[0]:
#                     if not row[el].values[-1]:
#                         pass
#                     else:
#                         self.labels_list[i][el]['text'] = float(row[el].values[-1])
#
#                         self.obj[el]['value'] = float(row[el].values[-1])
#         to_json([self.obj], self.obj_name)
#
#
# if __name__ == '__main__':
#     root, inside_left_frame, inside_right_frame = create_box.create_box()
#     fr = WorkFrame(inside_left_frame,
#                    exl_file=config.EXCEL_PATH + 'check.xlsx',
#                    anchor='w',
#                    calc='get',
#                    side='top',
#                    text='Вода, поступающая в аэротенк',
#                    obj=input_data.source_water,
# )
#
#     save_button = Button(root,
#                          text='Сохранить',
#                          command=lambda: fr.set_new_values(),
#
#                          activebackground='gray'
#                          )
#     save_button.pack(side='left', anchor='w')
#
#     root.mainloop()
