from copy import deepcopy
from Functions.set_values import first_run
from Functions.abbreviation import load_input_data
from Functions.functions import calculate
from InputData.input_data import source_water


def create_deep_copy():     # Создаём deep-копии, что бы не менять сами файлы в процессе итераций
    """
    Функция для создания глубкой копии входных параметров.
    Будет использоваться для работы с декоратором итеративного расчёта.
    После проведения итертивного расчёта для выдачи рекомендаций нужно вернуть программу в исходное состояние.
    При этом сами расчёты будут проводиться в оригиналах файлов,
    поскольку функции расчёта эшелонов настроены на эти файлы.
    После завершения итерационного расчёта значения из deep-копий вернутся в исходные файлы
    :return: c, sw, tp, cp
    """
    c, sw, tp, cp = load_input_data()
    c = deepcopy(c)
    sw = deepcopy(sw)
    tp = deepcopy(tp)
    cp = deepcopy(cp)

    return c, sw, tp, cp


c, sw, tp, cp = create_deep_copy()

# source_water = {
#                     'name': 'source_water',
#                     'value': sw.source_water
#                 }
# construction_parameters = {
#                     'name': 'construction_parameters',
#                     'value': cp.construction_parameters
#                           }
# constants = {
#                 'name': 'constants',
#                 'value': c.constants
#             }
# technological_parameters = {
#                                 'name': 'technological_parameters',
#                                 'value': tp.technological_parameters
#                             }


def save_values_decorator(calculate):
    def inner():
        c, sw, tp, cp = create_deep_copy()
        calculate()
        c, sw, tp, cp = load_input_data()
    return inner


@save_values_decorator
def iterating_calculate():
    pass


if __name__ == '__main__':

    iterating_calculate()


