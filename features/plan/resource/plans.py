from flask_restful import Resource

from ..model import PlanModel


class Plans(Resource):
    def get(self):
        return {"plans": [plan.json for plan in PlanModel.find_all()]}
