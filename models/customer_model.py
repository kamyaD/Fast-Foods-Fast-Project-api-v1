# from flask import Flask
#
# app = Flask(__name__)
# customers = []
#
# class Customer():
#     self.customer_infomation = {}
#     self.customers = customers
#
#     def customer_register(self,fname,lname,ybirth,email,pw,pw_conf):
#
#         """ here we will take the customer  details and store them in
#         in cusomer_information dictionary then append the the details to the
#         # customet list before returning the user details """
#
#          self.customer_infomation['fname'] = fname
#          self.customer_infomation['lname'] = lname
#          self.customer_infomation['ybirth'] = ybirth
#          self.customer_infomation['email'] = email
#          self.customer_infomation['pw'] = pw
#          self.customer_infomation['pw_conf'] = pw_conf
#
#          customers.append(self.customer_infomation)
#          return self.customer_infomation
#
#
#     def customer_login(self,email,pw):
#         #check if customer has an account
#
#         for customer in customers:
#             if email == customer['email'] and pw == customer['pw']:
#                 return customer
#             else:
#                 return "wrong login credentials"
#
#
#