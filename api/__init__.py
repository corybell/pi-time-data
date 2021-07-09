import flask
from injector import Injector
from flask_injector import FlaskInjector
from flask_cors import CORS
from dotenv import load_dotenv
from api.container import AppContainer
from api.blueprints import register_blueprints

load_dotenv()

app = flask.Flask(__name__)

injector = Injector([AppContainer(app)])

CORS(app)

register_blueprints(app)

# FlaskInjector(app=app, injector=injector)
