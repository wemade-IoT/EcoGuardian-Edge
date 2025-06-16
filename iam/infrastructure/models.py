from peewee import Model, CharField, DateTimeField

from shared.infrastructre.database import db


class Device(Model):

      device_id = CharField(primary_key=True)
      api_key = CharField()
      created_at = DateTimeField()

      class Meta:
          database = db
          table_name = 'devices'