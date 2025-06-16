from peewee import Model, AutoField, CharField, FloatField

from shared.infrastructre.database import db


class Metric(Model):
    id = AutoField(),
    plant_id = FloatField(),
    metric_value = FloatField(),
    metric_types_id = FloatField(),

    class Meta:
        database = db
        table_name = 'metrics'