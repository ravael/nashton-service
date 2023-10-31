from flask import Blueprint
from src.controllers.auth_controller import users
from src.controllers.riddle_controller import riddle

api = Blueprint('api', __name__)

api.register_blueprint(users, url_prefix="/users")
api.register_blueprint(riddle, url_prefix="/riddle")
