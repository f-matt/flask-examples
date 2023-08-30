from flask import jsonify, request, abort
from flask_restful import Resource, marshal_with
from marshmallow import Schema, fields
from main.models import Item

from datetime import datetime, date

items = [
    Item(id=1, name='First Item', full_description='Description of the first item', registration_date=date(2023, 1, 1), quantity=100, active=True),
    Item(id=2, name='Second Item', full_description='Description of the second item', registration_date=date(2023, 3, 31), quantity=10, active=False),
    Item(id=3, name='Third Item', full_description='Description of the third item', registration_date=date(2023, 12, 31), quantity=25, active=True),
    Item(id=4, name='Third Item', full_description=None, registration_date=None, quantity=75, active=True),
]

class IndexEndpoint(Resource):
    def get(self):
        return jsonify("online")


class ItemSchema(Schema):
    ids = fields.List(fields.Int())
    name = fields.Str()
    active = fields.Boolean()
    registration_date = fields.Date(format="%Y-%m-%d")


class ItemsService(Resource):
    @marshal_with(Item.resource_fields)
    def get(self):
      
        try:
            schema = ItemSchema()
            ids = request.args.getlist("id")

            d = request.args.to_dict()
            d["ids"] = ids
            d.pop("id", None)

            errors = schema.validate(d)
            if errors:
                abort(400, str(errors))
 
            params = schema.load(d)
            l = items
            if 'ids' in params:
                l = [i for i in l if i.id in params["ids"]]
            if 'name' in params:
                l = [i for i in l if params["name"].lower() in i.name.lower()]
            if 'active' in params:
                l = [i for i in l if i.active == params["active"]]
            if 'registration_date' in params:
                l = [i for i in l if i.registration_date == params["registration_date"]]

            return l, 200
        except Exception as e:
            print (e)
