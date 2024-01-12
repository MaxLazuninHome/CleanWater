from Functions.to_from_json import to_json

purified_water_quality_results = {
    'n_ammonium_out': {
        'value': None,
        'value_old': None,
        'description': 'Nам,вых - азот аммонийный, мг/л ',
        'mod': 'out'
    },
    'n_no2_out': {
        'value': None,
        'value_old': None,
        'description': 'NNО2,вых - азот нитритов, мг/л ',
        'mod': 'out'
    },
    'n_no3_out': {
        'value': None,
        'value_old': None,
        'description': 'NNО3,вых - азот нитратов, мг/л ',
        'mod': 'out'
    },
    'ammonium_ion': {
        'value': None,
        'value_old': None,
        'description': 'Аммоний-ион, мг/л',
        'mod': 'out'
    },
    'nitrite_ion': {
        'value': None,
        'value_old': None,
        'description': 'Нитрит-ион, мг/л',
        'mod': 'out'
    },
    'nitrate_ion': {
        'value': None,
        'value_old': None,
        'description': 'Нитрат-ион, мг/л',
        'mod': 'out'
    },
    'l_out': {
        'value': None,
        'value_old': None,
        'description': 'Lвых - БПК5, мг/л',
        'mod': 'out'
    },
    'a_t': {
        'value': None,
        'value_old': None,
        'description': 'at - взвешенные вещества, мг/л',
        'mod': 'out'
    },
    'p_po4_out': {
        'value': None,
        'value_old': None,
        'description': 'PPO4,вых - фосфор фосфатов, мг/л ',
        'mod': 'out'
    },
}

if __name__ == '__main__':
    to_json([purified_water_quality_results], 'purified_water_quality_results')
