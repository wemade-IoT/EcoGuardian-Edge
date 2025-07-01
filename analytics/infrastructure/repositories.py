from  analytics.infrastructure.models import Metric as MetricModel
from analytics.domain.entities import Metric
from datetime import datetime
class MetricsRepository:
    def save(self, metric) -> Metric:
        metric_model = MetricModel.create(
            metric_value = metric.metric_value,
            metric_types_id = metric.metric_types_id,
            device_id = metric.device_id,
            created_at = getattr(metric, 'created_at', datetime.now())
        )
        return Metric(
            metric.metric_value,
            metric.metric_types_id,
            metric.device_id,
            metric_model.id
        )
