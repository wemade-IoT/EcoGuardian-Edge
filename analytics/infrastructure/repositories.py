from  analytics.infrastructure.models import Metric as MetricModel
from analytics.domain.entities import Metric
class MetricsRepository:
    def save(self, metric) -> Metric:
        # Logic to save the metric to a database or external service
        metric_model = MetricModel.create(
            metric_value = metric.metric_value,
            metric_types_id = metric.metric_types_id,
            device_id = metric.device_id
        )
        return Metric(
            metric.metric_value,
            metric.metric_types_id,
            metric.device_id,
            metric_model.id
        )
