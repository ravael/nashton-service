from flask import Blueprint
from src.controllers.auth_controller import users

api = Blueprint('api', __name__)
api.register_blueprint(users, url_prefix="/users")
