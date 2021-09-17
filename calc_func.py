import math

import numpy as np


def lagrange_interpolation(argx, argy, xp):
    # args argx, argy are lists while xp is a float data type
    # argx is temperature
    # argy is conductivity
    # xp is tm
    # returns thermal conductivity
    x = np.array(argx, float)
    y = np.array(argy, float)

    yp = 0

    for xi, yi in zip(x, y):
        # lagrange interpolation from 4 data points (len of t and k)
        yp += yi * np.prod((xp - x[x != xi]) / (xi - x[x != xi]))

    return yp


thermal_conductivity_table = {

    'mineral_fiber_1': {
        'temp': [297, 366.5, 477.6, 588.7],
        'conductivity': [0.0346, 0.0447, 0.0735, 0.09224],
        'max_temp': 727.6,
        'recycle_content': 0.28
    },

    'mineral_fiber_235': {
        'temp': [297, 366.5, 477.6, 588.7],
        'conductivity': [0.0346, 0.0447, 0.06486, 0.0937],
        'max_temp': 922,
        'recycle_content': 0.28
    },

    'calcium_silicate': {
        'temp': [366.5, 477.6, 588.7],
        'conductivity': [0.06486, 0.7927, 0.09513],
        'max_temp': 922,
        'recycle_content': 0
    },

    'cellular_glass': {
        'temp': [297, 366.5, 477.6],
        'conductivity': [0.049, 0.06198, 0.0908],
        'max_temp': 699.8
    }

}


def calculate_heat_transfer_rate(data, r2):
    # This sets default hours to 480 hrs
    hours = data.get('hours', 480)

    # Get average temperature for conductivity
    t1 = float(data['temp1'])
    t2 = float(data['temp2'])
    tm = t1 + t2 / 2

    # Get data from thermal conductivity table for selected insulation material
    x = thermal_conductivity_table['cellular_glass']['temp']
    y = thermal_conductivity_table['cellular_glass']['conductivity']

    # Thermal conductivity
    k = lagrange_interpolation(x, y, tm)

    # q = 2 * np.pi * k * data['pipe_length'] * (t1 - t2)/np.log(r2/r1)
    # return q


def calculate_insulation_cost(data):
    #
    pipe_length = float(data['pipe_length'])
    installation_cost = data.get('cost_per_length', 2000)
    service_cost = pipe_length * installation_cost
    material_cost = data['cost_per_volume'] * np.pi * pipe_length
    return


def calculate_heat_loss_costs():
    # Calculated from heat flux (data['']), runtime(data['']) and fuel cost

    return


def calculate_energy_savings():
    # insulation_cost - energy_cost
    return
