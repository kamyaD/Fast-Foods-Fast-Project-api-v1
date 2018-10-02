from flask import Flask
from app import create_app
import os
from app.api.v2.models.connection import MyDatabase

app = create_app('development')

@app.before_first_request
def init_db():
    db = MyDatabase()

    db.create_user()
    db.create_Orders()
    db.create_menu()

if __name__ == '__main__':
    app.run(debug=True)
