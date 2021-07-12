from flask import Blueprint, jsonify
from dependency_injector.wiring import inject, Provide
from services.timer_service import TimerService
from ..containers import Container

blueprint = Blueprint('timer', __name__)

@blueprint.route('/timer', methods=['GET'])
@inject
def timer_list(timer_service: TimerService = Provide[Container.timer_service]):
  timerOptions = timer_service.all()
  return jsonify(timerOptions), 200
