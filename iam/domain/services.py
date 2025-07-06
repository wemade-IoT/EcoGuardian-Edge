from typing import Optional

from iam.domain.entities import Device


class AuthService:
    # Domain service for authentication business logic
    def __init__(self):
        pass

    @staticmethod
    def authenticate(device: Optional[Device]) -> bool:
        # Simple authentication check - device exists
        return device is not None