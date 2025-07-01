import requests
from iam.application.services import AuthApplicationService
import threading
import time
from analytics.infrastructure.models import Metric as MetricModel
from datetime import datetime, timedelta
from collections import defaultdict
import logging

BACKEND_URL = 'http://localhost:9080/api/v1/metrics'
PUSH_INTERVAL = 15# segundos

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s %(message)s')

def send_metric_to_backend(metric_value, metric_types_id, device_id, api_key):
    iam_service = AuthApplicationService()
    if not iam_service.authenticate(device_id, api_key):
        raise ValueError("Autenticación fallida: device_id o api_key inválidos")
    payload = {
        "metricValue": float(metric_value),
        "metricTypesId": int(metric_types_id),
        "deviceId": int(device_id)
    }
    headers = {
        "Device-Id": str(device_id),
        "Api-Key": api_key
    }
    try:
        response = requests.post(BACKEND_URL, json=payload, headers=headers)
        response.raise_for_status()
        logging.info(f"Métrica enviada al backend: {payload}")
        return response.json()
    except Exception as e:
        logging.error(f"Error enviando métrica al backend: {e}")
        raise

def get_average_metrics_last_2_minutes():
    now = datetime.now()
    two_minutes_ago = now - timedelta(minutes=120)
    metrics = list(MetricModel.select().where(MetricModel.created_at >= two_minutes_ago))
    grouped = defaultdict(list)
    for metric in metrics:
        grouped[(metric.metric_types_id, metric.device_id)].append(metric.metric_value)
    averages = []
    for (metric_types_id, device_id), values in grouped.items():
        avg = sum(values) / len(values)
        averages.append({
            'metric_types_id': metric_types_id,
            'device_id': device_id,
            'metric_value': avg
        })
    return averages

def push_all_metrics_to_backend(api_key):
    averages = get_average_metrics_last_2_minutes()
    for avg in averages:
        try:
            send_metric_to_backend(
                avg['metric_value'],
                avg['metric_types_id'],
                avg['device_id'],
                api_key
            )
        except Exception as e:
            logging.error(f"No se pudo enviar el promedio de métricas tipo {avg['metric_types_id']}: {e}")

def periodic_metrics_push(api_key):
    logging.info("Hilo de envío periódico de métricas iniciado.")
    while True:
        push_all_metrics_to_backend(api_key)
        time.sleep(PUSH_INTERVAL)

def start_periodic_metrics_push(api_key):
    thread = threading.Thread(target=periodic_metrics_push, args=(api_key,), daemon=True)
    thread.start()
    return thread