class Metric:
    def __init__(self, metric_value, metric_types_id, device_id, id=None):
        self.id = id
        self.metric_value = metric_value
        self.metric_types_id = metric_types_id
        self.device_id = device_id
