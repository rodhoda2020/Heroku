from db import db


# This will create a mapping between the database and
# and the objects in this class
class StoreModel(db.Model):
    __tablename__ = 'stores'

    # Even though we do not have an ID for items, we are
    # going to start using one since they are very useful
    id = db.Column(db.Integer, primary_key=True)

    # The 80 will limit the size of the username
    name = db.Column(db.String(80))

    # This will create a relationship with Item Model
    # This will be a list since there could be multiple items
    items = db.relationship('ItemModel', lazy='dynamic')

    # These properties will be saved into the database

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

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
