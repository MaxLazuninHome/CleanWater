"""
В данном эшелоне будет проводиться циклический расчёт, замкнутый сам на себя.
В качестве отправной точки будет заданно некоторое стартовое значене
для ключевой переменной, к которой происходит возврат при расчёте.
Этими значениями станут требования, предъявляемые к данным показателям.
"""

from Functions.Echelones import first_echelon_function, second_echelon_function, third_echelon_function
from Functions.abbreviation import abbreviation
from InputData.Constants import constants
from InputData.SourceWater import source_water
from InputData.ConstructionParameters import construction_parameters
from InputData.TechnologicalParameters import technological_parameters
from OutputData.Calculate.AnaerobicZone import anaerobic_results
from OutputData.PurifiedWaterQuality import purified_water_quality_results, requirements_for_purified_water
from OutputData.Calculate.AerobicZone.NitrficationVelocityCalculate import nitrification_velocity_calculate_results
from OutputData.Calculate.AerobicZone.OrganicSubstancesOxidation import organic_substances_oxidation_results
from OutputData.Calculate.AerobicZone.NitrificationFirstStage import nitrification_first_stage_result
from OutputData.Calculate.AnoxideZone import anoxyde_results
from OutputData.Output import output_results


v, d = abbreviation()
pwqr = purified_water_quality_results.purified_water_quality_results
nvcr = nitrification_velocity_calculate_results.nitrification_velocity
nfsr = nitrification_first_stage_result.nitrification_first_stage_results
osor = organic_substances_oxidation_results.organic_substances_oxidation
rpw = requirements_for_purified_water.requirements_for_purified_water
axr = anoxyde_results.anoxide_results
our = output_results.output_results
aar = anaerobic_results.anaerobic_results
sw = source_water.source_water
cp = construction_parameters.construction_parameters
tp = technological_parameters.technological_parameters
c = constants.constants


def circle_echelone(iterations):

    pwqr['n_ammonium_out'][v] = rpw['n_ammonium_out_req'][v]
    pwqr['n_no3_out'][v] = rpw['n_no3_out_req'][v]
    axr['l_anoxide_diluted_out'][v] = 8.529
    # axr['l_anoxide_diluted_out'][v] = ((sw['l_in'][v] - axr['delta_l_anoxide'][v]))

    for i in range(iterations):
        for j in range(iterations):

            axr['delta_alkalinity_denitrification'][v] = \
                (axr['tkn'][v] - pwqr['n_ammonium_out'][v] - pwqr['n_no2_out'][v] - pwqr['n_no3_out'][v] -
                 axr['n_increase'][v]) / 14 * c['delta_alk_denitrification_increase'][v]

            axr['alkalinity_denitrification'][v] = sw['alkalinity'][v] + axr['delta_alkalinity_denitrification'][v]

            nvcr['delta_alkalinity_nitrification'][v] = \
                (axr['tkn'][v] - pwqr['n_ammonium_out'][v] - axr['n_increase'][v]) / \
                14 * c['delta_alc_nitrification_decrease'][v]

            our['s_nitrification'][v] = axr['alkalinity_denitrification'][v] - nvcr['delta_alkalinity_nitrification'][v]

            nfsr['n_ammonium_teta_out'][v] = \
                c['k_s_a1'][v] / (nfsr['mu_max_a1'][v] * tp['c_0'][v] *
                                  our['s_nitrification'][v] *
                                  cp['w_aerobic'][v] * tp['a_i'][v] /
                                  (tp['q_i'][v] * tp['a_extra'][v] + pwqr['a_t'][v] /
                                   1000 * sw['q'][v] + nfsr['b_a1'][v] * cp['w_aerobic'][v] *
                                   tp['a_i'][v]) / (tp['c_0'][v] + c['k_s_o2_a1'][v]) /
                                  (our['s_nitrification'][v] + c['k_s_alc_a1'][v]) - 1)

            pwqr['n_ammonium_out'][v] = max(nfsr['n_ammonium_teta_out'][v], nvcr['x_1'][v])

        for j in range(iterations):

            axr['delta_l_anoxide'][v] = \
                (axr['tkn'][v] - pwqr['n_ammonium_out'][v] - pwqr['n_no2_out'][v] -
                 pwqr['n_no3_out'][v] - axr['n_increase'][v]) * c['teta'][v]
            #
            osor['l_aerobic'][v] = sw['l_in'][v] - axr['delta_l_anoxide'][v]    # - axr['delta_l_anoxide'][v]

            osor['d_bod'][v] = \
                (our['t_aerobic'][v] * osor['z'][v] + c['k_m_bod'][v] - osor['l_aerobic'][v]) ** 2 + \
                4 * osor['l_aerobic'][v] * c['k_m_bod'][v]
            osor['l_out_s'][v] = \
                (osor['l_aerobic'][v] - c['k_m_bod'][v] - our['t_aerobic'][v] * osor['z'][v] + osor['d_bod'][
                    v] ** 0.5) / 2
            pwqr['l_out'][v] = osor['l_out_s'][v] + c['l_i'][v] * pwqr['a_t'][v]

            axr['l_anoxide_diluted_out'][v] = ((sw['l_in'][v] - axr['delta_l_anoxide'][v]) +
                                               pwqr['l_out'][v] * our['r_common'][v]) / (1 + our['r_common'][v])
            axr['z_d'][v] = \
                    axr['mu_max_d'][v] / c['y_d'][v] * axr['l_anoxide_diluted_out'][v] / \
                (axr['l_anoxide_diluted_out'][v] + c['k_s_bod'][v]) * \
                c['k_s_o2_no3'][v] / (c['k_s_o2_no3'][v] + tp['c_0_anoxide'][v]) * \
                axr['x_b'][v] * 1000 / 24 / tp['a_i'][v] / (1 - tp['s'][v])
            axr['delta_n_denitrification'][v] = \
                axr['tkn'][v] + sw['n_nitrites_in'][v] + sw['n_nitrates_in'][v] - \
                pwqr['n_ammonium_out'][v] - pwqr['n_no2_out'][v] - pwqr['n_no3_out'][v] - axr['n_increase'][v]

            axr['d_d'][v] = (c['k_s_no3'][v] - axr['delta_n_denitrification'][v] + axr['z_d'][v] * axr['u_d'][v] -
                             axr['y_d'][v] * axr['u_d'][v]) ** 2 + 4 * \
                            (axr['delta_n_denitrification'][v] * c['k_s_no3'][v] +
                             axr['y_d'][v] * c['k_s_no3'][v] * axr['u_d'][v])
            axr['x_1'][v] = (axr['delta_n_denitrification'][v] + axr['y_d'][v] * axr['u_d'][v] - c['k_s_no3'][v] -
                             axr['z_d'][v] * axr['u_d'][v] + axr['d_d'][v] ** 0.5) / 2
            axr['x_3'][v] = axr['delta_n_denitrification'][v] / (our['r_common'][v] + 1)
            axr['x_4'][v] = \
                axr['delta_n_denitrification'][v] - (axr['l_anoxide'][v] - osor['l_aerobic'][v]) / c['teta'][v]
            #
            pwqr['n_no3_out'][v] = max(axr['x_1'][v], axr['x_3'][v], axr['x_4'][v])

