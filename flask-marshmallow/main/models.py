from flask_restful import fields

class Item:
    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'full_description': fields.String,
        'registration_date': fields.DateTime(dt_format='iso8601'),
        'quantity': fields.Integer,
        'active': fields.Boolean
    }

    def __init__(self, id, name, full_description, registration_date, quantity, active):
        self.id = id
        self.name = name
        self.full_description = full_description
        self.registration_date = registration_date
        self.quantity = quantity
        self.active = active
