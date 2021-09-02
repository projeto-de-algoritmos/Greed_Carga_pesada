from flask import Flask, json, request

from knapsack import Charge, bubbleSort_charge, knapsack

app = Flask(__name__)

charge_list = []
keys = []

def prepare_data(charge_list) -> dict:
    processed_list = {}
    for i in charge_list:
        processed_list[i.get_name()] = [i.get_weight(),i.get_value()]
    return processed_list

@app.route('/charge/', methods=["GET", "POST", "DELETE"])
def charge_route():
    if request.method == "GET":
        data = { 'charge_list': prepare_data(charge_list) }
        response = app.response_class(
                response=json.dumps(data),
                status=200,
                mimetype='application/json'
            )
        return response
    elif request.method == "POST":
        data = request.args.to_dict()
        if 'name' not in data.keys() or 'weight' not in data.keys() or 'name' not in data.keys():
            response = app.response_class(
                    status=400,
                    mimetype='application/json'
                )
            return response
        elif data['name'] in keys:
            response = app.response_class(
                    status=400,
                    mimetype='application/json'
                )
            return response
        else: 
            new_charge = Charge(data['name'], data['weight'], data['value'])
            charge_list.append(new_charge)
            keys.append(data['name'])
            response = app.response_class(
                    response=json.dumps(data),
                    status=200,
                    mimetype='application/json'
                )
            return response
    elif request.method == "DELETE":
        data = request.args.to_dict()
        if 'name' not in data.keys():
            response = app.response_class(
                    status=400,
                    mimetype='application/json'
                )
            return response
        else:
            flag = True
            for index, charge in enumerate(charge_list):
                if charge.get_name() == data['name']:
                    charge_list.pop(index)
                    flag = False
            if flag:
                response = app.response_class(
                        status=404,
                        mimetype='application/json'
                    )
                return response
            else:
                response = app.response_class(
                        status=200,
                        mimetype='application/json'
                    )
                return response

app.run(debug=True)
