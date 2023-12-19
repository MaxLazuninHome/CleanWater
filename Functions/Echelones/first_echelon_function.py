"""
Функция первого эшелона.
Включает в себя расчёт всех величин,
использующие только входные параметры
"""


from Functions.abbreviation import abbreviation
from Functions.set_values import first_run
from InputData.SourceWater import source_water
from InputData.Constants import constants
from InputData.TechnologicalParameters import technological_parameters
from InputData.ConstructionParameters import construction_parameters
from OutputData.Calculate.AnaerobicZone import anaerobic_results
from OutputData.Calculate.PhosphorusRemoval import phosphorus_removal_results
from OutputData.Calculate.PhosphorusRemoval.ChemicalPhosphorusRemoval import chemical_phosphorus_removal_results
from OutputData.Calculate.AerobicZone.NitrificationFirstStage import nitrification_first_stage_result
from OutputData.Calculate.AerobicZone.NitrificationSecondStage import nitrification_second_stage_results
from OutputData.Calculate.AerobicZone.NitrficationVelocityCalculate import nitrification_velocity_calculate_results
from OutputData.Calculate.AerobicZone.OrganicSubstancesOxidation import organic_substances_oxidation_results
from OutputData.Calculate.AerobicZone.SecondarySump import secondary_sump_results
from OutputData.Output import output_results

from OutputData.Calculate.AnoxideZone import anoxyde_results
from math import exp


v, d = abbreviation()
nvcr = nitrification_velocity_calculate_results.nitrification_velocity
nfsr = nitrification_first_stage_result.nitrification_first_stage_results
nssr = nitrification_second_stage_results.nitrification_second_stage_results
osor = organic_substances_oxidation_results.organic_substances_oxidation
our = output_results.output_results
ssr = secondary_sump_results.secondary_sump_results
aar = anaerobic_results.anaerobic_results
axr = anoxyde_results.anoxide_results
sw = source_water.source_water
prr = phosphorus_removal_results.phosphorus_removal_results
c = constants.constants
tp = technological_parameters.technological_parameters
cp = construction_parameters.construction_parameters
cprr = chemical_phosphorus_removal_results.chemical_phosphorus_removal_results


def first_echelon():

    sw['n_ammonium_in'][v] = sw['ammonium_ion'][v] * c['s_metr_ammonium_ion_n'][v]
    sw['n_nitrites_in'][v] = sw['nitrite_ion'][v] * c['s_metr_nitrite_ion_n'][v]
    sw['n_nitrates_in'][v] = sw['nitrate_ion'][v] * c['s_metr_nitrate_ion_n'][v]

    tp['r_anaerobic'][v] = tp['q_anaerobic'][v] / sw['q_h'][v]

    aar['s_acetate_in'][v] = sw['cod_in'][v] * c['k_acetate_cod'][v]

    prr['p_common'][v] = sw['p_po4_in'][v] * c['p_common_p_po4'][v]

    if tp['reagent'][v] == 2:
        cprr['delta_p_chemical'][v] = tp['d_me'][v] / 56 * 31 / cp['beta'][v]
        cprr['c_me_po4'][v] = cprr['delta_p_chemical'][v] / 31 * (56 + 31 + 4 * 16)
    elif tp['reagent'][v] == 1:
        cprr['delta_p_chemical'][v] = tp['d_me'][v] / 27 * 31 / cp['beta'][v]
        cprr['c_me_po4'][v] = cprr['delta_p_chemical'][v] / 31 * (27 + 31 + 4 * 16)

    axr['tkn'][v] = sw['n_ammonium_in'][v] * c['tkn_n_nh4'][v]
    axr['l_anoxide'][v] = sw['l_in'][v]     # TODO убрали вот это слагаемое. - aar['delta_l_anaerobic'][v]

    # axr['l_anoxide_diluted_out'][v] = 8.529
    # axr['l_anoxide_diluted_out'][v] = ((sw['l_in'][v] - axr['delta_l_anoxide'][v]))

    axr['x_b'][v] = c['cod_b'][v] * tp['a_i'][v] * (1 - tp['s'][v])
    axr['mu_max_d'][v] = c['mu_max_d_20'][v] * exp(c['hi_denitrification'][v] * (sw['temperature'][v] - 20))
    axr['b_d'][v] = c['b_d_20'][v] * exp(c['hi_denitrification'][v] * (sw['temperature'][v] - 20))
    axr['r_i'][v] = tp['q_return'][v] / sw['q_h'][v]

    nfsr['mu_max_a1'][v] = c['mu_max_a1_20'][v] * exp(c['hi_a1'][v] * (sw['temperature'][v] - 20))
    nfsr['b_a1'][v] = c['b_a1_20'][v] * exp(c['hi_a1'][v] * (sw['temperature'][v] - 20))

    nssr['mu_max_a2'][v] = c['mu_max_a2_20'][v] * exp(c['hi_a2'][v] * (sw['temperature'][v] - 20))
    nssr['b_a2'][v] = c['b_a2_20'][v] * exp(c['hi_a2'][v] * (sw['temperature'][v] - 20))

    nvcr['z_n'][v] = \
        (1 + c['phi_n'][v] * tp['a_i'][v]) * (tp['c_0'][v] + c['k_s_o2_a1'][v]) / c['ro_max_a1'][v] / \
        exp(c['hi_a1'][v] * (sw['temperature'][v] - 20)) / tp['c_0'][v] / tp['a_i'][v] / (1 - tp['s'][v])

    osor['z'][v] = \
        c['ro_max_bod'][v] * exp(c['hi_r'][v] * (sw['temperature'][v] - 20)) / \
        (1 + tp['a_i'][v] * c['phi_r'][v]) * tp['c_0'][v] / (tp['c_0'][v] + c['k_0'][v]) * \
        tp['a_i'][v] * (1 - tp['s'][v])

    ssr['q_ssa'][v] = sw['q_h'][v] / cp['f_tot'][v]
    ssr['a'][v] = 0.1 * tp['j_i'][v] * tp['a_i'][v]

    our['t_anaerobic'][v] = cp['w_anaerobic']['value'] / sw['q'][v] * 24
    our['t_anoxide'][v] = cp['w_anoxide'][v] / sw['q'][v] * 24
    our['t_aerobic'][v] = cp['w_aerobic']['value'] / sw['q'][v] * 24
    our['t_total'][v] = our['t_anaerobic'][v] + our['t_anoxide'][v] + our['t_aerobic'][v]
    our['r_common'][v] = (tp['q_nitrification'][v] + tp['q_return'][v]) / sw['q_h'][v]


