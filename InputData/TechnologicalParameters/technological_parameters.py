from Functions import to_from_json


technological_parameters = {
    "c_0":
        {
            'value': 4.9,
            'description': 'СО - КРК в аэробных зонах (усредненная по аэротенкам в значимой точке), O2, мг/л',
            'mod': 'in',
            'min_value': 1.5,
            'max_value': 8,
            'use_in_work': False,
            'ui_element': None
        },
    "c_0_anoxide":
        {
            'value': 0.2,
            'description': 'СОанокс - КРК в аноксидных зонах (усредненная по аэротенкам в значимой точке), O2, мг/л',
            'mod': 'in',
            'min_value': 0,
            'max_value': 2,
            'use_in_work': False,
            'ui_element': None
        },
    "a_i":
        {
            'value': 2.2,
            'description': 'ai - концентрация активного ила в аэротенках, г/л',
            'mod': 'in',
            'min_value': 0.2,
            'max_value': 5,
            'use_in_work': False,
            'ui_element': None
        },
    "q_anaerobic":
        {
            'value': 2040,
            'description': 'Qанаэр - расход анаэробного рецикла общий на все аэротенки, м3/ч',
            'mod': 'in',
            'min_value': 191,
            'max_value': 7628,
            'use_in_work': False,
            'ui_element': None
        },
    "a_extra":
        {
            'value': 4,
            'description': 'aИ - концентрация избыточного и возвратного АИ, г/л',
            'mod': 'in',
            'min_value': 3.31,
            'max_value': 4.04,
            'use_in_work': False,
            'ui_element': None
        },
    "q_nitrification":
        {
            'value': 2600,
            'description': 'Qнитр - расход нитратного рецикла общий на все аэротенки, м3/ч',
            'mod': 'in',
            'min_value': 38,
            'max_value': 38141,
            'use_in_work': False,
            'ui_element': None
        },
    "q_return":
        {
            'value': 2200,
            'description': 'QВ - расход возвратного АИ общий на все аэротенки, м3/ч',
            'mod': 'in',
            'min_value': 114,
            'max_value': 5721,
            'use_in_work': False,
            'ui_element': None
        },
    "q_i":
        {
            'value': 290,
            'description': 'QИ - расход избыточного АИ, м3/сут',
            'mod': 'in',
            'min_value': 0,
            'max_value': 2746,
            'use_in_work': False,
            'ui_element': None
        },
    "s":
        {
            'value': 0.35,
            'description': 's - зольность, доли единицы',
            'mod': 'in',
            'min_value': 0.1,
            'max_value': 0.4,
            'use_in_work': False,
            'ui_element': None
        },
    "reagent":
        {
            'value': 1,
            'description': 'Вид реагента для удаления фосфора по металлу; Al - 1, Fe - 2',
            'mod': 'in',
            'min_value': 0,
            'max_value': 1,
            'use_in_work': False,
            'ui_element': None
        },
    "d_me":
        {
            'value': 0,
            'description': 'DMе - доза реагента по металлу, мг/л',
            'mod': 'in',
            'min_value': 0,
            'max_value': 50,
            'use_in_work': False,
            'ui_element': None
        },
    "j_i":
        {
            'value': 57,
            'description': 'Ji - иловый индекс, мл/г',
            'mod': 'in',
            'min_value': 34,
            'max_value': 400,
            'use_in_work': False,
            'ui_element': None
        },
}

technological_parameters = to_from_json.from_json('technological_parameters')


if __name__ == '__main__':
    to_from_json.to_json([technological_parameters], 'technological_parameters', mode='b')
    to_from_json.to_json([technological_parameters], 'technological_parameters')
