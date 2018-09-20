#import objects from the Flask model
from flask import Flask, render_template, jsonify, request,session,flash,redirect,url_for 

# local imports
from app.customer_model import customer
from app.order_model import orders
from app.admin_model import admin


app = Flask(__name__) # define app 

@app.route('/api/v1/order', methods=['GET']) #Testing the jsonify out put on a browser
def getOrders():
    return jsonify({'message' : 'Itworks!'})

@app.route('/api/v1/register/', method=['POST'])

    
@app.route('/api/v1/all_orders', methods=['POST']) # Places a new Order
def addOrder():
    order = request.get_json('name')
    orders.append(order)
    return jsonify({'orders' : orders})


@app.route('/api/v1/all_orders', methods=['GET']) # GET API that gets all orders
def returnAll():
    return jsonify({'orders': orders})


@app.route('/api/v1/all_orders/<string:name>', methods=['PUT']) # Update the status of an order
def editOrder(name):
    ords=[order for order in orders if order['name']== name]
    ords[0]['name'] = request.get_json(['name'])
    return jsonify({'order' : ords[0]})


@app.route('/api/v1/all_orders/<string:name>', methods=['GET']) # fetch Specific order
def returnOne(name):
    ords=[order for order in orders if order['name']== name]
    return jsonify({'order' : ords[0]})

@app.route('/api/v1/all_orders/<string:name>', methods=['Delete']) # Delete an order
def deleteOrder(name):
    delOrder=[order for order in orders if order['name']== name]
    orders.remove(delOrder[0])
    return jsonify({'orders': orders})

if __name__ == '__main__':
    app.run(debug=False)
