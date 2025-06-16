from peewee import SqliteDatabase


db = SqliteDatabase('ecoguardian_edge.db')

def init_db():
    db.connect()
    # Place any database initialization code here, such as creating tables
    from analytics.infrastructure.models import Metric
    db.create_tables([Metric], safe=True)