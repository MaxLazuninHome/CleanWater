from Functions import to_from_json


source_water = {
    "q":
        {
            'value': 52140,
            'description': 'Q - расход сточных вод суточный, м3/сут',
            'mod': 'in'
        },
    "q_h":
        {
            'value': 2173,
            'description': 'Qч - расход сточных вод часовой, м3/ч',
            'mod': 'in'
        },
    "temperature":
        {
            'value': 21.6,
            'description': 'Т - температура, °C',
            'mod': 'in'
        },
    "l_in":
        {
            'value': 100,
            'description': 'Lвх - БПК5, мг/л',
            'mod': 'in'
        },
    "cod_in":
        {
            'value': 223,
            'description': 'ХПКвх - ХПК, мг/л',
            'mod': 'in'
        },
    "c_in":
        {
            'value': 29,
            'description': 'Свх  - взвешенные вещества, мг/л',
            'mod': 'in'
        },
    "alkalinity":
        {
            'value': 6.2,
            'description': 'Щвх - щелочность, ммоль/л HCO3',
            'mod': 'in'
        },
    "p_po4_in":
        {
            'value': 2.6,
            'description': 'PPO4,вх - фосфор фосфатов, мг/л ',
            'mod': 'in'
        },
    "ammonium_ion":
        {
            'value': 42,
            'description': 'Аммоний-ион, мг/л',
            'mod': 'in'
        },
    "nitrite_ion":
        {
            'value': 0.14,
            'description': 'Нитрит-ион, мг/л',
            'mod': 'in'
        },
    "nitrate_ion":
        {
            'value': 0,
            'description': 'Нитрат-ион, мг/л',
            'mod': 'in'
        },
    "n_ammonium_in":
        {
            'value': None,
            'description': 'Nам,вх - азот аммонийный, мг/л ',
            'mod': ''
        },
    "n_nitrites_in":
        {
            'value': None,
            'description': 'NNО2,вх - азот нитритов, мг/л ',
            'mod': ''
        },
    "n_nitrates_in":
        {
            'value': None,
            'description': 'NNО3,вх - азот нитратов, мг/л ',
            'mod': ''
        },
}

source_water = to_from_json.from_json('source_water')


# def calculate_source_water():
#     source_water['n_ammonium_in']['value'] = source_water['ammonium_ion']['value'] * \
#                                              constants.constants['s_metr_ammonium_ion_n']['value']
#
#     source_water['n_nitrites_in']['value'] = source_water['nitrite_ion']['value'] * \
#                                              constants.constants['s_metr_nitrite_ion_n']['value']
#
#     source_water['n_nitrates_in']['value'] = source_water['nitrate_ion']['value'] * \
#                                              constants.constants['s_metr_nitrate_ion_n']['value']



# if __name__ == '__main__':
#     to_from_json.to_json([source_water], 'source_water', mode='b')
#     to_from_json.to_json([source_water], 'source_water', mode='b')
