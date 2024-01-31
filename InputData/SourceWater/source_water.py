from Functions import to_from_json


source_water = {
    "q":
        {
            'value': 52140,
            'description': 'Q - расход сточных вод суточный, м3/сут',
            'mod': 'in',
            'min_value': 0.9,
            'max_value': 1071000,
            'use_in_work': False,
            'ui_element': None
        },
    "q_h":
        {
            'value': 2173,
            'description': 'Qч - расход сточных вод часовой, м3/ч',
            'mod': 'in',
            'min_value': 0.04,
            'max_value': 133875,
            'use_in_work': False,
            'ui_element': None
        },
    "temperature":
        {
            'value': 21.6,
            'description': 'Т - температура, °C',
            'mod': 'in',
            'min_value': 10,
            'max_value': 32,
            'use_in_work': False,
            'ui_element': None
        },
    "l_in":
        {
            'value': 100,
            'description': 'Lвх - БПК5, мг/л',
            'mod': 'in',
            'min_value': 94,
            'max_value': 200,
            'use_in_work': False,
            'ui_element': None
        },
    "cod_in":
        {
            'value': 223,
            'description': 'ХПКвх - ХПК, мг/л',
            'mod': 'in',
            'min_value': 113,
            'max_value': 600,
            'use_in_work': False,
            'ui_element': None
        },
    "c_in":
        {
            'value': 29,
            'description': 'Свх  - взвешенные вещества, мг/л',
            'mod': 'in',
            'min_value': 10,
            'max_value': 1000,
            'use_in_work': False,
            'ui_element': None
        },
    "alkalinity":
        {
            'value': 6.2,
            'description': 'Щвх - щелочность, ммоль/л HCO3',
            'mod': 'in',
            'min_value': 4,
            'max_value': 20,
            'use_in_work': False,
            'ui_element': None
        },
    "p_po4_in":
        {
            'value': 2.6,
            'description': 'PPO4,вх - фосфор фосфатов, мг/л ',
            'mod': 'in',
            'min_value': 1,
            'max_value': 20,
            'use_in_work': False,
            'ui_element': None
        },
    "ammonium_ion":
        {
            'value': 42,
            'description': 'Аммоний-ион, мг/л',
            'mod': 'in',
            'min_value': 5,
            'max_value': 45,
            'use_in_work': False,
            'ui_element': None
        },
    "nitrite_ion":
        {
            'value': 0.14,
            'description': 'Нитрит-ион, мг/л',
            'mod': 'in',
            'min_value': 0,
            'max_value': 70,
            'use_in_work': False,
            'ui_element': None
        },
    "nitrate_ion":
        {
            'value': 0,
            'description': 'Нитрат-ион, мг/л',
            'mod': 'in',
            'min_value': 0,
            'max_value': 70,
            'use_in_work': False,
            'ui_element': None
        },
    "n_ammonium_in":
        {
            'value': None,
            'description': 'Nам,вх - азот аммонийный, мг/л ',
            'mod': '',
            'min_value': 3.89,
            'max_value': 35,
            'use_in_work': False,
            'ui_element': None
        },
    "n_nitrites_in":
        {
            'value': None,
            'description': 'NNО2,вх - азот нитритов, мг/л ',
            'mod': '',
            'min_value': 0,
            'max_value': 21.3,
            'use_in_work': False,
            'ui_element': None
        },
    "n_nitrates_in":
        {
            'value': None,
            'description': 'NNО3,вх - азот нитратов, мг/л ',
            'mod': '',
            'min_value': 0,
            'max_value': 15.8,
            'use_in_work': False,
            'ui_element': None
        },
}

source_water = to_from_json.from_json('source_water')
#

if __name__ == '__main__':
    to_from_json.to_json([source_water], 'source_water', mode='b')
    to_from_json.to_json([source_water], 'source_water', mode='c')
