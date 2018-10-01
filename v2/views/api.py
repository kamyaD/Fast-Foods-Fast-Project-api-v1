# import objects from the Flask model
from flask import Flask, render_template, jsonify, request, session, redirect, url_for, Blueprint

from ..models.connection import MyDatabase, User , Orders, Menu


app = Flask(__name__)
api = Blueprint('api', __name__)

orders = []
special = "[@_!#$%^&*()<>?/\\|}{~:]"


@api.route('/orders', methods=['POST'])  # Places a new Order
def addOrder():

    order_name = request.get_json()['order_name']
    customer_name = request.get_json()['customer_name']

    order = Orders(order_name, customer_name)

    #print(order.order_name)

    order.place_order()

@api.route('/orders', methods=['GET'])

def returnAll():
    all = Orders().all_orders()
    return  jsonify({"orders":[order.serialize() for order in all]})

@api.route('/orders/<int:name>', methods=['PUT'])
def editOrder(name):
    for order in orders:
        if order['id'] == name:
            order['name'] = request.get_json()['name']
            order['price'] = request.get_json()['price']
            order['status'] = request.get_json()['status']

        return jsonify({'order': orders})



@api.route('/orders/<int:name>', methods=['GET'])  # fetch Specific order
def returnOne(name):
    for order in orders:
        if order['id'] == name:
            return jsonify(order)
    return jsonify({"message": "Item doesnt exist"})


@api.route('/orders/<int:name>', methods=['Delete'])  # Delete an order
def deleteOrder(name):
    for order in orders:
        if order['id'] == name:
            orders.remove(order)
    return jsonify({'orders': orders})


app.register_blueprint(api, url_prefix='/api/v2')