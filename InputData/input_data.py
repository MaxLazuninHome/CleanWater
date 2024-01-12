from Functions.abbreviation import load_input_data

from InputData.SourceWater import source_water as sw
from InputData.TechnologicalParameters import technological_parameters as tp
from InputData.ConstructionParameters import construction_parameters as cp
from InputData.Constants import constants as c




# Данный файл объединяет все импорты в один словарь для подачи его в объект UI для отображения входных параметров

source_water = {
                    'name': 'source_water',
                    'value': sw.source_water
                }
construction_parameters = {
                    'name': 'construction_parameters',
                    'value': cp.construction_parameters
                          }
constants = {
                'name': 'constants',
                'value': c.constants
            }
technological_parameters = {
                                'name': 'technological_parameters',
                                'value': tp.technological_parameters
                           }




if __name__ == '__main__':
    print(sw.source_water)
