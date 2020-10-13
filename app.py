import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.item import Item, Items
from security import authenticate, identity
from resources.user  import UserRegister
from db import db
from resources.store import Store, StoreList



app = Flask(__name__)
# SQLAlchemy will read the data.db file
# The os.environ.get() will first try to look for the first variable, and if it fails, it goes to
# the second variable and find it
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)




jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)

