from tkinter import *
from Functions.to_from_json import *


class OutputFrame:

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

    def __init__(self, master, appointment, anchor, obj, obj_name, label_heigh=150, calc=None,
                 side='top', text='Главное окно программы'):
        self.obj = obj['value']
        self.obj_name = obj['name']
        self.calc = calc
        self.main_frame = LabelFrame(master, text=text, width=600, height=label_heigh)
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

        self.names = []
        self.values = []
        self.descriptions = []
        self.labels_list = []
        self.values_list_old = []
        self.mod = []
        self.tmp_names = list(self.obj.keys())
        for i in range(len(self.tmp_names)):

            if list(self.obj.values())[i]['mod'] != '':
                self.names.append(self.tmp_names[i])
                self.values.append(list(self.obj.values())[i]['value'])
                self.descriptions.append(list(self.obj.values())[i]['description'])
                self.mod.append(list(self.obj.values())[i]['mod'])
        for i in range(len(self.names)):
            frame = Frame(self.inner_frame, height=30)
            frame.pack(anchor='w')
            value = None

            if appointment == 'in':
                value = Entry(frame, width=20)
                value.insert(0, round(float(self.values[i]), 3))
                value.bind("<Down>", self.focus_next_widget)
                value.bind("<Up>", self.focus_previous_widget)

            elif appointment == 'out':
                value_old = Label(frame, width=10, text='-')
                self.values_list_old.append(value_old)
                value_old.pack(side='left')
                value = Label(frame, width=10, text=round(float(self.values[i]), 2))
                setattr(self, f'entry_{self.names[i]}', value)
                setattr(self, f'entry_{self.names[i]}_old', value_old)
                # graph_btn = Button(frame, text='Show Graph', command=lambda v=value: self.show_graph(v))  # <- Добавить кнопку

            self.labels_list.append(value)
            description = Label(frame, anchor='w', text=self.descriptions[i])
            value.pack(side='left')
            setattr(self, f'entry_{self.names[i]}', value)
            # if appointment == 'out':
            #     graph_btn.pack(side='left')
            description.pack(side='left', expand=True)

    def calculate(self):
        if self.calc == 'get':
            for name in self.names:
                new_value = float(getattr(self, f'entry_{name}').get())
                if new_value == 0:
                    self.obj[name]['value'] = 1e-8
                else:
                    self.obj[name]['value'] = new_value

        to_json([self.obj], self.obj_name)

    def show_output(self):
        if self.calc == 'set':
            for i in range(len(self.labels_list)):
                self.values_list_old[i]['text'] = self.labels_list[i]['text']
                self.labels_list[i]['text'] = round(self.obj[self.names[i]]['value'], 2)
                if float(self.labels_list[i]['text']) > float(self.values_list_old[i]['text']):
                    self.labels_list[i].config(fg='green')
                elif float(self.labels_list[i]['text']) < float(self.values_list_old[i]['text']):
                    self.labels_list[i].config(fg='red')
                else:
                    self.labels_list[i].config(fg='black')

    def change_slider(self, scale):
        self.obj['bod_full_source']['value'] = float(scale.get())


# if __name__ == '__main__':
#
#     first_run()
#     functions.calculate_zones()
#     root = Tk()
#     root.title('Главное окно')
#     root.update_idletasks()
#     s = root.geometry()
#     s = s.split('+')
#     s = s[0].split('x')
#     width_root = int(s[0])
#     height_root = int(s[1])
#
#     w = root.winfo_screenwidth()
#     h = root.winfo_screenheight()
#     w = w // 2
#     h = h // 2
#     w = w - width_root // 2
#     h = h - height_root // 2
#     root.geometry('1550x750+200+100'.format(w, h))
#     inside_left_frame = Frame()
#     inside_right_frame = Frame()
#     inside_left_frame.pack(side='left', anchor='n', padx=20, fill='both', expand=True)
#     inside_right_frame.pack(side='left', anchor='n', fill='both', expand=True)
#     source_water = OutputFrame(inside_left_frame,
#                                anchor='w',
#                                calc='get',
#                                side='top',
#                                text='Вода, поступающая в аэротэнк',
#                                appointment='in',
#                                obj=input_data.source_water,
#                                obj_name='source_water')
#     technological_parameters = OutputFrame(inside_left_frame,
#                                            anchor='w',
#                                            calc='get',
#                                            side='top',
#                                            text='Технологические параметры',
#                                            appointment='in',
#                                            obj=input_data.technological_parameters,
#                                            obj_name='technological_parameters')
#     construction_parameters = OutputFrame(inside_left_frame,
#                                           anchor='w',
#                                           calc='get',
#                                           side='top',
#                                           text='Конструктивные параметры сооружения',
#                                           appointment='in',
#                                           obj=input_data.construction_parameters,
#                                           obj_name='construction_parameters')
#     consts = OutputFrame(inside_left_frame,
#                          anchor='w',
#                          calc='get',
#                          side='top',
#                          text='Кинетические константы',
#                          appointment='in',
#                          obj=input_data.constants,
#                          obj_name='constants')
#
#     output = OutputFrame(inside_right_frame,
#                          anchor='n',
#                          calc='set',
#                          side='top',
#                          text='Выходные параметры',
#                          appointment='out',
#                          label_heigh=400,
#                          obj=output_data.output_data,
#                          obj_name='output')
#
#     # output = OutputFrame(inside_right_frame,
#     #                      anchor='n',
#     #                      calc='set',
#     #                      side='top',
#     #                      text='Выходные параметры',
#     #                      appointment='out',
#     #                      label_heigh=400,
#     #                      obj=output_data.output_results,
#     #                      obj_name='output')
#     #
#     # pwqr = OutputFrame(inside_right_frame,
#     #                    anchor='n',
#     #                    calc='set',
#     #                    side='top',
#     #                    text='Качество очищенной воды',
#     #                    appointment='out',
#     #                    label_heigh=100,
#     #                    obj=output_data.purified_water_quality_results,
#     #                    obj_name='output')
#
#     button = Button(inside_right_frame,
#                     text='Расчитать',
#                     command=lambda: functions.calculate(source_water, consts,
#                                                         construction_parameters,
#                                                         technological_parameters,
#                                                         output),
#                     activebackground='gray'
#                     )
#     button.pack(side='top', anchor='w')
#
#
#     root.mainloop()






