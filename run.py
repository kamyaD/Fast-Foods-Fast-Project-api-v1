from flask import Flask
from app import create_app
import os

app = create_app('development')

if __name__ == '__main__':
    app.run(debug=True)
