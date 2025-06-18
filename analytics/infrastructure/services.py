import requests
import threading
import time
from analytics.application.services import MetricApplicationService
from iam.application.services import AuthApplicationService

BASE_URL = 'http://localhost:9080/api/v1/'

SENSOR_ENDPOINTS = {
    'water': f'{BASE_URL}water',
    'humidity': f'{BASE_URL}humidity',
    'light': f'{BASE_URL}light',
}

FETCH_INTERVAL = 60

BACKEND_URL = 'http://localhost:9080/api/v1/metric'

def fetch_sensor_data(sensor_type):
    url = SENSOR_ENDPOINTS.get(sensor_type)
    if not url:
        raise ValueError(f"Tipo de sensor desconocido: {sensor_type}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error al obtener datos de {sensor_type}: {e}")
        return None

def fetch_all_sensors():
    data = {}
    for sensor in SENSOR_ENDPOINTS:
        data[sensor] = fetch_sensor_data(sensor)
    return data

def periodic_fetch(callback=None):
    while True:
        data = fetch_all_sensors()
        if callback:
            callback(data)
        time.sleep(FETCH_INTERVAL)

def start_periodic_fetch(callback=None):
    thread = threading.Thread(target=periodic_fetch, args=(callback,), daemon=True)
    thread.start()
    return thread

def send_to_backend(sensor_data):
    payload = {
        "metricValue": float(sensor_data["metric_value"]),
        "metricTypesId": int(sensor_data["metric_types_id"]),
        "deviceId": int(sensor_data["device_id"])
    }
    headers = {
        "X-Device-Id": str(sensor_data["device_id"]),
        "X-API-Key": sensor_data["api_key"]
    }
    try:
        response = requests.post(BACKEND_URL, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Datos enviados al backend: {payload}")
    except Exception as e:
        print(f"Error enviando datos al backend: {e}")

def process_sensor_data(sensor_data):
    metric_service = MetricApplicationService()
    auth_service = AuthApplicationService()
    sensor_type_map = {
        'humidity': 1,
        'light': 2,
        'water': 3
    }
    # Diccionario de API keys por device_id (ahora como string)
    api_keys = {
        "1": 'testkey001',
        "2": 'testkey002',
        "3": 'testkey003'
    }
    for sensor, value in sensor_data.items():
        if value is not None:
            metric_types_id = sensor_type_map.get(sensor)
            metric_value = value.get('value') if isinstance(value, dict) else value
            device_id = value.get('device_id') if isinstance(value, dict) else None
            if device_id is None:
                print(f"No se encontró device_id para {sensor}, se omite la métrica.")
                continue
            if metric_value is None:
                print(f"No se encontró metric_value para {sensor} (device_id={device_id}), se omite la métrica.")
                continue
            device_id_str = str(device_id)
            api_key = api_keys.get(device_id_str)
            if not api_key:
                print(f"No se encontró api_key para device_id={device_id}, se omite la métrica.")
                continue
            auth_service.get_or_create_test_device(device_id_str, api_key)
            try:
                metric = metric_service.create_metric(metric_types_id, metric_value, device_id_str, api_key)
                print(f"Métrica guardada: {metric}")
            except Exception as e:
                print(f"Error guardando métrica para {sensor}: {e}")

            send_to_backend({
                "metric_value": metric_value,
                "metric_types_id": metric_types_id,
                "device_id": device_id_str,
                "api_key": api_key
            })

start_periodic_fetch(process_sensor_data)


