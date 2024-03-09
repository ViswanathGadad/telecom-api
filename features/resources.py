from flask_restful import Api

from features.customer.resource import Customer, Login


def add_api_resources(app):
    api = Api(app)
    api.add_resource(Login, "/login")
    api.add_resource(Customer, "/customer/<string:customer_id>")
