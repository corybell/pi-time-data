from dependency_injector import providers
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .container import AppContainer
from blueprints import health_check, relay, option

def create_app() -> Flask:
  load_dotenv()

  container = AppContainer()
  container.wire(modules=[health_check, relay, option])
  
  app = Flask(__name__)
  app.container = container
  CORS(app)
  
  app.register_blueprint(health_check.blueprint)
  app.register_blueprint(option.blueprint)
  app.register_blueprint(relay.blueprint)
  
  return app