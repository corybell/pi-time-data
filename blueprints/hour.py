from flask import Blueprint, jsonify
from dependency_injector.wiring import inject, Provide
from services.hour import HourService
from app.container import AppContainer

blueprint = Blueprint('hour', __name__)

@blueprint.route('/hour/<string:id>', methods=['GET'])
@inject
def hour_get(id: str, hour_service: HourService = Provide[AppContainer.hour_service]):
  hour = hour_service.get(id)
  if not hour:
    return jsonify({}), 404

  return jsonify(hour), 200
