import logging
from dependency_injector import providers
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .container import AppContainer
from blueprints import health_check, relay, option, hour

def create_app() -> Flask:
  load_dotenv()

  container = AppContainer()
  container.wire(modules=[health_check, relay, option, hour])
  
  app = Flask(__name__)
  app.container = container
  CORS(app)
  
  app.register_blueprint(health_check.blueprint)
  app.register_blueprint(option.blueprint)
  app.register_blueprint(relay.blueprint)
  app.register_blueprint(hour.blueprint)

  return app