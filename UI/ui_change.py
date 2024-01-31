from tkinter import *
from Functions.to_from_json import *
from Functions import create_box
from Functions.set_values import first_run
from Functions.functions import calculate
from copy import deepcopy
from InputData import input_data
from OutputData import output_data
from UI.entry_with_help import ToolTip
import pandas as pd
from tkinter import simpledialog


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

    def show_output(self):
        pass

    def set_new_values(self):
        pass

    def check_value(self, value, min_value, max_value):

        if value > max_value or value < min_value:
            correct_value = None
            # В цикле просим пользователя ввести корректное значение
            while correct_value is None:
                # Открываем окно с просьбой ввести корректное значение
                user_input = simpledialog.askstring(
                    title="Wrong value",
                    prompt=f"Enter a value between {min_value} and {max_value}:"
                )

                # Проверяем, что пользователь ввел число
                if user_input is not None:
                    try:
                        correct_value = float(user_input)
                    except ValueError:
                        continue  # Не удалось преобразовать введенный текст в число

                    # Проверяем, что значение входит в указанный диапазон
                    if min_value <= correct_value <= max_value:
                        return correct_value
                    else:
                        correct_value = None  # Если значение не подходит, продолжаем цикл
        else:
            return value


class InputFrame(MainFrame):
    @staticmethod
    def create_entry_with_tooltip(parent, obj):
        entry = Entry(parent, width=20)
        entry.insert(0, round(float(obj['value']), 3), )
        entry.pack()
        ToolTip(entry, obj)
        return entry

    def __init__(self, master, anchor, obj, side, text, check_value=True):
        super().__init__(master, anchor, obj, side, text)
        self.check = check_value

        for el, params in self.obj.items():
            if params['mod']:
                frame = Frame(self.inner_frame, height=30)
                frame.pack(anchor='w')

                value = self.create_entry_with_tooltip(parent=frame,
                                                       obj=params,
                                                       )

                value.bind("<Down>", self.focus_next_widget)
                value.bind("<Up>", self.focus_previous_widget)
                value.pack(side='left')

                params['ui_element'] = value

                description = Label(frame, anchor='w', text=params['description'])
                description.pack(side='left', expand=True)

    def set_new_values(self):
        for el, params in self.obj.items():
            if params['mod']:
                new_value = float(params['ui_element'].get())
                if self.check:
                    correct_value = self.check_value(value=new_value,
                                                     min_value=params['min_value'],
                                                     max_value=params['max_value'])
                    params['ui_element'].delete(0, END)
                    params['ui_element'].insert(0, round(correct_value, 2))
                else:
                    correct_value = new_value

                if correct_value == 0:
                    params['value'] = 1e-8
                    self.obj_for_save[el]['value'] = 1e-8
                else:
                    params['value'] = correct_value
                    self.obj_for_save[el]['value'] = correct_value

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

                description = Label(frame, anchor='w', text=params['description'])
                description.pack(side='left', expand=True)

    def show_output(self):

        for el, params in self.obj.items():
            params['value_old'] = float(params['ui_element']['text'])
            params['ui_element_old']['text'] = params['ui_element']['text']
            params['ui_element']['text'] = round(self.obj_for_save[el]['value'], 2)

            if round(self.obj_for_save[el]['value'], 2) > round(params['value_old'], 2):
                params['ui_element'].config(fg='green')
            elif round(self.obj_for_save[el]['value'], 2) < round(params['value_old'], 2):
                params['ui_element'].config(fg='red')
            else:
                params['ui_element'].config(fg='black')

    # def change_slider(self, scale):
    #     self.obj['bod_full_source']['value'] = float(scale.get())


class WorkFrame(MainFrame):
    def __init__(self, master, anchor,  obj, side, text, exl_file):
        super().__init__(master, anchor,  obj, side, text)
        self.exl_file = exl_file                  # Путь к отслеживаемому exel-файлу
        self.labels_list = []
        for el, params in self.obj.items():
            if params['mod']:
                frame = Frame(self.inner_frame, height=30)
                frame.pack(anchor='w')

                value = Label(frame, width=10, text=round(float(params['value']), 2))
                value.pack(side='left')

                params['ui_element'] = value

                description = Label(frame, anchor='w', text=params['description'])
                description.pack(side='left', expand=True)

    def set_new_values(self):
        row = pd.read_excel(self.exl_file).tail(1)
        for el, params in self.obj.items():
            if params['mod']:
                index = row.last_valid_index()          # Получаем индекс последней используемой строки
                new_value = float(row.loc[index, el])   # Забираем значение из ячейки
                if new_value == 0:                      # Если нулевое
                    params['value'] = 1e-8              # Присваиваем маленькое ненулевое значение
                    self.obj_for_save[el]['value'] = 1e-8    # Для избежания ошибки деления на ноль
                    params['ui_element']['text'] = 0
                else:
                    params['value'] = new_value
                    self.obj_for_save[el]['value'] = new_value
                    params['ui_element']['text'] = new_value
        to_json([self.obj_for_save], self.obj_name)


if __name__ == '__main__':
    first_run()
    root, inside_left_frame, inside_right_frame = create_box.create_box()
    fri = WorkFrame(inside_left_frame,
                    exl_file=config.INPUT_DATA,
                    anchor='w',
                    side='top',
                    text='Вода, поступающая в аэротенк',
                    obj=input_data.source_water,
                    )
    fro = OutputFrame(inside_left_frame,
                    anchor='w',
                    side='top',
                    text='Вода, поступающая в аэротенк',
                    obj=output_data.output_data,
)

    save_button = Button(root,
                         text='Сохранить',
                         command=lambda: calculate(fri, fro),

                         activebackground='gray'
                         )
    save_button.pack(side='left', anchor='w')
    root.mainloop()
