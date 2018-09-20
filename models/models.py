from flask import Flask

app = Flask(__name__)
users = []
login = []
orders = []

class User():


    def __init__(self,firstName,lastName,yearBirth,email,passWord):   
        self.firstName = firstName
        self.lastName = lastName
        self.yearBirth = yearBirth
        self.email = email
        self.passWord = passWord

    def firstName(self):
        fname = self.firstName.split[0]
        return fname

    def lastName(self):
        lname = self.lastNamesplit[1]
        return lname

    def yearBirth(self):
        yearbirth = self.yearBirth
        return yearbirth

    def email():
        email = self.email
        return email

    def passWord():
        password = self.passWord



class login(User):

    def __init__(self,userName):
        self.userName = userName
        self.passWord = User.passWord()
    
    def userName():
        username = self.userName
        return username
    
    def passWord():
        password = self.passWord
        return password

class orders():
    
    def __init__(self,oirderName,orderDescription,odrerAccepted,odrerDeclined,odrerComplete):
        self.orderName = ordername
        self.orderDescription = description
        self.odrerAccepted = accepted
        self.odrerDeclined = declined
        self.odrerComplete = complete

    def orderName():
        ondername = self.orderName
        return ondername

    def orderDescription():
        description = self.orderDescription
        return description
    
    def odrerAccepted():
        accepted = self.odrerAccepted
        return accepted

    def odrerDeclined():
        declined = self.odrerDeclined
        return declined
    
    def orderComplete():
        complete = self.odrerComplete
        return complete




    




