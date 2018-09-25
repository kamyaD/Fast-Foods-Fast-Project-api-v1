#import objects from the Flask model
from flask import Flask, render_template, jsonify, request,session,flash,redirect,url_for, Blueprint 

app = Flask(__name__) #define app and telling flask that template folder is named v1
api = Blueprint('api', __name__)


orders=[]
special = "[@_!#$%^&*()<>?/\|}{~:]"

@api.route('/orders', methods=['GET']) #Testing the jsonify out put on a browser
def getOrders():
    return jsonify({'message' : 'Itworks!'})

@api.route('/orders_post', methods=['POST']) # Places a new Order
def addOrder():
    order_from_user = request.get_json()
    order = dict()
    order['price']= order_from_user['price']
    order['name'] = order_from_user['name']
    if not order['name'] or len(order['name'].strip()) == 0:
        return jsonify({"message": "order name can't be blank"}), 401
    elif order['name'] in special:
        return jsonify({"message": "order name can't be Special character"}), 401
    order['id']=len(orders)+1
    orders.append(order)
    return jsonify({'orders' : orders})
    

@api.route('/orders_all', methods=['GET']) # GET API that gets all orders
def returnAll():
    return jsonify({'orders': orders})


@api.route('/orders_put/<int:name>', methods=['PUT']) # Update the status of an order
def editOrder(name):
    for i, order in enumerate(orders):
        if order['id']== name:
            order['name']=request.get_json()['name']
            order['price']=request.get_json()['price']

    return jsonify({'order' : orders})


@api.route('/orders_get/<int:name>', methods=['GET']) # fetch Specific order
def returnOne(name):
    for i, order in enumerate(orders):
        if order['id']== name:
            return jsonify(order)
    return jsonify({"message":"Iten doesnt exist"})


@api.route('/orders_del/<int:name>', methods=['Delete']) # Delete an order
def deleteOrder(name):
    for i, order in enumerate(orders):
        if order['id']== name:
            del orders[i]
    return jsonify({'orders': orders})

app.register_blueprint(api, url_prefix='/api/v1')