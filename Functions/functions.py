import calculating_order
from tkinter import simpledialog, filedialog
from Functions.abbreviation import load_input_data
from Functions.to_from_json import *
from Functions.set_values import first_run
from Configurations import config
import numpy as np
import pandas as pd
import os
import shutil
import sys


c, sw, tp, cp = load_input_data()


def calculate_source_water():
    sw['n_ammonium_in']['value'] = sw['ammonium_ion']['value'] * c['s_metr_ammonium_ion_n']['value']
    sw['n_nitrites_in']['value'] = sw['nitrite_ion']['value'] * c['s_metr_nitrite_ion_n']['value']
    sw['n_nitrates_in']['value'] = sw['nitrate_ion']['value'] * c['s_metr_nitrate_ion_n']['value']


def calculate_zones():
    calculating_order.complete_calculate()


def calculate(*args):

    for arg in args:
        arg.set_new_values()
    calculate_zones()
    for arg in args:
        arg.show_output()


def change_mode(mode):
    mode = 'setting' if mode == 'work' else 'work'
    return mode


# def save_aerotank(*args):
#     user_input = simpledialog.askstring("Ввод", "Введите название:")
#     if user_input:
#         user_text = user_input
#         save_path = f'{user_text}/'
#         try:
#             # os.mkdir(save_path)
#             os.mkdir(config.JSON_PATH + save_path)
#         except FileExistsError:
#             pass
#         for arg in args:
#             # arg.set_new_values()
#
#             to_json([arg.obj], arg.obj_name, path=save_path, mode='s')


# def load_aerotank(root):
#
#     # Функция вызывается при нажатии на кнопку
#     directory = filedialog.askdirectory()  # Открытие диалога для выбора папки
#     if directory:  # Проверка, что пользователь выбрал папку
#         print(f"Выбранная папка: {directory}")
#         # Здесь вы можете делать что угодно с выбранным путём, например сохранять в переменную
#     else:
#        directory =  config.JSON_PATH + 'CurrentJsons'
#
#     folder_from = directory
#     folder_to = config.JSON_PATH + 'CurrentJsons'
#
#     for f in os.listdir(folder_from):
#         # print(f'{folder_from}/{f}')
#         # if os.path.isfile(os.path.join(folder_from, f)):
#         #     print(os.path.join(folder_from, f), os.path.join(folder_to, f))
#         shutil.copy(f'{folder_from}/{f}', f'{folder_to}/{f}')
#     # print(sw)
#     sw = from_json('source_water', path=directory[-3:] + '/', mode='l')
#     root.destroy()

















def concat_arrays(path, files_list):
    files_list = files_list
    total_array = np.load(path + files_list[0])
    total_array = total_array.reshape(total_array.shape[0], total_array.shape[2])
    for i in range(1, len(files_list)):
        second_array = np.load(path + files_list[i])
        second_array = second_array.reshape(second_array.shape[0], second_array.shape[2])
        total_array = np.hstack((total_array, second_array))
    return total_array


def create_catalogs():
    path = os.getcwd()
    try:
        os.makedirs(path+ f'/input/values')
        print('готово')
        os.makedirs(path + f'/input/names')
        print('готово')
        os.makedirs(path + f'/start/values')
        print('готово')
        os.makedirs(path + f'/start/names')
        print('готово')
        os.makedirs(path + f'/output/values')
        print('готово')
        os.makedirs(path + f'/output/names')
    except:
        pass


def set_start_values(*args):
    files_names, files_values = args
    i = 0
    for arg in files_values:
        names = []          # Подготавливаем под имена
        values = []         # Подготавливаем под значения
        for el in arg:          # Разархивируем объект
            names.append(el)        # Сохраняем имена
            values.append(arg[el]['value'])         # Сохраняем значения
        values = np.asarray(values)         # Прверащаем в numpy массив
        values = values.reshape((1, values.shape[0]))        # Решейпим столбец в строку
        names = np.asarray(names)       # Прверащаем в numpy массив
        names = names.reshape((1, names.shape[0]))      # Решейпим столбец в строку
        np.save(os.getcwd() + f'/start/names/{files_names[i]}_names', names)        # Сохраняем массив имён
        np.save(os.getcwd() + f'/input/names/{files_names[i]}_names', names)        # Сохраняем его же для входных параметров
        np.save(os.getcwd() + f'/start/values/{files_names[i]}_values', values)         # Сохраняем массив значений входных параметров

        i += 1


# def save_changes(*args, path, mode):
#     files_names, files_values = args
#     i = 0
#     for arg in files_values:
#         names = []
#         values = []
#         for el in arg:
#             names.append(el)
#             values.append(arg[el]['value'])
#
#         np.save(path + f'/{mode}/names/{args[0][i]}_names', names)
#         np.save(path + f'/{mode}/values/{args[0][i]}_values', values)
#         print(pd.DataFrame, values)
#         i += 1
#     values = np.asarray(values)
#     # созранение и загрузка файла
#     # np.save(path + f'/names/{mode}_names', names)
#     # np.save(path + f'/values/{mode}_values', values)
#     return names, values


# def create_output_array(*args, path):
#     output_path = path + f'/values/output_'
#     input_path = path + f'/values/input_'
#
#     input_array = np.load(input_path + 'values.npy')
#     # print(input_array)
#     names = []
#     values = []
#     for arg in args:
#         for el in arg:
#             names.append(el)
#     np.save(path + f'/names/output_names', names)
#     x = np.load(path + f'/names/output_names.npy')
#     # print(x)
#     calculate_zones()


# if __name__== '__main__':
#     values_generator()
#     concat_arrays('D:\\Max\\Clean Water Samara\\Data_generator/input/values/')
    # ar = np.load('D:\\Max\\Clean Water Samara\\Data_generator/input/values/technological_parameters_values.npy')
    # ar = ar.reshape(5, 9)
    # print(ar.shape)
    # df = pd.DataFrame(ar)
    # print(df)
