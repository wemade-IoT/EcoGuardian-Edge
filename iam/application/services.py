from typing import Optional

from iam.domain.entities import Device
from iam.domain.services import AuthService
from iam.infrastructure.repositories import DeviceRepository


class AuthApplicationService:
    # Application service for device authentication
    def __init__(self):
        self.device_repository = DeviceRepository()
        self.auth_service = AuthService()

    def authenticate(self, device_id: int, api_key: str) -> bool:
        # Authenticate device using ID and API key
        device: Optional[Device] = self.device_repository.find_by_id_and_api_key(device_id, api_key)
        return self.auth_service.authenticate(device)

    def get_or_create_test_device(self,device_id:int,api_key:str) -> Device:
        # Get or create a test device for development
        return self.device_repository.get_or_create_test_device(device_id,api_key)

    def get_device_by_id_and_api_key(self, device_id: int, api_key: str) -> Optional[Device]:
        # Find device by ID and API key combination
        return self.device_repository.find_by_id_and_api_key(device_id, api_key)