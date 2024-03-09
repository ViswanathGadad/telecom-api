from flask import request
from flask_restful import Resource
from werkzeug.security import check_password_hash

from ..model import CustomerModel


class Login(Resource):
    def post(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return {"message": 'Login required'}, 401
        customer = CustomerModel.find_by(username=auth.username)

        if not customer:
            return {"message": 'User not found'}, 403

        if check_password_hash(customer.password, auth.password):
            return {
                "message": "Successful login",
                "customer_id": customer.customer_id
            }

        return {"message": 'Invalid password'}, 401
