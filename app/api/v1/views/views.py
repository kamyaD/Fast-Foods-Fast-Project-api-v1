#import objects from the Flask model
from flask import Flask, render_template, jsonify, request,session,flash,redirect,url_for, Blueprint 
# from app.models.connection import MyDatabase


 #define app and telling flask that template folder is named v1
app = Flask(__name__)
api_v1 = Blueprint('api_v1', __name__)



orders=[]
special = "[@_!#$%^&*()<>?/\\|}{~:]"

# @api.route('/orders', methods=['GET']) #Testing the jsonify out put on a browser
# def getOrders():
#     return jsonify({'message' : 'Itworks!'})

@api_v1.route('/orders', methods=['POST']) # Places a new Order
def addOrder():
    order_from_user = request.get_json()
    order = {}
    #order['price']= order_from_user['price']
    order['name'] = order_from_user['name']
    order['status']= "pending"
    if not order['name'] or len(order['name'].strip()) == 0:
        return jsonify({"message": "order name can't be blank"}), 401
    elif order['name'] in special:
        return jsonify({"message": "order name can't be Special character"}), 401
    order['id']=len(orders)+1
    return orders
    return jsonify({'orders' : orders})
    

@api_v1.route('/orders', methods=['GET']) # GET api_v1 that gets all orders
def returnAll():
    return jsonify({'orders': orders})


@api_v1.route('/orders/<int:name>', methods=['PUT']) # Update the status of an order
def editOrder(name):
    for order in orders:
        if order['id']== name:
            order['name']=request.get_json()['name']
            order['price']=request.get_json()['price']
            order['status']=request.get_json()['status']
       
        return jsonify({'order' : orders})


@api_v1.route('/orders/<int:name>', methods=['GET']) # fetch Specific order
def returnOne(name):
    for  order in orders:
        if order['id']== name:
            return jsonify(order)
    return jsonify({"message":"Iten doesnt exist"})


@api_v1.route('/orders/<int:name>', methods=['Delete']) # Delete an order
def deleteOrder(name):
    for order in orders:
        if order['id']== name:
            orders.remove(order)
    return jsonify({'orders': orders})