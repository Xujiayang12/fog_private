from peewee import *
import warnings

warnings.filterwarnings("ignore")

db = SqliteDatabase('air.db')
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Air(BaseModel):
    date = CharField()
    year = IntegerField()
    month = IntegerField()
    day = IntegerField()
    aqi = IntegerField()
    rank = CharField()
    pm25 = IntegerField()
    pm10 = IntegerField()
    so2 = IntegerField()
    co = FloatField()
    no2 = IntegerField()
    o3 = IntegerField()

    class Meta:
        db_table = 'air'
