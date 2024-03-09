from features.repo import db


class PlanModel(db.Model):
    __tablename__ = "plans"

    plan_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    validity = db.Column(db.Integer, nullable=False)

    @property
    def json(self):
        return {
            'plan_id': self.plan_id,
            'name': self.name,
            'cost': self.cost,
            'validity': self.validity,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
