from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import calc_func as calc


@app.route('/',  methods=["GET", "POST"])
def serve_app():
    # check the request method to ensure the handling of POST request only
    if request.method == "POST":
        # store form values

        input_val = {
            'temp2': request.form['temp2'],
            'temp1': request.form['temp1'],
            'flux_density': request.form['flux_density'],
            'pipe_length': request.form['pipe_length'],
            'pipe_size': request.form['pipe_size'],
            'insulation_mat': request.form['insulation_mat'],
            'runtime': request.form['runtime'],
        }
        print(input_val)
    return render_template('index.html')
    # return render_template('index.html', var=input_val)

# @app.route('/calculate',  methods=["GET", "POST"])
# def calculate(var=None):
#     # check the request method to ensure the handling of POST request only
#     if request.method == "POST":
#         # store form values
#
#         input_val = {
#             'temp2': request.form['temp2'],
#             'temp1': request.form['temp1'],
#             'flux_density': request.form['flux_density'],
#             'pipe_length': request.form['pipe_length'],
#             'pipe_size': request.form['pipe_size'],
#             'insulation_mat': request.form['insulation_mat'],
#             'runtime': request.form['runtime'],
#         }
#     return render_template('index.html', temp1=input_val['temp1'])
