from flask import Blueprint, jsonify
from dependency_injector.wiring import inject, Provide
from services.minute import MinuteService
from app.container import AppContainer

blueprint = Blueprint('minute', __name__)

@blueprint.route('/minute/<string:id>', methods=['GET'])
@inject
def minute_get(id: str, minute_service: MinuteService = Provide[AppContainer.minute_service]):
  minute = minute_service.get(id)
  if not minute:
    return jsonify({}), 404

  return jsonify(minute), 200
