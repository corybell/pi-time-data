from flask import Blueprint, jsonify, request
from dependency_injector.wiring import inject, Provide
from services.relay import RelayService
from services.option import OptionService
from app.container import AppContainer

blueprint = Blueprint('hydrate', __name__)

@blueprint.route('/hydrate', methods=['GET'])
@inject
def hydrate(
    relay_service: RelayService = Provide[AppContainer.relay_service],
    option_service: OptionService = Provide[AppContainer.option_service]
  ):
  
  relays = relay_service.all()

  all_options = option_service.all()

  return jsonify(
    relays=relays, 
    hours=all_options['hours'],
    minutes=all_options['minutes'],
  ), 200