from peewee import Model, AutoField, FloatField, IntegerField, DateTimeField
from datetime import datetime

from shared.infrastructre.database import db


class Metric(Model):
    id = AutoField()
    device_id = IntegerField()
    metric_value = FloatField()
    metric_types_id = FloatField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'metrics'