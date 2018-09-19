function histry(){
    alert("Thank you for ordering at Fast Foods Fast: \n Your order is  "+document.order_form.order.value+" \n \n You will be served shortly !");
}


def addOne():
    order = {'name' : request.json['name']}

    orders.append(order)
    return jsonify({'orders' : orders})