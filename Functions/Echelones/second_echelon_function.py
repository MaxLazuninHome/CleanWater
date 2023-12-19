"""
Функция второго эшелона расчитывает значения,
для которых необходимы входные данные,
или значения из первого эшелона.
"""

from Functions.abbreviation import abbreviation
from Functions.Echelones.first_echelon_function import first_echelon
from math import exp, log
from InputData.SourceWater import source_water
from InputData.ConstructionParameters import construction_parameters
from InputData.Constants import constants
from InputData.TechnologicalParameters import technological_parameters
from OutputData.Calculate.AerobicZone.SecondarySump import secondary_sump_results
from OutputData.Calculate.AnaerobicZone import anaerobic_results
from OutputData.Output import output_results
from OutputData.Calculate.PhosphorusRemoval.PhosphorusRemovalFAO import phosphorus_removal_fao_results
from OutputData.Calculate.AerobicZone.NitrificationSecondStage import nitrification_second_stage_results
from OutputData.Calculate.AnoxideZone import anoxyde_results
from OutputData.PurifiedWaterQuality.requirements_for_purified_water import requirements_for_purified_water
from OutputData.PurifiedWaterQuality import purified_water_quality_results


v, d = abbreviation()
prfao = phosphorus_removal_fao_results.phosphorus_removal_fao_results
pwqr = purified_water_quality_results.purified_water_quality_results
nssr = nitrification_second_stage_results.nitrification_second_stage_results
ssr = secondary_sump_results.secondary_sump_results
rpw = requirements_for_purified_water
aar = anaerobic_results.anaerobic_results
axr = anoxyde_results.anoxide_results
our = output_results.output_results
sw = source_water.source_water
cp = construction_parameters.construction_parameters
tp = technological_parameters.technological_parameters
c = constants.constants


def second_echelon():

    aar['d'][v] = (c['k_acetate_saturation'][v] + our['t_anaerobic'][v] / 24 * c['k_acetate_consumption'][v] *
                   exp(c['hi_consumption'][v] * (sw['temperature'][v] - 20)) - aar['s_acetate_in'][v]) ** 2 + \
                 4 * aar['s_acetate_in'][v] * c['k_acetate_saturation'][v]

    aar['s_acetate_anaerobic'][v] = (aar['s_acetate_in'][v] - our['t_anaerobic'][v] / 24 *
                                     c['k_acetate_consumption'][v] *
                                     exp(c['hi_consumption'][v] * (sw['temperature'][v] - 20)) -
                                     c['k_acetate_saturation'][v] + aar['d'][v] ** 0.5) / 2

    aar['delta_l_anaerobic'][v] = aar['s_acetate_in'][v] - aar['s_acetate_anaerobic'][v]

    prfao['delta_p_acetate'][v] = (aar['s_acetate_in'][v] - aar['s_acetate_anaerobic'][v]) * c['n_acetate_p'][v]

    # axr['z_d'][v] = \
    #     axr['mu_max_d'][v] / c['y_d'][v] * axr['l_anoxide_diluted_out'][v] / \
    #     (axr['l_anoxide_diluted_out'][v] + c['k_s_bod'][v]) * \
    #     c['k_s_o2_no3'][v] / (c['k_s_o2_no3'][v] + tp['c_0_anoxide'][v]) * \
    #     axr['x_b'][v] * 1000 / 24 / tp['a_i'][v] / (1 - tp['s'][v])
    axr['bod5_tkn'][v] = axr['l_anoxide'][v] / axr['tkn'][v]
    axr['y_d'][v] = axr['b_d'][v] * axr['x_b'][v] * 1000 / 24 / tp['a_i'][v] / (1 - tp['s'][v])
    axr['u_d'][v] = tp['a_i'][v] * (1 - tp['s'][v]) * our['t_anoxide'][v]

    ssr['k'][v] = 4.5 * cp['k_ss'][v] * cp['h_set'][v] ** 0.8 / ssr['q_ssa'][v]

    our['r_nitrification'][v] = our['r_common'][v] - axr['r_i'][v]

    our['teta_a2'][v] = 1 / ((nssr['mu_max_a2'][v] * (rpw['n_no2_out_req'][v] /
                                                      (rpw['n_no2_out_req'][v] + c['k_s_a2'][v])) *
                              (tp['c_0'][v] / (tp['c_0'][v] + c['k_s_o2_a2'][v]))) - nssr['b_a2'][v])

    our['load_bod_5'][v] = (24 * sw['l_in'][v]) / (tp['a_i'][v] * (1 - tp['s'][v]) * our['t_total'][v])
    if 100 * (0.5 - log(ssr['k'][v], ssr['a'][v])) < 4:
        pwqr['a_t'][v] = 4
    else:
        pwqr['a_t'][v] = 100 * (0.5 - log(ssr['k'][v], ssr['a'][v]))


if __name__ == "__main__":
    first_echelon()
    second_echelon()
    print(f"{round(aar['delta_l_anaerobic'][v], 1):<10}{aar['delta_l_anaerobic'][d]}")
    print(f"{round(aar['d'][v]) :<10}{aar['d'][d]}")
    print(f"{round(aar['s_acetate_anaerobic'][v], 1) :<10}{aar['s_acetate_anaerobic'][d]}")

    print(f"{round(prfao['delta_p_acetate'][v], 1):<10}{prfao['delta_p_acetate'][d]}")
    # print(f"{round(axr['z_d'][v], 2) :<10}{axr['z_d'][d]}")
    print(f"{round(axr['bod5_tkn'][v], 1) :<10}{axr['bod5_tkn'][d]}")
    print(f"{round(axr['y_d'][v], 1) :<10}{axr['y_d'][d]}")
    print(f"{round(axr['u_d'][v], 1) :<10}{axr['u_d'][d]}")
    print(f"{round(ssr['k'][v], 2) :<10}{ssr['k'][d]}")
    print(f"{round(our['r_nitrification'][v], 2) :<10}{our['r_nitrification'][d]}")
    print(f"{round(our['teta_a2'][v], 2) :<10}{our['teta_a2'][d]}")
    print(f"{round(our['load_bod_5'][v], 2) :<10}{our['load_bod_5'][d]}")
    print(f"{round(pwqr['a_t'][v], 2) :<10}{pwqr['a_t'][d]}")