if __name__ == '__main__':

    first_echelon()
    print(f"{round(sw['n_ammonium_in'][v], 1) :<10}{sw['n_ammonium_in'][d]}")
    print(f"{round(sw['n_nitrites_in'][v], 3) :<10}{sw['n_nitrites_in'][d]}")
    print(f"{round(sw['n_nitrates_in'][v], 2) :<10}{sw['n_nitrates_in'][d]}")
    print(f"{round(tp['r_anaerobic'][v], 2) :<10}{tp['r_anaerobic'][d]}")
    print(f"{round(aar['s_acetate_in'][v], 2) :<10}{aar['s_acetate_in'][d]}")
    print(f"{round(prr['p_common'][v], 1) :<10}{prr['p_common'][d]}")
    print(f"{round(cprr['delta_p_chemical'][v], 2) :<10}{cprr['delta_p_chemical'][d]}")
    print(f"{round(cprr['c_me_po4'][v], 2) :<10}{cprr['c_me_po4'][d]}")
    print(f"{round(axr['tkn'][v], 2) :<10}{axr['tkn'][d]}")
    print(f"{round(axr['l_anoxide'][v], 2) :<10}{axr['l_anoxide'][d]}")
    # print(f"{round(axr['l_anoxide_diluted_out'][v], 2) :<10}{axr['l_anoxide_diluted_out'][d]}")
    print(f"{round(axr['x_b'][v], 2) :<10}{axr['x_b'][d]}")
    print(f"{round(axr['mu_max_d'][v], 1) :<10}{axr['mu_max_d'][d]}")
    print(f"{round(axr['b_d'][v], 2) :<10}{axr['b_d'][d]}")
    print(f"{round(axr['r_i'][v], 1) :<10}{axr['r_i'][d]}")
    print(f"{round(nfsr['mu_max_a1'][v], 2) :<10}{nfsr['mu_max_a1'][d]}")
    print(f"{round(nfsr['b_a1'][v], 3) :<10}{nfsr['b_a1'][d]}")
    print(f"{round(nssr['mu_max_a2'][v], 2) :<10}{nssr['mu_max_a2'][d]}")
    print(f"{round(nssr['b_a2'][v], 3) :<10}{nssr['b_a2'][d]}")
    print(f"{round(nvcr['z_n'][v], 4) :<10}{nvcr['z_n'][d]}")
    print(f"{round(osor['z'][v], 2) :<10}{osor['z'][d]}")
    print(f"{round(ssr['q_ssa'][v], 2) :<10}{ssr['q_ssa'][d]}")
    print(f"{round(ssr['a'][v], 2) :<10}{ssr['a'][d]}")
    print(f"{round(our['t_anaerobic'][v], 2) :<10}{our['t_anaerobic'][d]}")
    print(f"{round(our['t_anoxide'][v], 2) :<10}{our['t_anoxide'][d]}")
    print(f"{round(our['t_aerobic'][v], 2) :<10}{our['t_aerobic'][d]}")
    print(f"{round(our['t_total'][v], 2) :<10}{our['t_total'][d]}")
    print(f"{round(our['r_common'][v], 2) :<10}{our['r_common'][d]}")
