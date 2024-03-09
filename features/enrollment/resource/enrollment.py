from flask import request
from flask_restful import Resource

from ..model import CustomerPlanEnrollmentModel
from ...customer.model import CustomerModel
from ...plan.model import PlanModel


class CustomerPlanEnrollment(Resource):
    def post(self, customer_id):
        customer = CustomerModel.find_by(customer_id=customer_id)
        if not customer:
            return {"message": "Customer does not exist"}, 404

        plan_id = request.json['plan_id']
        plan = PlanModel.find_by(plan_id=plan_id)
        if not plan:
            return {"message": "Plan does not exist"}, 404

        enrollment = CustomerPlanEnrollmentModel.create(customer, plan)
        enrollment.save_to_db()

        return {"message": "Successful enrollment", "enrollment": enrollment.json}

    def put(self, customer_id, enrollment_id):
        enrollment = CustomerPlanEnrollmentModel.find_by(customer_id=customer_id, enrollment_id=enrollment_id)
        if not enrollment:
            return {"message": "Enrollment does not exist"}, 404

        plan_id = request.json['plan_id']
        new_plan = PlanModel.find_by(plan_id=plan_id)
        if not new_plan:
            return {"message": "Plan does not exist"}, 404

        enrollment.update_plan(new_plan)

        return {"message": "Enrollment updated", "enrollment": enrollment.json}
