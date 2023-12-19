# import pandas as pd
#
# data = pd.read_excel('D:\Max\CleanWaterMain\Обратный_расчет_2023.09.08.xlsx',
#                      skiprows=0,
#                      usecols='A:E')
#
# print(data.iloc[170:179, 3])

import tkinter as tk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime


def create_new_window():
    new_window = tk.Toplevel(root)
    fig = plt.Figure(figsize=(7, 7), dpi=100)
    plot1 = fig.add_subplot(111)

    # Генерируем данные

    dates = [i for i in range(100)]
    print(dates)
    values = [random.randint(20, 25) for _ in range(100)]

    plot1.plot_date(dates, values, linestyle='solid')

    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas.draw()
    canvas.get_tk_widget().pack()


root = tk.Tk()

button = tk.Button(root, text="Create new window", command=create_new_window)
button.pack()

root.mainloop()