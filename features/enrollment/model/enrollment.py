from datetime import datetime, timedelta

from sqlalchemy import DateTime

from features.repo import db


class CustomerPlanEnrollmentModel(db.Model):
    __tablename__ = "enrollments"

    enrollment_id = db.Column(db.Integer, primary_key=True)
    enroll_date = db.Column(DateTime, nullable=False)
    expire_date = db.Column(DateTime, nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('plans.plan_id'), nullable=False)

    plan = db.relationship('PlanModel', uselist=False)

    @property
    def json(self):
        enrollment_json = {
            'enrollment_id': self.enrollment_id,
            'enroll_date': self.enroll_date.strftime("%d-%m-%Y"),
            'expire_date': self.expire_date.strftime("%d-%m-%Y"),
            'status': 'Inactive' if datetime.now().date() > self.expire_date.date() else 'Active'
        }
        enrollment_json.update(self.plan.json)
        return enrollment_json

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_plan(self, new_plan):
        self.plan_id = new_plan.plan_id
        self.expire_date = self.enroll_date + timedelta(days=new_plan.validity)
        db.session.commit()

    @classmethod
    def find_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def create(cls, customer, plan, enroll_date=None):
        return cls(customer_id=customer.customer_id,
                   plan_id=plan.plan_id,
                   enroll_date=enroll_date or datetime.now(),
                   expire_date=(enroll_date or datetime.now()) + timedelta(days=plan.validity))
