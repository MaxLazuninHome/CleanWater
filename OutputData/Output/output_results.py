from Functions.to_from_json import to_json

output_results = {
    't_anaerobic':
        {
        'value': None,
        'value_old': None,
        'description': 'Tанаэр - продолжительность пребывания в анаэробной зоне, ч',
        'mod': 'out',
        'ui_element': None
        },
    't_anoxide':
        {
            'value': None,
            'value_old': None,
            'description': 'Тaнокс - продолжительность пребывания в аноксидной зоне, ч',
            'mod': 'out',
            'ui_element': None
        },
    't_aerobic':
        {
            'value': None,
            'value_old': None,
            'description': 'Тaэр - продолжительность пребывания в аэробной зоне, ч',
            'mod': 'out',
            'ui_element': None
        },
    't_total':
        {
            'value': None,
            'value_old': None,
            'description': 'Тобщ - суммарная продолжительность пребывания в аэротенке, ч',
            'mod': 'out',
            'ui_element': None
        },
    'r_common':
        {
            'value': None,
            'value_old': None,
            'description': 'Rобщ - кратность циркуляции общая, доли Q',
            'mod': 'out',
            'ui_element': None
        },
    'r_nitrification':
        {
            'value': None,
            'value_old': None,
            'description': 'Rнитр - кратность нитратного рецикла, доли Q',
            'mod': 'out',
            'ui_element': None
        },
    "r_anaerobic":
        {
            'value': None,
            'value_old': None,
            'description': 'Ranaer - кратность анаэробного рецикла м3/ч',
            'mod': 'out',
            'ui_element': None
        },
    'teta_aerobic':
        {
            'value': None,
            'value_old': None,
            'description': 'θаэр - аэробный возраст АИ, сут',
            'mod': 'out',
            'ui_element': None
        },
    'teta_a1':
        {
            'value': None,
            'value_old': None,
            'description': 'θА1 - расчетное значение аэробного возраста АИ '
                           'для достижения требуемой концентрации N-NH4, сут',
            'mod': 'out',
            'ui_element': None
        },
    'teta_a2':
        {
            'value': None,
            'value_old': None,
            'description': 'θА2 - Расчетное значение аэробного возраста АИ '
                           'для достижения требуемой концентрации N-NO2, сут',
            'mod': 'out',
            'ui_element': None
        },
    's_nitrification':
        {
            'value': None,
            'value_old': None,
            'description': 'ЩН - щелочность после нитрификации, мг-экв/л',
            'mod': 'out',
            'ui_element': None
        },
    'load_bod_5':
        {
            'value': None,
            'value_old': None,
            'description': 'Нагрузка по БПК5 на беззольное вещество qi,г БПК/(г×сут)',
            'mod': 'out',
            'ui_element': None
        },
}

if __name__ == '__main__':
    to_json([output_results], 'output_data')