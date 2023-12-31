from flask import Flask
from flask_cors import CORS
import os
from src.config.config import Config
from dotenv import load_dotenv
from src.models.user_model import User
from src.routes import api
from src.config.database import MongoDBConnection

load_dotenv()

app = Flask(__name__)
CORS(app)

config = Config().dev_config

app.env = config.ENV

app.register_blueprint(api, url_prefix="/api")
