from v3.models.connection import MyDatabase
from v3.views.api import app


if __name__ == "__main__":
    # create tables
    MyDatabase.create_user(MyDatabase)
    MyDatabase.create_Orders(MyDatabase)
    MyDatabase.create_menu(MyDatabase)

    # drop tables





