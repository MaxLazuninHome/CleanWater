import pandas as pd
import numpy as np
import os
from Functions.functions import calculate_zones


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
