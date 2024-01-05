from Functions import to_from_json


source_water = {
    "q":
        {
            'value': 52140,
            'description': 'Q - расход сточных вод суточный, м3/сут',
            'mod': 'in',
            'use_in_work': False
        },
    "q_h":
        {
            'value': 2173,
            'description': 'Qч - расход сточных вод часовой, м3/ч',
            'mod': 'in',
            'use_in_work': False
        },
    "temperature":
        {
            'value': 21.6,
            'description': 'Т - температура, °C',
            'mod': 'in',
            'use_in_work': False
        },
    "l_in":
        {
            'value': 100,
            'description': 'Lвх - БПК5, мг/л',
            'mod': 'in',
            'use_in_work': False
        },
    "cod_in":
        {
            'value': 223,
            'description': 'ХПКвх - ХПК, мг/л',
            'mod': 'in',
            'use_in_work': False
        },
    "c_in":
        {
            'value': 29,
            'description': 'Свх  - взвешенные вещества, мг/л',
            'mod': 'in',
            'use_in_work': False
        },
    "alkalinity":
        {
            'value': 6.2,
            'description': 'Щвх - щелочность, ммоль/л HCO3',
            'mod': 'in',
            'use_in_work': False
        },
    "p_po4_in":
        {
            'value': 2.6,
            'description': 'PPO4,вх - фосфор фосфатов, мг/л ',
            'mod': 'in',
            'use_in_work': False
        },
    "ammonium_ion":
        {
            'value': 42,
            'description': 'Аммоний-ион, мг/л',
            'mod': 'in',
            'use_in_work': False
        },
    "nitrite_ion":
        {
            'value': 0.14,
            'description': 'Нитрит-ион, мг/л',
            'mod': 'in',
            'use_in_work': False
        },
    "nitrate_ion":
        {
            'value': 0,
            'description': 'Нитрат-ион, мг/л',
            'mod': 'in',
            'use_in_work': False
        },
    "n_ammonium_in":
        {
            'value': None,
            'description': 'Nам,вх - азот аммонийный, мг/л ',
            'mod': '',
            'use_in_work': False
        },
    "n_nitrites_in":
        {
            'value': None,
            'description': 'NNО2,вх - азот нитритов, мг/л ',
            'mod': '',
            'use_in_work': False
        },
    "n_nitrates_in":
        {
            'value': None,
            'description': 'NNО3,вх - азот нитратов, мг/л ',
            'mod': '',
            'use_in_work': False
        },
}

# source_water = to_from_json.from_json('source_water')


if __name__ == '__main__':
    to_from_json.to_json([source_water], 'source_water', mode='b')
    to_from_json.to_json([source_water], 'source_water', mode='c')
