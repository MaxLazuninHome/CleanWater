import pandas as pd
from Configurations.config import EXCEL_PATH,INPUT_DATA, OUTPUT_DATA
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def join_excel_sheets(rows=10):

    df1 = pd.read_excel(OUTPUT_DATA)   # Загружаем данные из файлов
    df2 = pd.read_excel(INPUT_DATA)

    rows_to_take = min(len(df1), len(df2), rows)   # Определяем количество строк, которое нужно взять из каждой таблицы

    df1_subset = df1.tail(rows_to_take)    # Получаем заданное количество последних строк из каждой таблицы
    df2_subset = df2.tail(rows_to_take)

    joined_df = pd.concat([df1_subset.reset_index(drop=True),   # Объединяем таблицы (колонки df2 добавляются к df1)
                           df2_subset.reset_index(drop=True)],
                          axis=1)

    return joined_df    # Возвращаем результат


def choose_columns_and_plot(root, num_points=10):

    df = join_excel_sheets()

    # Объединение даты и времени в одну колонку если это требуется
    df['DateTime'] = pd.to_datetime(df[df.columns[0]].astype(str) + ' ' + df[df.columns[1]].astype(str))

    df = df.iloc[-num_points:]  # Взятие последних num_points записей

    graph_window = tk.Toplevel(root)      # Создание главного окна
    graph_window.geometry('300x600+100+100')      # Задаём размеры главного окна
    graph_window.title("Выберите столбцы для построения графика")

    frame_for_checkboxes = tk.Frame(graph_window)    # Создание поля под чекбоксы
    frame_for_checkboxes.pack()

    left_frame = tk.LabelFrame(frame_for_checkboxes,    # Создание левого столбика с чекбоксами
                               text='Выходящая вода',
                               width=150,
                               height=600)
    left_frame.pack(side='left', anchor='n')

    right_frame = tk.LabelFrame(frame_for_checkboxes,    # Создание правого столбика с чекбоксами
                                text='Входящая вода',
                                width=150, height=600)
    right_frame.pack(side='left', anchor='n')

    checkboxes_vars = {}    # Список для хранения переменных состояний чекбоксов

    # Создаем чекбоксы для каждого столбца, начиная с третьего (первые две колонки - дата и время)
    for col in df.columns[2:23]:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(left_frame, text=col, variable=var)
        cb.pack(side='top', anchor='w')
        checkboxes_vars[col] = var

    for col in df.columns[23:-2]:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(right_frame, text=col, variable=var)
        cb.pack(side='top', anchor='w')
        checkboxes_vars[col] = var

    def on_button_click():

        window_title = "Графики"    # Заглавие второго окна

        plot_window = tk.Toplevel(graph_window)     # Создание второго окна для графиков
        plot_window.title(window_title)     # Подпись графика

        fig, ax = plt.subplots()      # Создание фигуры для графика

        x_indexes = range(len(df['DateTime']))     # Индексы для оси X

        for col, var in checkboxes_vars.items():     # Построение графиков для выбранных столбцов
            if var.get():
                ax.plot(x_indexes, df[col], label=col)

        ax.set_xticks(x_indexes)     # Установка меток даты и времени на оси X
        ax.set_xticklabels(df['DateTime'].dt.strftime('%Y-%m-%d %H:%M'), rotation=45, ha="right")

        ax.legend()
        ax.set_xlabel('Время')
        ax.set_ylabel('Значения')
        ax.grid()

        canvas = FigureCanvasTkAgg(fig, master=plot_window)      # Встраиваем график в tkinter окно
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        graph_window.withdraw()      # Обновление и закрытие первоначального окна

    plot_button = tk.Button(graph_window, text="Построить график", command=on_button_click)    # Кнопка для построения графика
    plot_button.pack(side='bottom', anchor='center')

    # graph_window.mainloop()


if __name__ == '__main__':

    choose_columns_and_plot()
