from flask import Flask

app = Flask(__name__)
admins = []

class admin():
    self.admin_infomation = {}
    self.admins = admins

    def admin_register(self,fname,lname,ybirth,email,pw,pw_conf):

        """ here we will take the admin  details and store them in 
        in cusomer_information dictionary then append the the details to the 
        customet list before returning the user details """

         self.admin_infomation['fname'] = fname
         self.admin_infomation['lname'] = lname
         self.admin_infomation['ybirth'] = ybirth
         self.admin_infomation['email'] = email
         self.admin_infomation['pw'] = pw
         self.admin_infomation['pw_conf'] = pw_conf

         admins.append(self.admin_infomation)
         return self.admin_infomation
     

    def admin_login(self,email,pw):
        #check if admin has an account

        for admin in admins:
            if email == admin['email'] and pw == admin['pw']:
                return admin
            else:
                return "wrong login credentials" 


    