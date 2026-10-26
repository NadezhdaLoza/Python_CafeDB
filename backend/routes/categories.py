from flask import Blueprint
from controllers.categories import CategoryController

category_router = Blueprint('categories', __name__, url_prefix="categories/")
controller = CategoryController()

@category_router.get('')
def get_all():
    return controller.get_all()

@category_router.get('<id>')
def get_one(id: int):
    return controller.get_one(id)

@category_router.post('')
def post():
    return controller.post()

@category_router.put('')
def put():
    return controller.put()

@category_router.delete('<id>')
def delete(id: int):
    return controller.delete(id)