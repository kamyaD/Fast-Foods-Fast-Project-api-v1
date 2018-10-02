from app.api.v2.views.api import api
from app.api.v1.views.views import api_v1
from flask import Flask

from instance.config import app_config

def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    app.register_blueprint(api, url_prefix='/api/v2')

    return app
