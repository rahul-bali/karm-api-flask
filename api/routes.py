from flask import request, jsonify

from api import app, db
from models.unit import Unit
from models.unit import UnitSchema

'''

@api.route('/', methods=['GET'])
def get():
    return jsonify({'msg': "Hello rahul"})

'''

# Init Schema
# unit_schema = UnitSchema(strict=True)
# units_schema = UnitSchema(many=True, strict=True)

unit_schema = UnitSchema()
units_schema = UnitSchema(many=True)


# Create a unit
@app.route('/unit', methods=['POST'])
def add_unit():
    name = request.json['name']
    description = request.json['description']

    new_unit = Unit(name, description)

    db.session.add(new_unit)
    db.session.commit()

    return unit_schema.jsonify(new_unit)


# Get all units
@app.route('/unit', methods=['GET'])
def get_units():
    all_units = Unit.query.all()
    result = units_schema.dump(all_units)
    return jsonify(result.data)


# Get Single units
@app.route('/unit/<id>', methods=['GET'])
def get_unit(id):
    unit = Unit.query.get(id)
    return unit_schema.jsonify(unit)


# Update a unit
@app.route('/unit/<id>', methods=['PUT'])
def update_unit(id):
    unit = Unit.query.get(id)

    name = request.json['name']
    description = request.json['description']

    unit.name = name
    unit.description = description
    db.session.commit()

    return unit_schema.jsonify(unit)


# Delete unit
@app.route('/unit/<id>', methods=['DELETE'])
def delete_unit(id):
    unit = Unit.query.get(id)

    db.session.delete(unit)
    db.session.commit()
    return unit_schema.jsonify(unit)

