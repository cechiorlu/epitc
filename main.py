from flask import Flask, render_template, request
import scipy.optimize as opt
import numpy as np


app = Flask(__name__)
import calc_func as calc


@app.route('/', methods=["GET", "POST"])
def serve_app():
    return render_template('index.html')


@app.route('/calculate', methods=["GET", "POST"])
def calculate():
    # check the request method to ensure the handling of POST request only
    if request.method == "POST":
        # store form values

        input_val = {
            'temp2': request.form['temp2'],
            'temp1': request.form['temp1'],
            'steam_cost': request.form['steam_cost'],
            'pipe_length': request.form['pipe_length'],
            'pipe_size': request.form['pipe_size'],
            'insulation_mat': request.form['insulation_mat'],
            'runtime': request.form['runtime'],
            'cost_per_length': request.form['cost_per_length'],
            'cost_per_volume': request.form['cost_per_volume']
        }

        max_temp = float(input_val['temp2']) + 273
        pipe_size = float(input_val['pipe_size'])/2

        objective_function = lambda x: calc.total_costs(input_val, x[0], x[1])
        constraint1 = ({'type': 'ineq', 'fun': lambda x: np.array(max_temp - x[1])})
        constraint2 = ({'type': 'ineq', 'fun': lambda x: np.array(x[1] - 303)})

        results = opt.minimize(objective_function, x0=[3.0, max_temp-10], method='trust-constr', constraints=[constraint1, constraint2], options={'disp': True, 'xtol': 1e-08, 'gtol': 1e-08, 'barrier_tol': 1e-08, 'maxiter': 1100})
        thickness = results['x'][0] - pipe_size

        return render_template('calculate.html', results=results, thickness=thickness)
