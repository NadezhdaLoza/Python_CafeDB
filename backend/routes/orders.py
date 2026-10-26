from flask import Blueprint
from controllers.orders import OrderController

order_router = Blueprint('orders', __name__, url_prefix="orders/")
controller = OrderController()

@order_router.get('')
def get_all():
    return controller.get_all()

@order_router.get('<id>')
def get_one(id: int):
    return controller.get_one(id)

@order_router.post('')
def post():
    return controller.post()

@order_router.put('')
def put():
    return controller.put()

@order_router.delete('<id>')
def delete(id: int):
    return controller.delete(id)