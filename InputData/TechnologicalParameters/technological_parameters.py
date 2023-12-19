# from InputData.SourceWater import source_water
from Functions import to_from_json
from Functions.abbreviation import load_input_data

technological_parameters = {
    "c_0":
        {
            'value': 4.9,
            'description': 'СО - КРК в аэробных зонах (усредненная по аэротенкам в значимой точке), O2, мг/л',
            'mod': 'in'
        },
    "c_0_anoxide":
        {
            'value': 0.2,
            'description': 'СОанокс - КРК в аноксидных зонах (усредненная по аэротенкам в значимой точке), O2, мг/л',
            'mod': 'in'
        },
    "a_i":
        {
            'value': 2.2,
            'description': 'ai - концентрация активного ила в аэротенках, г/л',
            'mod': 'in'
        },
    "q_anaerobic":
        {
            'value': 2040,
            'description': 'Qанаэр - расход анаэробного рецикла общий на все аэротенки, м3/ч',
            'mod': 'in'
        },
    "a_extra":
        {
            'value': 4,
            'description': 'aИ - концентрация избыточного и возвратного АИ, г/л',
            'mod': 'in'
        },
    "q_nitrification":
        {
            'value': 2600,
            'description': 'Qнитр - расход нитратного рецикла общий на все аэротенки, м3/ч',
            'mod': 'in'
        },
    "q_return":
        {
            'value': 2200,
            'description': 'QВ - расход возвратного АИ общий на все аэротенки, м3/ч',
            'mod': 'in'
        },
    "q_i":
        {
            'value': 290,
            'description': 'QИ - расход избыточного АИ, м3/сут',
            'mod': 'in'
        },
    "s":
        {
            'value': 0.35,
            'description': 's - зольность, доли единицы',
            'mod': 'in'
        },
    "r_anaerobic":
        {
            'value': None,
            'description': 'Ranaer - кратность анаэробного рецикла м3/ч',
            'mod': 'in'
        },
    "reagent":
        {
            'value': 1,
            'description': 'Вид реагента для удаления фосфора по металлу; Al - 1, Fe - 2',
            'mod': 'in'
        },
    "d_me":
        {
            'value': 0,
            'description': 'DMе - доза реагента по металлу, мг/л',
            'mod': 'in'
        },
    "j_i":
        {
            'value': 57,
            'description': 'Ji - иловый индекс, мл/г',
            'mod': 'in'
        },
}
_, sw, _, _ = load_input_data()

technological_parameters['r_anaerobic']['volume'] = \
    technological_parameters['q_anaerobic']['value'] / sw['q_h']['value']

technological_parameters = to_from_json.from_json('technological_parameters')


# if __name__ == '__main__':
#     to_from_json.to_json([technological_parameters], 'technological_parameters', mode='b')