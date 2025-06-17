from peewee import Model, AutoField, FloatField, IntegerField

from shared.infrastructre.database import db


class Metric(Model):
    id = AutoField()
    device_id = IntegerField()
    metric_value = FloatField()
    metric_types_id = FloatField()

    class Meta:
        database = db
        table_name = 'metrics'