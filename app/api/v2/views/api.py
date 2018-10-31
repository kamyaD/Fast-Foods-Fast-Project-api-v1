# import objects from the Flask model
from flask import (Blueprint, Flask, jsonify, make_response, redirect,
                   render_template, request, session, url_for, abort)
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import datetime
from ..models.connection import Menu, MyDatabase, Orders, User
from flask_cors import CORS

import re


api = Blueprint('api_v2', __name__)
CORS(api)
orders = []
special = "[@_!#$%^&*()<>?/\\|}{~:]"


def empty_input(name):
    if not name or name.strip() == "":
        abort(400)
        return jsonify({"message": " name can't be blank"}), 401


@api.route('/orders', methods=['POST'])  # Places a new Order
@jwt_required
def addOrder():
    identity = get_jwt_identity()
    print(request.get_json())
    order_name = request.get_json()['order']
    empty_input(order_name)
    if not Validations().valid_name(order_name):
        return jsonify({"message": "enter valid order name"}), 400
    customer_name = request.get_json()['customer']
    if not Validations().valid_name(customer_name):
        return jsonify({"message": "enter valid customer Name "}), 400
    order = Orders(order_name, customer_name)
    order.place_order()
    return jsonify({"message": "order place sucessfully"})


@api.route('/orders', methods=['GET'])
@jwt_required
def returnAll():
    all = Orders().all_orders()

    if all:
        return jsonify({"orders": [order.serialize() for order in all]})
    return jsonify({"message": "Sorry the order list is empty"})


@api.route('/menu', methods=['POST'])
@jwt_required
def post_food():

    food_name = request.get_json()['food_name']
    if not Validations().valid_name(food_name):
        return jsonify({"message": "enter valid food name"}), 400
    food_desc = request.get_json()['food_desc']
    if not Validations().valid_name(food_desc):
        return jsonify({"message": "enter valid food description"}), 400
    food_price = request.get_json()['food_price']
    food = Menu(food_name, food_desc, food_price)
    food.insert_to_menu()

    return jsonify({"message": "food created sucessfully"})


@api.route('/menu', methods=['GET'])
def returnMenu():
    all = Menu().all_menu()
    if all:
        return jsonify({"menu": [menu.serialize() for menu in all]})
    return jsonify({"message": "Sorry the menu  list is empty"})


@api.route('/orders/<int:id>', methods=['GET'])
@jwt_required
def getOrder(id):
    order = Orders().get_specific_order(id)
    if order:
        return jsonify({"order": order.serialize()})


# user registration
@api.route('/user', methods=['POST'])
def register():
    print(request.get_json())
    name = request.get_json()['name']
    email = request.get_json()['email']
    password = request.get_json()['password']

    user_found = User().get_user_by_name(name)

    if user_found:
        return jsonify({"message": "user already exists"}), 400

    if not Validations().valid_name(name):
        return jsonify({"message": "enter valid username"}), 400

    if not Validations().valid_email(email):
        return jsonify({"message": "enter valid email"}), 400

    if not Validations().valid_password(password):
        return jsonify({"message": "enter valid password"}), 400

    register = User(name, email, password, 1)
    register.insert_to_user()
    return jsonify({"message": "registration successful"}), 201


@api.route('/admin', methods=['POST'])
def admin():
    name = request.get_json()['name']
    email = request.get_json()['email']
    password = request.get_json()['password']

    user_found = User().get_user_by_name(name)

    if user_found:
        return jsonify({"message": "user already exists"}), 400

    if not Validations().valid_name(name):
        return jsonify({"message": "enter valid username"}), 400

    if not Validations().valid_email(email):
        return jsonify({"message": "enter valid email"}), 400

    if not Validations().valid_password(password):
        return jsonify({"message": "enter valid password"}), 400

    register = User(name, email, password, 2)
    register.insert_to_user()
    return jsonify({"message": "registration successful"}), 201


@api.route('/login', methods=['POST'])
def login():
    name = request.get_json()['name']
    password_user = request.get_json()['password']

    if not Validations().valid_name(name):
        return jsonify({"message": "enter valid username"}), 400

    user_found = User().get_user_by_name(name)

    print(user_found)

    if user_found:

        if password_user == user_found.password:
            data = {
                'logged_in': True,
                'name': name,
                "role": user_found.role,
                'token': create_access_token({
                    "user": name,



                }, expires_delta=datetime.timedelta(minutes=30))
            }

            return make_response(jsonify(
                {
                    'message': "Success",
                    'data': data
                }), 200)
    return jsonify({"message": "User not found"}), 404

# Update the status of an order


@api.route('/orders/<int:order_id>', methods=['PUT'])
@jwt_required
def editOrder(order_id):
    order = Orders().get_specific_order(order_id)

    if order:
        order.order_status = request.get_json()['status']
        order.update_order_status()

        return make_response(
            jsonify({
                'message': 'Order status successully updated!'
            }), 200
        )

    return make_response(
        jsonify({
                'message': 'Order not found!'
                }), 404
    )


@api.route('/orders/<string:name>', methods=['GET'])
def userHistry(name):
    user_histry = Orders(customer_name=name).get_user_order_histry()

    if user_histry:
        return make_response(
            jsonify({
                "user_histry": user_histry
            })
        )
    else:
        return make_response(
            jsonify({"message": "The customer order does not exist"})
        )


class Validations:

    def valid_email(self, email):
        return re.match(r"^[^@]+@[^@]+\.[^@]+$", email)

    def valid_name(self, name):
        return re.match("^[a-zA-Z]+$", name)

    def valid_password(self, password):
        return re.match("^[a-zA-Z]+$", password)
