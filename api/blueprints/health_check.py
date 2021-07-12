from flask import Blueprint, jsonify
from dependency_injector.providers import Configuration
from dependency_injector.wiring import inject, Provide
from ..containers import Container

blueprint = Blueprint('health_check', __name__)

@blueprint.route('/health-check', methods=['GET'])
@inject
def health_check(config: Configuration = Provide[Container.config]):
  return jsonify(version='1.0.0', config=config), 200
