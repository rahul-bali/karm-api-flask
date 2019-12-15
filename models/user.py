from api import db, ma
from models import category


# User class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    created_on = db.Column(db.DateTime())
    active = db.Column(db.Boolean(True))
    category = db.Column(db.Enum())
    owner = db.Column(category.name)

    def __init__(self, name, description):
        self.name = name
        self.description = description


# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')
