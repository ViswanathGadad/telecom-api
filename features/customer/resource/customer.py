from flask_restful import Resource

from ..model import CustomerModel


class Customer(Resource):
    def get(self, customer_id):
        customer = CustomerModel.find_by(customer_id=customer_id)

        if not customer:
            return {"message": "customer does not exist"}, 404

        return {"customer": customer.json}
