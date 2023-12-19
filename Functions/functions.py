import calculating_order

from Functions.abbreviation import load_input_data
import numpy as np
import pandas as pd
import os


c, sw, tp, cp = load_input_data()


def calculate_source_water():
    sw['n_ammonium_in']['value'] = sw['ammonium_ion']['value'] * c['s_metr_ammonium_ion_n']['value']
    sw['n_nitrites_in']['value'] = sw['nitrite_ion']['value'] * c['s_metr_nitrite_ion_n']['value']
    sw['n_nitrates_in']['value'] = sw['nitrate_ion']['value'] * c['s_metr_nitrate_ion_n']['value']


def calculate_zones():
    # calculate_source_water()
    calculating_order.complete_calculate()


def calculate(*args):

    for arg in args:
        arg.calculate()
    calculate_zones()
    for arg in args:
        arg.show_output()


def input_values_generator(examples_count, path, deviate=0.1):
    start_values_path = path + '/start/values/'
    input_values_path = path + '/input/values/'
    input_names_path = path + '/input/names'
    files_list = os.listdir(start_values_path)

    for el in files_list:

        if el != 'total_array.npy':                                                     # Проверяем, что бы не захватить конкатенированный массив
            start_values = np.load(start_values_path + el)                              # Загружаем первый массив значений
            start_values = start_values.reshape(start_values.shape[1])                  # Решейпим
            input_generated_list = []                                                   # Создаём список для будущей генерации
            for i in range(start_values.shape[0]):
                generated_value = np.random.uniform(start_values[i]-start_values[i]*deviate,       # По каждому значению генерируем случайное значение
                                                    start_values[i]+start_values[i]*deviate,       # в количестве examples_count штук
                                                    (1, examples_count))
                input_generated_list.append(generated_value)
            input_generated_array = np.asarray(input_generated_list)                               # Переделываем список в нампай массив
            generated_array = input_generated_array.transpose()                                    # Транспонируем
            generated_array = generated_array.reshape(generated_array.shape[0], generated_array.shape[2])      # Решейпим, что бы убрать лишнюю размерность
            np.save(input_values_path + el, generated_array)                                       # Сохраняем





    #Генерация выходного массива
def output_values_generator(path, output_obj_list, input_obj_list, input_obj_names, examples_count, output_names_list):

    input_values_path = path + '/input/values/'          # Папка с массивами входных параметров
    input_names_path = path + '/start/names/'             # Папка с массивами названий входных параметров
    output_names_path = path + '/output/names/'          # Папка с массивами названий выходных параметров
    output_values_path = path + '/output/values/'          # Папка с массивами значений выходных параметров
    nn_output_list = []


    # Сохранение массива названий выходных параметров
    output_names = list(output_obj_list[0].keys())
    np.save(output_names_path + '/output_names', output_names)

        # Генерация выходных результатов
    c = 0
    for count in range(examples_count):                                                     # 5000 - Предполагаемый размер датасета
        for obj_number in range(len(input_obj_list)):                                                # 3 - количество объектов входных параметров
            names_list = np.load(input_names_path + input_obj_names[obj_number] + '_names.npy')
            values_for_change_list = np.load(input_values_path + input_obj_names[obj_number] + '_values.npy')
            calculated_values = []
            for name_number in range(len(names_list)):                                             # Количество столбцов в объекте
                input_obj_list[obj_number][names_list[0][name_number]]['value'] = values_for_change_list[count][name_number]
                c += 1
        calculate_zones()

        for i in range(len(output_names)):

            calculated_values.append(output_obj_list[0][output_names[i]]['value'])
        calculated_values = np.asarray(calculated_values)
        nn_output_list.append(calculated_values)
        # print(len(nn_output_list))
        # print(nn_output_list)
    x = pd.DataFrame(nn_output_list)
    print('Финальная таблица выходных значений')
    print(x.shape)
    np.save(output_values_path + 'output_values', nn_output_list)
    np.save(path + '/output/names/output_names', output_names)
    # x = np.load(output_path + '/names/output_values.npy')
    # print(x)








            # print(el)
    # total_input_array = concat_arrays(input_path)
    # np.save(input_path + '/total_array', total_input_array)


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
