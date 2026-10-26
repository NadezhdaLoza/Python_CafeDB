from flask import Blueprint
from controllers.dishes import DishController

dish_router = Blueprint('dishes', __name__, url_prefix="dishes/")
controller = DishController()

@dish_router.get('')
def get_all():
    return controller.get_all()

@dish_router.get('<id>')
def get_one(id: int):
    return controller.get_one(id)

@dish_router.post('')
def post():
    return controller.post()

@dish_router.put('')
def put():
    return controller.put()

@dish_router.delete('<id>')
def delete(id: int):
    return controller.delete(id)