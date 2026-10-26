from flask import Blueprint

from routes.positions import position_router
from routes.categories import category_router
from routes.suppliers import supplier_router
from routes.ingredients import ingredient_router
from routes.dishes import dish_router
from routes.recipes import recipe_router
from routes.bonus_cards import bonus_card_router
from routes.clients import client_router
from routes.employees import employee_router
from routes.orders import order_router

router = Blueprint('api', __name__, url_prefix="/api")

router.register_blueprint(position_router)
router.register_blueprint(category_router)
router.register_blueprint(supplier_router)
router.register_blueprint(ingredient_router)
router.register_blueprint(dish_router)
router.register_blueprint(recipe_router)
router.register_blueprint(bonus_card_router)
router.register_blueprint(client_router)
router.register_blueprint(employee_router)
router.register_blueprint(order_router)