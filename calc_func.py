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
        'recycle_content': 0.28,
        'design_life': 20,
    },

    'mineral_fiber_235': {
        'temp': [297, 366.5, 477.6, 588.7],
        'conductivity': [0.0346, 0.0447, 0.06486, 0.0937],
        'max_temp': 922,
        'recycle_content': 0.28,
        'design_life': 20,
    },

    'calcium_silicate': {
        'temp': [366.5, 477.6, 588.7],
        'conductivity': [0.06486, 0.7927, 0.09513],
        'max_temp': 922,
        'recycle_content': 0,
        'design_life': 18,
    },

    'cellular_glass': {
        'temp': [297, 366.5, 477.6],
        'conductivity': [0.049, 0.06198, 0.0908],
        'max_temp': 699.8,
        'design_life': 16,
        'recycle_content': 0.19,
    }

}


def calculate_heat_transfer_rate(data, x, c):
    # Get average temperature for conductivity
    t1 = float(data['temp1']) + 273
    t2 = float(data['temp2']) + 273
    tm = t1 + c / 2
    l = float(data['pipe_length'])

    # Get data from thermal conductivity table for selected insulation material
    a = thermal_conductivity_table[data['insulation_mat']]['temp']
    b = thermal_conductivity_table[data['insulation_mat']]['conductivity']

    # Thermal conductivity
    k = lagrange_interpolation(a, b, tm)

    # Pipe radius
    r1 = float(data['pipe_size']) / 2

    q = 2 * np.pi * k * l * (t1 - c) / np.log(x / r1)
    return q


def calculate_insulation_cost(data, x):
    r1 = float(data['pipe_size']) / 2
    pipe_length = float(data['pipe_length'])
    ins_mat = thermal_conductivity_table[data['insulation_mat']]
    installation_cost = float(data['cost_per_length'])
    service_cost = pipe_length * installation_cost
    material_cost = float(data['cost_per_volume']) * np.pi * pipe_length * (x ** 2 - r1 ** 2)

    return (installation_cost + material_cost * (1 - ins_mat['recycle_content'])) / ins_mat['design_life']


def calculate_heat_loss_cost(data, x, c):
    runtime = float(data['runtime']) * 52 * 60 * 60
    steam_cost = float(data['steam_cost'])

    total_heat_lost = calculate_heat_transfer_rate(data, x, c) * runtime
    amount_of_steam = total_heat_lost * 0.00084 / 1000

    return amount_of_steam * steam_cost


def total_costs(data, x, c):
    return calculate_heat_loss_cost(data, x, c) + calculate_insulation_cost(data, x)
