
from flask import request, Blueprint, jsonify

from analytics.application.services import MetricApplicationService
from iam.interfaces.services import authenticate_request

metric_api = Blueprint('metric_api', __name__)
metric_service = MetricApplicationService()

@metric_api.route('/api/v1/analytics/metrics', methods=['POST'])
def create_metric():
    auth_result = authenticate_request()
    if auth_result:
        return auth_result
    data = request.json
    try:
        plant_id = data['plant_id']
        metric_type = data['metric_types_id']
        metric_value = data['metric_value']
        device_id = data['device_id']
        metric = metric_service.create_metric(plant_id, metric_type, metric_value,device_id,request.headers.get('X-API-Key'))
        return jsonify({'status': 'success', 'data': {
            'id': metric.id,
            'plant_id': metric.plant_id,
            'metric_types_id': metric.metric_types_id,
            'metric_value': metric.metric_value
        }}), 201
    except KeyError:
        return jsonify({'error': 'Missing required fields'}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
