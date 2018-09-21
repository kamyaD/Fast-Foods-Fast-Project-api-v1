#import objects from the Flask model
from flask import Flask, render_template, jsonify, request,session,flash,redirect,url_for 


app = Flask(__name__, template_folder='v1') #define app and telling flask that template folder is named v1

orders=[]

@app.route('/api/v1/order', methods=['GET']) #Testing the jsonify out put on a browser
def getOrders():
    return jsonify({'message' : 'Itworks!'})


@app.route('/api/v1/all_orders', methods=['POST']) # Places a new Order
def addOrder():
    order_from_user = request.get_json()
    order = dict()
    order['price']= order_from_user['price']
    order['name']= order_from_user['name']
    order['id']=len(orders)+1
    orders.append(order)
    return jsonify({'orders' : orders})


@app.route('/api/v1/all_orders', methods=['GET']) # GET API that gets all orders
def returnAll():
    return jsonify({'orders': orders})


@app.route('/api/v1/all_orders/<int:name>', methods=['PUT']) # Update the status of an order
def editOrder(name):
    for order in orders:
        if order['id']== name:
            order['name']=request.get_json()['name']
            order['price']=request.get_json()['price']

    return jsonify({'order' : orders})


@app.route('/api/v1/all_orders/<int:name>', methods=['GET']) # fetch Specific order
def returnOne(name):
    for order in orders:
        if order['id']== name:
            return jsonify(order)
    return jsonify({"message":"Iten doesnt exist"})


@app.route('/api/v1/all_orders/<int:name>', methods=['Delete']) # Delete an order
def deleteOrder(name):
    for i, order in enumerate(orders):
        if order['id']== name:
            del orders[i]
    return jsonify({'orders': orders})

if __name__ == '__main__':
    app.run(debug=False)
