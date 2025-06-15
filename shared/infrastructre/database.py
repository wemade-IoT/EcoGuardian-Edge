from peewee import SqliteDatabase

db = SqliteDatabase('ecoguardian-edge.db')

def init_db():
    db.connect()
    # Place any database initialization code here, such as creating tables