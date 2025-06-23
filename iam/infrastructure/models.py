from peewee import Model, IntegerField, CharField, DateTimeField

from shared.infrastructre.database import db


class Device(Model):

      device_id = IntegerField(primary_key=True)
      api_key = CharField()
      created_at = DateTimeField()

      class Meta:
          database = db
          table_name = 'devices'