from Functions.to_from_json import *
from InputData.SourceWater import source_water as sw
from InputData.TechnologicalParameters import technological_parameters as tp
from InputData.ConstructionParameters import construction_parameters as cp
from InputData.Constants import constants as c


def first_run():
    c.constants = from_json('constants')
    sw.source_water = from_json('source_water')
    tp.technological_parameters = from_json('technological_parameters')
    cp.construction_parameters = from_json('construction_parameters')



def save_values():

    to_json([sw.source_water], 'source_water')
    to_json([tp.technological_parameters], 'technological_parameters')
    to_json([cp.construction_parameters], 'construction_parameters')
    to_json([c.constants], 'constants')


if __name__ == '__main__':
    first_run()
