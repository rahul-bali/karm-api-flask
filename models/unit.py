from api import db, ma


# Unit class
class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(100), unique=True)
    joined_on = db.Column(db.DateTime())
    active = db.Column(db.Boolean(True))
    about = db.Column(db.String(25))
    avatar_link = db.Column(db.String(250))
    id_badges = db.Column(user.py)
    ## portfolio images

    def __init__(self, name, description):
        self.name = name
        self.description = description


# Unit Schema
class UnitSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')
