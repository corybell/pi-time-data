from flask import Blueprint, jsonify
from dependency_injector.wiring import inject, Provide
from services.option import OptionService
from app.container import AppContainer

blueprint = Blueprint('option', __name__)

@blueprint.route('/option', methods=['GET', 'OPTIONS'])
@inject
def option_list(option_service: OptionService = Provide[AppContainer.option_service]):
  options = option_service.all()
  return jsonify(options), 200
