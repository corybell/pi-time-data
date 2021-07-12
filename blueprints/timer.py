from flask import Blueprint, jsonify
from dependency_injector.wiring import inject, Provide
from services.timer import TimerService
from app.container import AppContainer

blueprint = Blueprint('timer', __name__)

@blueprint.route('/timer', methods=['GET'])
@inject
def timer_list(timer_service: TimerService = Provide[AppContainer.timer_service]):
  timerOptions = timer_service.all()
  return jsonify(timerOptions), 200
