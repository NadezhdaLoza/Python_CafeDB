from flask import Blueprint
from controllers.bonus_cards import BonusCardController

bonus_card_router = Blueprint('bonus_cards', __name__, url_prefix="bonus-cards/")
controller = BonusCardController()

@bonus_card_router.get('')
def get_all():
    return controller.get_all()

@bonus_card_router.get('<id>')
def get_one(id: int):
    return controller.get_one(id)

@bonus_card_router.post('')
def post():
    return controller.post()

@bonus_card_router.put('')
def put():
    return controller.put()

@bonus_card_router.delete('<id>')
def delete(id: int):
    return controller.delete(id)