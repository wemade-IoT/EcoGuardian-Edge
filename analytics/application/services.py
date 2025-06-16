from analytics.infrastructure.repositories import MetricsRepository
from analytics.domain.services import MetricService
from analytics.infrastructure.models import Metric

class MetricApplicationService:
    def __init__(self):
        self.metrics_repository = MetricsRepository()
        self.metrics_service = MetricService()
    def create_metric(self, plant_id: float, metric_types_id: float, metric_value: float) -> Metric:
        metric = self.metrics_service.create_metric(plant_id, metric_types_id, metric_value)
        return self.metrics_repository.save(metric)