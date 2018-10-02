# import objects from the Flask model
from flask import Flask, render_template, jsonify, request, session, redirect, url_for, Blueprint

from ..models.connection import MyDatabase, User , Orders, Menu

api = Blueprint('api_v2', __name__)

orders = []
special = "[@_!#$%^&*()<>?/\\|}{~:]"


@api.route('/orders', methods=['POST'])  # Places a new Order
def addOrder():

    order_name = request.get_json()['order_name']
    customer_name = request.get_json()['customer_name']

    order = Orders(order_name, customer_name)

    order.place_order()

    return jsonify({"message":"order place sucessfully"})

@api.route('/orders', methods=['GET'])

def returnAll():
    all = Orders().all_orders()
    return  jsonify({"orders":[order.serialize() for order in all]})


@api.route('/menu', methods=['POST'])

def post_food():
    
    food_name = request.get_json()['food_name']
    food_desc = request.get_json()['food_desc']
    food_price = request.get_json()['food_price']
    

    food = Menu(food_name, food_desc, food_price)

    food.insert_to_menu()

    return jsonify({"message":"food created sucessfully"})


@api.route('/menu', methods=['GET'])

def returnMenu():
    all = Menu().all_menu()

    return  jsonify({"Menu":[menu.serialize() for menu in all]})



@api.route('/orders/<int:id>', methods=['GET'])
def getOrder(id):

    order = Orders().get_specific_order(id)
    if order:
        return jsonify({"order": order.serialize()})
       


@api.route('/orders/<int:name>', methods=['Delete'])  # Delete an order
def deleteOrder(name):
    for order in orders:
        if order['id'] == name:
            orders.remove(order)
    return jsonify({'orders': orders})

