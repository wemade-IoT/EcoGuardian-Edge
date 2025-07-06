from analytics.infrastructure.repositories import MetricsRepository
from analytics.domain.services import MetricService
from analytics.infrastructure.models import Metric
from iam.application.services import AuthApplicationService


class MetricApplicationService:
    # Application service for handling metric operations with authentication
    
    def __init__(self):
        self.metrics_repository = MetricsRepository()
        self.metrics_service = MetricService()
        self.iam_service = AuthApplicationService()
    
    def create_metric(self, metric_types_id: float, metric_value: float, device_id: int, api_key: str) -> Metric:
        # Create a new metric after device authentication
        # Validate device exists and API key is valid
        if not self.iam_service.get_device_by_id_and_api_key(device_id, api_key):
            raise ValueError("Device not found or Invalid API key")
        
        # Create metric using domain service
        metric = self.metrics_service.create_metric(metric_types_id, metric_value, device_id)
        return self.metrics_repository.save(metric)