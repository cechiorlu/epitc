import numpy as np

def lagrange_interpolation(argx, argy, xp):
    # args argx, argy are lists while xp is a float data type
    # Use package from db_connect to get argx and argy
    x = np.array(argx, float)
    y = np.array(argy, float)

    yp = 0

    for xi, yi in zip(x, y):
        # lagrange interpolation from 4 data points (len of t and k)
        yp += yi * np.prod((xp - x[x != xi]) / (xi - x[x != xi]))

    return yp


def calculate_thickness(data):
    # hours = data.get('hours', 480)
    # This sets default hours to 480 hrs
    t1 = float(data['temp1'])
    t2 = float(data['temp2'])
    tm = (t1 + t2)/2

    
    # Unedited code


def calculate_insulation_cost():
    # 
    return

def calculate_energy_cost():
    # Calculated from heat flux (data['']), runtime(data['']) and fuel cost
    return

def calculate_energy_savings():
    # insulation_cost - energy_cost
    return