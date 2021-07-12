from flask import Blueprint, jsonify, request
from dependency_injector.wiring import inject, Provide
from services.relay import RelayService
from app.container import AppContainer

blueprint = Blueprint('relay', __name__)

known_relays = ['1', '2', '3', '4', '5', '6', '7', '8']
known_commands = ['on', 'off']

@blueprint.route('/relay', methods=['GET'])
@inject
def relay_list(relay_service: RelayService = Provide[AppContainer.relay_service]):
  relays = relay_service.all()
  return jsonify(relays), 200

@blueprint.route('/relay/<string:relay_id>', methods=['GET'])
@inject
def relay_get(relay_id: str, relay_service: RelayService = Provide[AppContainer.relay_service]):
  if relay_id not in known_relays:
    return jsonify(message='relay not found'), 404

  relay = relay_service.get(relay_id)
  return jsonify(relay), 200

@blueprint.route('/relay/<string:relay_id>', methods=['PUT'])
@inject
def relay_edit(relay_id: str, relay_service: RelayService = Provide[AppContainer.relay_service]):
  if relay_id not in known_relays:
    return jsonify(message='relay not found'), 404

  payload = request.get_json()
  status = relay_service.edit(relay_id, payload)
  if not status:
    return jsonify({}), 400
  
  return jsonify({}), 200
