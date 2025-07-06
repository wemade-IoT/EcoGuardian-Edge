from analytics.domain.entities import Metric


class MetricService:
    # Domain service for metric business logic
    def __init__(self):
        pass

    @staticmethod
    def create_metric(metric_type: float, metric_value: float, device_id: int) -> Metric:
        # Validate and create metric with business rules
        try:
            metric_value = float(metric_value)
            metric_type = float(metric_type)
            # Ensure metric value is within valid percentage range
            if not (0 <= metric_value <= 100):
                raise ValueError("Metric value must be between 0 and 100 percentage")
            # Ensure metric type is within valid type range
            if not (1 <= metric_type <= 4):
                raise ValueError("Metric type must be between 1 and 4")
        except ValueError:
            raise ValueError("Metric value and type must be a float")
        return Metric(metric_value, metric_type, device_id)
