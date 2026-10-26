from flask import Blueprint
from controllers.recipes import RecipeController

recipe_router = Blueprint('recipes', __name__, url_prefix="recipes/")
controller = RecipeController()

@recipe_router.get('')
def get_all():
    return controller.get_all()

@recipe_router.get('<id>')
def get_one(id: int):
    return controller.get_one(id)

@recipe_router.post('')
def post():
    return controller.post()

@recipe_router.put('')
def put():
    return controller.put()

@recipe_router.delete('<id>')
def delete(id: int):
    return controller.delete(id)