from flask_restful import Api

from features.customer.resource import Customer, Login
from features.enrollment.resource import CustomerPlanEnrollment
from features.plan.resource import Plans


def add_api_resources(app):
    api = Api(app)
    api.add_resource(CustomerPlanEnrollment, "/customer/<string:customer_id>/enroll",
                     "/customer/<string:customer_id>/enroll/<string:enrollment_id>")
    api.add_resource(Login, "/login")
    api.add_resource(Plans, "/plans")
    api.add_resource(Customer, "/customer/<string:customer_id>")
