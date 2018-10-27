import os

class Config():
    FLASK_APP='run.py'


class ProductionConfig(Config):
    ENV = "production"

    DATABASE_URL = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    ENV = "development"

    DATABASE_URL = "host='localhost' dbname='orders' user='postgres' password='admin'"

class TestingConfig(Config):
    ENV = "development"

    DATABASE_URL = "host='localhost' dbname='orders_test' user='postgres' password='admin'"
    DATABASE_CREATE_URL = "host='localhost' user='postgres' password='admin'"

    DB_NAME = "orders_test"

app_config = {
    'production':ProductionConfig,
    'development':DevelopmentConfig,
    'test':TestingConfig
}