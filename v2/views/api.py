from flask import Flask, render_template, jsonify, request, session, flash, redirect, url_for, Blueprint
from views.api import *
import sys

import psycopg2

app = Flask(__name__)
api = Blueprint('api', __name__)


@api.route('/register', methods=['POST'])
def register():
        name = request.get_json()['name' ]
        email = request.get_json()['email']
        username = request.get_json()['username']
        password = request.get_json()['password']

        cursor.execute(
            "INSERT INTO user(user_name, user_email, user_pw, confirm_pw) VALUES(%s, %s, %s, %s)",
            (name,
             email,
             username,
             password))

        connection.commit()


        registered = 'Sucessfully registered you may now log in with your username and password'
        return jsonify ({ 'message': registered })


@app.route('/login', methods=['POST'])
def login():
    name = request.get_json()['name']
    password = request.get_json()['password']
    login_data = cur.execute(
        "SELECT * FROM user WHERE user_name = %s",
        [username])

    if result > 0:
        resuult = cur.fetchone()
        password = result['password']

        session['logged_in'] = True
            session['username'] = username
            access = 'Thanks for login in '
            return {'message': access}

        else:
            incorrect = 'Your login combination did not match please try again'
            return {'message': incorrect}
    else:
        incorrect = "The user name is incorrect please try again"
        return {'message': incorrect}

















app.register_blueprint(api, url_prefix='/api/v2')