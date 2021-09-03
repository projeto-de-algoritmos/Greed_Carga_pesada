from flask import Blueprint, request, json, Response

from Models.Charge import Charge
from Models.ChargeList import ChargeList

charge_view = Blueprint("", __name__)

charge_list = []

def prepare_data(charge_list) -> dict:
    processed_list = {}
    for i in charge_list:
        processed_list[i.get_name()] = [i.get_weight(),i.get_value()]
    return processed_list

@charge_view.route('/charge/', methods=["GET", "POST"])
def charge_route():
    if request.method == "POST":
        data = request.get_json()
        print(data.keys())
        if 'data' not in data.keys() or 'pesoMax' not in data.keys():
            response = Response(
                    status=400,
                    mimetype='charge_viewlication/json'
                )
            return response
        else: 
            charge_list = ChargeList(data['data'], data['pesoMax']['pesoMax'])
            result = {'data': charge_list.knapsack()}
            response = Response(
                    response=json.dumps(result),
                    status=200,
                    mimetype='charge_viewlication/json'
                )
            return response
