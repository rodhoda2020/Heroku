from db import db


# This will create a mapping between the database and
# and the objects in this class
class ItemModel(db.Model):
    __tablename__ = 'items'

    # Even though we do not have an ID for items, we are
    # going to start using one since they are very useful
    id = db.Column(db.Integer, primary_key=True)

    # The 80 will limit the size of the username
    name = db.Column(db.String(80))

    # The precision indicates two decimal places
    price = db.Column(db.Float(precision=2))


    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    # These properties will be saved into the database

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        # This comes from SQLAlchemy
        # We want to build a query and filter it by name
        # The first will limit to the first row

    def save_to_db(self):
        db.session.add(self)
        # The session is a collection of objects
        # In this case we are adding the self variables
        db.session.commit()

        # This method will update and insert

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()