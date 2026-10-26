from flask import Blueprint
from controllers.suppliers import SupplierController

supplier_router = Blueprint('suppliers', __name__, url_prefix="suppliers/")
controller = SupplierController()

@supplier_router.get('')
def get_all():
    return controller.get_all()

@supplier_router.get('<id>')
def get_one(id: int):
    return controller.get_one(id)

@supplier_router.post('')
def post():
    return controller.post()

@supplier_router.put('')
def put():
    return controller.put()

@supplier_router.delete('<id>')
def delete(id: int):
    return controller.delete(id)