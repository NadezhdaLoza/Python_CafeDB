from flask import Blueprint
from controllers.ingredients import IngredientController

ingredient_router = Blueprint('ingredients', __name__, url_prefix="ingredients/")
controller = IngredientController()

@ingredient_router.get('')
def get_all():
    return controller.get_all()

@ingredient_router.get('<id>')
def get_one(id: int):
    return controller.get_one(id)

@ingredient_router.post('')
def post():
    return controller.post()

@ingredient_router.put('')
def put():
    return controller.put()

@ingredient_router.delete('<id>')
def delete(id: int):
    return controller.delete(id)