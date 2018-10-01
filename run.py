from flask import Flask
from v3.views.api import app

if __name__ == '__main__':
    app.run(debug=True)
