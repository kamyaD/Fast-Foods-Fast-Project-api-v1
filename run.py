from flask import Flask
from v2.views.api import app

if __name__ == '__main__':
    app.run(debug=True)
