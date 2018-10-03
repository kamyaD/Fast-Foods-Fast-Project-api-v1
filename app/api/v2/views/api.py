# import objects from the Flask model
from flask import (Blueprint, Flask, jsonify, make_response, redirect,
                   render_template, request, session, url_for)
from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity

from ..models.connection import Menu, MyDatabase, Orders, User

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

    if all:
        return  jsonify({"orders":[order.serialize() for order in all]})    
    return jsonify({"message":"Sorry the order list is empty"})



@api.route('/menu', methods=['POST'])
@jwt_required
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

    return  jsonify({"menu":[menu.serialize() for menu in all]})
 return jsonify({"message":"Sorry the menu  list is empty"})





@api.route('/orders/<int:id>', methods=['GET'])
def getOrder(id):

    order = Orders().get_specific_order(id)
    if order:
        return jsonify({"order": order.serialize()})
       




# user registration
@api.route('/user', methods=['POST']) 
def register():
    name = request.get_json()['name' ]
    email = request.get_json()['email']
    password = request.get_json()['password']
    register=User(name,email,password)
    register.insert_to_user()
    return jsonify({"message":"registration successful"})

@api.route('/login', methods=['POST']) 
def login():
    name = request.get_json()['name']
    password_user = request.get_json()['password']

    login_data = User()
    user_found = login_data.get_user_by_name(name)
    

    if user_found:

        if password_user==user_found.password:
            data = {
                'logged_in':True,
                'name':name,
                'token': create_access_token(name)
            }

            return make_response(jsonify(
                {
                'message': "Success",
                "data":data
                }),200) 

@api.route('/orders/<int:name>', methods=['PUT']) # Update the status of an order
def editOrder(name):
    for order in orders:
        if order['id']== name:
            order['status']=request.get_json()['status']
       