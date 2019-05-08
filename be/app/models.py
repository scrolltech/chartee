import datetime

from apphelpers.db.peewee import create_pgdb_pool, create_base_model, created
from playhouse.postgres_ext import BinaryJSONField, ForeignKeyField
from peewee import CharField, DateTimeField

import settings


db = create_pgdb_pool(database=settings.DB_NAME)
BaseModel = create_base_model(db)


class CommonModel(BaseModel):
    created = created()


class Chart(CommonModel):
    title = CharField(null=False, index=True)
    type = CharField(default='')
    data = BinaryJSONField(default={})
    updated = DateTimeField(null=False, default=datetime.datetime.utcnow)


class Spanshot(CommonModel):
    chart = ForeignKeyField(Chart, null=False, default=1, db_column='chart_id')
    data = BinaryJSONField(null=False)


class Revision(CommonModel):
    chart = ForeignKeyField(Chart, null=False, default=1, db_column='chart_id')
    snap = ForeignKeyField(Spanshot, null=False, default=1, db_column='snap_id')


the_models = BaseModel.__subclasses__() + CommonModel.__subclasses__()


def setup_db():
    db.create_tables(the_models, fail_silently=True)


def destroy_db():
    for o in the_models[::-1]:
        if o.table_exists():
            o.drop_table()
            print("DROP: " + o._meta.name)
