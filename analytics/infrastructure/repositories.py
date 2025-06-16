from  analytics.infrastructure.models import Metric as MetricModel
from analytics.domain.entities import Metric
class MetricsRepository:
    def save(self, metric) -> Metric:
        # Logic to save the metric to a database or external service
        metric_model = MetricModel.create(
            plant_id = metric.plant_id,
            metric_value = metric.metric_value,
            metric_types_id = metric.metric_types_id
        )
        return Metric(
            metric.plant_id,
            metric.metric_value,
            metric.metric_types_id,
            metric_model.id
        )
