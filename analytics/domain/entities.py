class Metric:
    def __init__(self, plant_id, metric_value , metric_types_id,id=None):
        self.id = id
        self.plant_id = plant_id
        self.metric_value = metric_value
        self.metric_types_id = metric_types_id