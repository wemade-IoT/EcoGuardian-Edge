from analytics.domain.entities import Metric


class MetricService:
    def __init__(self):
        pass

    @staticmethod
    def create_metric(plant_id: float, metric_type:float, metric_value: float) -> Metric:
        try:
            metric_value = float(metric_value)
            metric_type = float(metric_type)
            if not (0 <= metric_value <= 100):
                raise ValueError("Metric value must be between 0 and 100 percentage")
            if not (1 <= metric_type <= 3):
                raise ValueError("Metric type must be between 1 and 3")
        except ValueError:
            raise ValueError("Metric value and type must be a float")
        return Metric(plant_id,metric_type, metric_value)