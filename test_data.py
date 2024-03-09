from datetime import datetime, timedelta

from features.customer.model import CustomerModel
from features.enrollment.model import CustomerPlanEnrollmentModel
from features.plan.model import PlanModel
from features.repo import db


def insert_test_data():
    db.drop_all()
    db.create_all()

    cust1 = CustomerModel.create({
        "username": "user1",
        "password": "pass1",
        "name": "Test User 1",
        "dob": "31-01-1990",
        "email": "test.user.1@gmail.com",
        "aadhar_number": "123409876543",
        "registration_date": "15-02-2023",
        "mobile_no": "9234567810"
    })

    cust2 = CustomerModel.create({
        "username": "user2",
        "password": "pass2",
        "name": "Test User 2",
        "dob": "15-02-1991",
        "email": "test.user.2@gmail.com",
        "aadhar_number": "654312340987",
        "mobile_no": "7890123456"
    })

    cust3 = CustomerModel.create({
        "username": "user3",
        "password": "pass3",
        "name": "Test User 3",
        "dob": "05-01-1994",
        "email": "test.user.3@gmail.com",
        "aadhar_number": "564312340978",
        "mobile_no": "8790123465"
    })

    plan1 = PlanModel(name="Platinum365", cost=499, validity=365)
    plan2 = PlanModel(name="Gold180", cost=299, validity=180)
    plan3 = PlanModel(name="Silver90", cost=199, validity=90)

    cust1.save_to_db()
    cust2.save_to_db()
    cust3.save_to_db()
    plan1.save_to_db()
    plan2.save_to_db()
    plan3.save_to_db()

    CustomerPlanEnrollmentModel.create(cust1,
                                       plan1,
                                       datetime.now() - timedelta(days=plan1.validity + 1)
                                       ).save_to_db()

    CustomerPlanEnrollmentModel.create(cust2,
                                       plan2,
                                       ).save_to_db()
