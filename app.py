#import objects from the Flask model
from flask import Flask, render_template, jsonify, request,session,flash,redirect,url_for 

app = Flask(__name__, template_folder='v1') #define app and telling flask that template folder is named v1
orders = [{'name':'coffee'}, {'name':'Beaf'},{'name' : 'Milk'}] # Making a Dictionary of orders that is to be used to test the code

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

if __name__ == '__main__':
    app.run(debug=False)
