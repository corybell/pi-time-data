from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .containers import Container
from .blueprints import health_check, relay, timer

load_dotenv()

def create_app() -> Flask:
    container = Container()
    container.wire(modules=[relay, timer])
    
    app = Flask(__name__)
    app.container = container
    CORS(app)
    
    app.register_blueprint(health_check.blueprint)
    app.register_blueprint(timer.blueprint)
    app.register_blueprint(relay.blueprint)
    return app