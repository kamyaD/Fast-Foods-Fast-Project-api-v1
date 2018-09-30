from flask import Flask, render_template, jsonify, request, session, flash, redirect, url_for, Blueprint
from views.api import *
import sys

import psycopg2

app = Flask(__name__)
api = Blueprint('api', __name__)

# user registration
@api.route('/register', methods=['POST'])
def register():
        name = request.get_json()['name' ]
        email = request.get_json()['email']
        username = request.get_json()['username']
        password = request.get_json()['password']

        cursor.execute(
            "INSERT INTO user(user_name, user_email, user_pw, confirm_pw) VALUES(%s, %s, %s, %s)",
            (name,
             email,
             username,
             password))

        connection.commit()


        registered = 'Sucessfully registered you may now log in with your username and password'
        return jsonify ({ 'message': registered })

# user login
@app.route('/login', methods=['POST'])
def login():
    name = request.get_json()['name']
    password = request.get_json()['password']
    login_data = cursor.execute(
        "SELECT * FROM user WHERE user_name = %s",
        [username])

    if result > 0:
        resuult = cur.fetchone()
        password = result['password']

        session['logged_in'] = True
            session['username'] = username
            access = 'Thanks for login in '
            return {'message': access}

        else:
            incorrect = 'Your login combination did not match please try again'
            return {'message': incorrect}
    else:
        incorrect = "The user name is incorrect please try again"
        return {'message': incorrect}

# Placing an order
@api.route('/orders', methods=['POST'])
def addOrder():
    order['name'] = order_from_user['name']
    customer['customer_id'] = id_from_user['id']
    order['status']= "pending"
    if not order['name'] or len(order['name'].strip()) == 0:
        return jsonify({"message": "order name can't be blank"}), 401
    elif order['name'] in special:
        return jsonify({"message": "order name can't be Special character"}), 401
    order['id']=len(orders)+1

    if order['name'] and customer['customer_id']:
        cursor.execute("INSERT INTO orders(order_name,order_status,customer_id) VALUES(%s,%s) "),
        (order['name'] ,
         order['status'],
         customer['customer_id'])
        connection.commit()

        responce="Your order has been successfuly created"
        return jsonify({"message":responce})
    else:
        error_message= "Incorrect order, please try again"
        return jsonify({"message": error_message})

# Get the order histry of a user
@api.route('/orders/<int:name>', methods=['GET']) # fetch Specific order
def returnOne(name):
    for  order in orders:
        if order['id']== name:
            order=cursor.execute("SELECT * FROM orders WHERE customer_id=customer_id")
            connection.commit()
            return jsonify(order)
        else:
            return jsonify({"message":"Item doesnt exist"})

# Get all orders:
@api.route('/orders', methods=['GET']) # GET API that gets all orders
def returnAll():
    all =cursor.execute( "SELECT * FROM orders")
    connection.commit()
    return jsonify({'orders': all})


@api.route('/orders/<int:name>', methods=['PUT']) # Update the status of an order
def editOrder(name):
    for order in orders:
        if order['id']== name:
            order['name']=request.get_json()['name']
            order['price']=request.get_json()['price']
            order['status']=request.get_json()['status']
            cursor.execute("INSERT INTO orders(order_status) VALUES(%s) WHERE order_name=name   "),
            (order['name'],
             order['status'],
             customer['customer_id'])
            connection.commit()

# GET API that gets all orders
@api.route('/menu', methods=['GET'])
def returnAll():
    menu =cursor.execute( "SELECT * FROM menu")
    connection.commit()
    return jsonify({'orders': menu})

# Add a meal option to a menu
@api.route('/menu/<int:name>', methods=['PUT'])
def editmenu(name):
    for item in menu:
        if item['id']== name:
            item['name']=request.get_json()['name']
            item['description']=request.get_json()['description']
            item['price']=request.get_json()['price']
            cursor.execute("INSERT INTO menu(item_name,item_description,item_price) VALUES(%s,%s,%s) WHERE item_name=item_name   "),
            (item['name'],
             item['description'],
             item['price'])
            connection.commit()



































app.register_blueprint(api, url_prefix='/api/v2')