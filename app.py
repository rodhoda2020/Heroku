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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
# This is the decorator that will run the method below it
# before the first request.
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)

