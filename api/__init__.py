from dependency_injector import providers
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .containers import Container
from .blueprints import health_check, relay, timer

def create_app() -> Flask:
    load_dotenv()

    container = Container()
    container.config = providers.Configuration()
    container.config.host.from_env('API_HOST')
    container.config.port.from_env('API_PORT')

    container.wire(modules=[health_check, relay, timer])
    
    app = Flask(__name__)
    app.container = container
    CORS(app)
    
    app.register_blueprint(health_check.blueprint)
    app.register_blueprint(timer.blueprint)
    app.register_blueprint(relay.blueprint)
    
    return app