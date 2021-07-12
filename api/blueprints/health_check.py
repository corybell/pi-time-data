from flask import Blueprint, jsonify

blueprint = Blueprint('health_check', __name__)

@blueprint.route('/health-check', methods=['GET'])
def health_check():
  return jsonify(version='1.0.0'), 200
