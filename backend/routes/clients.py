from flask import Blueprint
from controllers.clients import ClientController

client_router = Blueprint('clients', __name__, url_prefix="clients/")
controller = ClientController()

@client_router.get('')
def get_all():
    return controller.get_all()

@client_router.get('<id>')
def get_one(id: int):
    return controller.get_one(id)

@client_router.post('')
def post():
    return controller.post()

@client_router.put('')
def put():
    return controller.put()

@client_router.delete('<id>')
def delete(id: int):
    return controller.delete(id)