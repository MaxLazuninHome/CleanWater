from Functions.to_from_json import to_json

output_results = {
    't_anaerobic': {
        'value': None,
        'description': 'Tанаэр - продолжительность пребывания в анаэробной зоне, ч',
        'mod': 'out'
    },
    't_anoxide': {
        'value': None,
        'description': 'Тaнокс - продолжительность пребывания в аноксидной зоне, ч',
        'mod': 'out'
    },
    't_aerobic': {
        'value': None,
        'description': 'Тaэр - продолжительность пребывания в аэробной зоне, ч',
        'mod': 'out'
    },
    't_total': {
        'value': None,
        'description': 'Тобщ - суммарная продолжительность пребывания в аэротенке, ч',
        'mod': 'out'
    },
    'r_common': {
        'value': None,
        'description': 'Rобщ - кратность циркуляции общая, доли Q',
        'mod': 'out'
    },
    'r_nitrification': {
        'value': None,
        'description': 'Rнитр - кратность нитратного рецикла, доли Q',
        'mod': 'out'
    },
    'teta_aerobic': {
        'value': None,
        'description': 'θаэр - аэробный возраст АИ, сут',
        'mod': 'out'
    },
    'teta_a1': {
        'value': None,
        'description': 'θА1 - расчетное значение аэробного возраста АИ '
                       'для достижения требуемой концентрации N-NH4, сут',
        'mod': 'out'
    },
    'teta_a2': {
        'value': None,
        'description': 'θА2 - Расчетное значение аэробного возраста АИ '
                       'для достижения требуемой концентрации N-NO2, сут',
        'mod': 'out'
    },
    's_nitrification': {
        'value': None,
        'description': 'ЩН - щелочность после нитрификации, мг-экв/л',
        'mod': 'out'
    },
    'load_bod_5': {
        'value': None,
        'description': 'Нагрузка по БПК5 на беззольное вещество qi,г БПК/(г×сут)',
        'mod': 'out'
    },
}

if __name__ == '__main__':
    to_json([output_results], 'output_data')