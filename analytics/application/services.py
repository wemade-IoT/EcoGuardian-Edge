from analytics.infrastructure.repositories import MetricsRepository
from analytics.domain.services import MetricService
from analytics.infrastructure.models import Metric
from iam.application.services import AuthApplicationService


class MetricApplicationService:
    def __init__(self):
        self.metrics_repository = MetricsRepository()
        self.metrics_service = MetricService()
        self.iam_service = AuthApplicationService()
    def create_metric(self, plant_id: float, metric_types_id: float, metric_value: float, device_id:str, api_key:str) -> Metric:
        if not self.iam_service.get_device_by_id_and_api_key(device_id, api_key):
            raise ValueError("Device not found or Invalid API key")
        metric = self.metrics_service.create_metric(plant_id, metric_types_id, metric_value)
        return self.metrics_repository.save(metric)