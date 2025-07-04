from iam.application.services import AuthApplicationService

def create_devices():
    auth_service = AuthApplicationService()
    devices = [
        (1, "b1e2c3d4-5f6a-7b8c-9d0e-1f2a3b4c5d6e"),
    ]
    for device_id, api_key in devices:
        device = auth_service.get_or_create_test_device(device_id, api_key)
        print(f"Dispositivo creado o existente: id={device.device_id}, api_key={device.api_key}")

if __name__ == "__main__":
    create_devices()