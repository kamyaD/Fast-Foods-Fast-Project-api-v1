orders = []


class Orders():
    # Here we will manage and also store orders

    def __init__(self):
        self.orders = orders
        self.order_info = {}
    
    def delete_order():
        for order in orders:
            if order['name'] == name:
                orders.remove(order)

    def add_order(self,order_name,order_description):
        self.order_info['name'] == order_name
        self.order_info['order_description'] == order_description
        orders.append(self.order_info)
        return self.order_info
    
    def view_orders(self):
        if len(orders) == 0:
            return "There are no orders yet, please try again later"
        else:
            return orders
    
    def edit_order(self,name):
        for order in orders:
            if order['name'] == name:
                option = input("Enter n,d to change name or description of order respectively")
                if option == 'n':
                    new_order_name = input("Please enter a new order name")
                    order["name"] = new_order_name
                elif option == d:
                    new_description = input("Please enter a new desription")
                    order["description"] = new_description
                else:
                    return "Your have entered wrong input option"

            else:
                return "The order to change does not exist"
    
    def get_agiven_ordr(self, name):
        for order in orders:
            if order['name'] == name:
                return order
            else:
                return "The order you are looking for does not exist."

        

# database Post gree




        
    