if __name__ == '__main__':
    first_echelon_function.first_echelon()
    second_echelon_function.second_echelon()
    third_echelon_function.third_echelon()
    circle_echelone(10)

    print(f"{round(nvcr['delta_alkalinity_nitrification'][v], 2) :<10}{nvcr['delta_alkalinity_nitrification'][d]}")
    print(f"{round(axr['delta_alkalinity_denitrification'][v], 2) :<10}{axr['delta_alkalinity_denitrification'][d]}")
    print(f"{round(axr['alkalinity_denitrification'][v], 2) :<10}{axr['alkalinity_denitrification'][d]}")
    print(f"{round(our['s_nitrification'][v], 2) :<10}{our['s_nitrification'][d]}")
    print(f"{round(nfsr['n_ammonium_teta_out'][v], 2) :<10}{nfsr['n_ammonium_teta_out'][d]}")
    print(f"{round(pwqr['n_ammonium_out'][v], 2) :<10}{pwqr['n_ammonium_out'][d]}")
    print(f"{round(axr['delta_l_anoxide'][v]) :<10}{axr['delta_l_anoxide'][d]}")
    print(f"{round(osor['l_aerobic'][v], 1) :<10}{osor['l_aerobic'][d]}")
    print(f"{round(osor['d_bod'][v]) :<10}{osor['d_bod'][d]} ")
    print(f"{round(osor['l_out_s'][v], 2) :<10}{osor['l_out_s'][d]}")
    print(f"{round(pwqr['l_out'][v], 2) :<10}{pwqr['l_out'][d]}")
    print(f"{round(axr['l_anoxide_diluted_out'][v], 2) :<10}{axr['l_anoxide_diluted_out'][d]}")
    print(f"{round(axr['z_d'][v], 2) :<10}{axr['z_d'][d]}")
    print(f"{round(axr['delta_n_denitrification'][v], 1) :<10}{axr['delta_n_denitrification'][d]}")
    print(f"{round(axr['d_d'][v], 1) :<10}{axr['d_d'][d]}")
    print(f"{round(axr['x_1'][v], 1) :<10}{axr['x_1'][d]}")
    print(f"{round(axr['x_3'][v], 1) :<10}{axr['x_3'][d]}")
    print(f"{round(axr['x_4'][v], 1) :<10}{axr['x_4'][d]}")
    print(f"{round(pwqr['n_no3_out'][v], 1) :<10}{pwqr['n_no3_out'][d]}")
