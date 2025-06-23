from flask import Blueprint, request, jsonify

from iam.application.services import AuthApplicationService

iam_api = Blueprint('iam', __name__)

auth_service = AuthApplicationService()

def authenticate_request():
    device_id = request.headers.get('Device-Id')
    api_key = request.headers.get('Api-Key')
    if not device_id or not api_key:
        return jsonify({"error": "Missing Device-Id or Api-Key header"}), 401
    try:
        device_id_int = int(device_id)
    except ValueError:
        return jsonify({"error": "Device-Id must be an integer"}), 401
    if not auth_service.authenticate(device_id_int, api_key):
        return jsonify({"error": "Invalid Device-Id or Api-Key"}), 401
    return None