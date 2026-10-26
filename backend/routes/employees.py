from flask import Blueprint
from controllers.employees import EmployeeController

employee_router = Blueprint('employees', __name__, url_prefix="employees/")
controller = EmployeeController()

@employee_router.get('')
def get_all():
    return controller.get_all()

@employee_router.get('<id>')
def get_one(id: int):
    return controller.get_one(id)

@employee_router.post('')
def post():
    return controller.post()

@employee_router.put('')
def put():
    return controller.put()

@employee_router.delete('<id>')
def delete(id: int):
    return controller.delete(id)