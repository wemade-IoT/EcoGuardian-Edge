from  analytics.infrastructure.models import Metric as MetricModel
from analytics.domain.entities import Metric
from datetime import datetime

class MetricsRepository:
    # Repository for metric data persistence
    def save(self, metric) -> Metric:
        # Save metric to database and return domain entity
        metric_model = MetricModel.create(
            metric_value = metric.metric_value,
            metric_types_id = metric.metric_types_id,
            device_id = metric.device_id,
            created_at = getattr(metric, 'created_at', datetime.now())
        )
        # Return domain entity with generated ID
        return Metric(
            metric.metric_value,
            metric.metric_types_id,
            metric.device_id,
            metric_model.id
        )
