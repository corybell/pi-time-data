from flask import Blueprint, jsonify, request
from dependency_injector.wiring import inject, Provide
from services.relay import RelayService
from app.container import AppContainer

blueprint = Blueprint('relay', __name__)

@blueprint.route('/relay', methods=['GET'])
@inject
def relay_list(relay_service: RelayService = Provide[AppContainer.relay_service]):
  relays = relay_service.all()
  
  return jsonify(relays), 200

@blueprint.route('/relay/<string:id>', methods=['GET'])
@inject
def relay_get(id: str, relay_service: RelayService = Provide[AppContainer.relay_service]):
  relay = relay_service.get(id)
  if not relay:
    return jsonify({}), 404
  
  return jsonify(relay), 200

@blueprint.route('/relay/<string:id>', methods=['PUT'])
@inject
def relay_edit(id: str, relay_service: RelayService = Provide[AppContainer.relay_service]):
  payload = request.get_json()
  if not payload:
    return jsonify({}), 400

  relay = relay_service.edit(id, payload)
  if not relay:
    return jsonify({}), 404
  
  return jsonify(relay), 200
