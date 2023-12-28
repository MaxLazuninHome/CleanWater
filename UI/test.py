import tkinter as tk
from tkinter import simpledialog

import tkinter as tk
from tkinter import filedialog

def select_folder():
    # Функция вызывается при нажатии на кнопку
    directory = filedialog.askdirectory()  # Открытие диалога для выбора папки
    if directory:  # Проверка, что пользователь выбрал папку
        print(f"Выбранная папка: {directory}")
        # Здесь вы можете делать что угодно с выбранным путём, например сохранять в переменную
    else:
        print("Папка не была выбрана.")

# Создаем окно приложения
root = tk.Tk()
root.title("Выбор папки")

# Создаем кнопку, которая будет вызывать функцию select_folder
button_select_folder = tk.Button(root, text="Выбрать папку", command=select_folder)
button_select_folder.pack(pady=20, padx=20)  # Размещаем кнопку в окне

root.mainloop()  # Запускаем основной цикл обработки событий