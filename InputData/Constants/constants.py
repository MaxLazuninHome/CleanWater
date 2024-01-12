from Functions import to_from_json
from pprint import pprint
constants = {
    "tkn_n_nh4":
        {
            'value': 1.18,
            'description': 'TKN/N-NH4',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "p_common_p_po4":
        {
            'value': 1,
            'description': 'Робщ/P-PO4',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_acetate_cod":
        {
            'value': 0.05,
            'description': 'КНАс/БПК - доля ацетата в ХПК',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_cod_bod5":
        {
            'value': 2,
            'description': 'КХПК/БПК5',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_acetate_consumption":
        {
            'value': 1500,
            'description': 'k,НАс – константа потребления ацетата в анаэробной зоне, г ХПК/(м3×сут)',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_acetate_saturation":
        {
            'value': 3,
            'description': 'KS,HAc – константа насыщения по ацетату, мг/л',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "hi_consumption":
        {
            'value': 0.03,
            'description': 'cHAc - температурная константа потребления ацетата, 1/°C',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "n_acetate_p":
        {
            'value': 0.05,
            'description': 'nНАс,Р - стехиометрический коэффициент удаления фосфора, мг Р/мг ХПК ацетата',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "y":
        {
            'value': 0.6,
            'description': 'Y - коэффициент прироста биомассы, кгБВАИ/кг∆БПК',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "b":
        {
            'value': 0.05,
            'description': 'b - коэффициент распада биомассы, 1/сут',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_p":
        {
            'value': 6,
            'description': 'kP - содержание фосфора в БВАИ, %',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "c_i":
        {
            'value': 0.25,
            'description': 'Ci - фракция инертного вещества в общем количестве взвешенных веществ, доли ед.',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "mu_max_d_20":
        {
            'value': 2.25,
            'description': 'μmax,D,20 - максимальная скорость роста денитрифицирующих бактерий для 20°C, 1/сут',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "hi_denitrification":
        {
            'value': 0.06,
            'description': 'HIдн - температурная константа денитрификации, 1/°C',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_s_bod":
        {
            'value': 30,
            'description': 'KS,БПК - константа полунасыщения по БПК, мг/л',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_s_no3":
        {
            'value': 0.5,
            'description': 'Ks,NO3 - константа полунасыщения по N-NО3, мгN/л',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_s_o2_no3":
        {
            'value': 0.17,
            'description': 'Ks,O2,NO3 - константа полунасыщения по кислороду для NO3, мгО/л',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "b_d_20":
        {
            'value': 0.05,
            'description': 'bD,20 - Скорость распада денитрифицирующих микроорганизмов  для 20°C, 1/сут',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "y_d":
        {
            'value': 1.8,
            'description': 'YD - коэффициент прироста денитрифицирующей биомассы, ХПК(Б)/N-NO3(СВ)',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "cod_b":
        {
            'value': 1.42,
            'description': 'ХПКБ - перевод ХПК БВАИ в массу БВАИ гХПК/гБВАИ',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "teta":
        {
            'value': 2.86,
            'description': 'ϑ - стехиометрический коэффициент, мгБПК5/мг N-NO3',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_n":
        {
            'value': 0.08,
            'description': 'kN - содержание азота в БВАИ, г/г',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "delta_alk_denitrification_increase":
        {
            'value': 0.85,
            'description': 'ΔAlkДН - удельное увеличение щелочности за счет денитрификации, мг-экв/моль N-NO3',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "mu_max_a1_20":
        {
            'value': 0.8,
            'description': 'μmax,A1,20 - максимальная скорость роста '
                           'нитрифицирующих бактерий 1-й стадии для 20°C,1/сут',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "hi_a1":
        {
            'value': 0.12,
            'description': 'cА1 - температурная константа 1-й стадии нитрификации, 1/°C',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_s_a1":
        {
            'value': 1.45,
            'description': 'Ks,А1 - константа полунасыщения по N-NH4, мгN/л',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_s_o2_a1":
        {
            'value': 0.75,
            'description': 'Ks,O2,A1 - константа полунасыщения по кислороду для NH4, мгО/л',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_s_alc_a1":
        {
            'value': 0.5,
            'description': 'Ks,alk,A1 - константа полунасыщения по щелочности, ммольHCO3/л',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "b_a1_20":
        {
            'value': 0.15,
            'description': 'bA1,20 - скорость распада нитрифицирующих микроорганизмов '
                           '1-й стадии нитрификации для 20°C, 1/сут',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "mu_max_a2_20":
        {
            'value': 1.3,
            'description': 'μmax,A2,20 - максимальная скорость роста нитрифицирующих бактерий '
                           '2-й стадии для 20°C, 1/сут',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "hi_a2":
        {
            'value': 0.1,
            'description': 'cА2 - температурная константа 2-й стадии нитрификации, 1/°C',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_s_a2":
        {
            'value': 0.6,
            'description': 'Ks,A2 - константа полунасыщения по N-NO2, мгN/л',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_s_o2_a2":
        {
            'value': 0.9,
            'description': 'Ks,O2,A2 - константа полунасыщения по кислороду для NO2, мгО/л',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "b_a2_20":
        {
            'value': 0.03,
            'description': 'bA2,20 - скорость распада нитрифицирующих микроорганизмов '
                           '2й стадии нитрификации для 20°C, 1/сут',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "y_a":
        {
            'value': 0.1,
            'description': 'YA - коэффициент прироста биомассы нитрификаторов, гБВАИ/гN(a)',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "delta_alc_nitrification_decrease":
        {
            'value': 2,
            'description': 'ΔAlkН - удельное снижение щелочности за счет нитрификации, мг-экв/моль N-NН4',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "ro_max_a1":
        {
            'value': 8,
            'description': 'ρmax,А1 - максимальная скорость нитрификации 1-й стадии для 20°C, мг/(г×ч)',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_m_nh4":
        {
            'value': 0.3,
            'description': 'Km,NH4 - константа Михаэлиса по N-NH4, мгN/л',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "phi_n":
        {
            'value': 0.09,
            'description': 'ФН - коэффициент ингибирования продуктами метаболизма нитрифицир. ила, л/г',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "ro_max_bod":
        {
            'value': 16,
            'description': 'ρmax.БПК - максимальная скорость окисления БПК, мг/(г×ч) ',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_m_bod":
        {
            'value': 8,
            'description': 'Km.БПК - константа Михаэлиса окисления органических веществ, мг/л',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "hi_r":
        {
            'value': 0.09,
            'description': 'cг - температурная константа аэробного гетеротрофного процесса',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "k_0":
        {
            'value': 0.625,
            'description': 'Ко - кислородная константа гетеротрофного процесса, мгО/л',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "phi_r":
        {
            'value': 0.07,
            'description': 'jг - коэффициент ингибирования продуктами метаболизма гетеротрофн. ила, л/г',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "l_i":
        {
            'value': 0.3,
            'description': 'li - удельное БПК5 активного ила, г БПК/г СВ АИ',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "s_metr_ammonium_ion_n":
        {
            'value': 14 / 18,
            'description': 'Стеохиометрический коэффициент аммоний-иона в азот',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "s_metr_nitrite_ion_n":
        {
            'value': 14 / (14 + 32),
            'description': 'Стеохиометрический коэффициент нитрит-иона в азот',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "s_metr_nitrate_ion_n":
        {
            'value': 14 / (14 + 3 * 16),
            'description': 'Стеохиометрический коэффициент нитрат-иона в азот',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "s_metr_n_ammonium_ion":
        {
            'value': 18 / 14,
            'description': 'Стеохиометрический коэффициент азота в аммоний-ион',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "s_metr_n_nitrite_ion":
        {
            'value': (14 + 32) / 14,
            'description': 'Стеохиометрический коэффициент азота в нитрит-ион',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        },
    "s_metr_n_nitrate_ion":
        {
            'value': (14 + 3 * 16) / 14,
            'description': 'Стеохиометрический коэффициент азота в нитрат-ион',
            'mod': 'in',
            'use_in_work': False,
            'ui_element': None
        }

}
# constants['s_metr_n_ammonium_ion']['value'] = 1 / constants['s_metr_ammonium_ion_n']['value']
# constants['s_metr_n_nitrite_ion']['value'] = 1 / constants['s_metr_nitrite_ion_n']['value']
# constants['s_metr_n_nitrate_ion']['value'] = 1 / constants['s_metr_nitrate_ion_n']['value']

constants = to_from_json.from_json('constants')

if __name__ == '__main__':

    to_from_json.to_json([constants], 'constants', mode='b')
    to_from_json.to_json([constants], 'constants')

