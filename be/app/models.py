import datetime

from peewee import CharField, DateTimeField
from playhouse.postgres_ext import BinaryJSONField, ForeignKeyField
from playhouse.shortcuts import model_to_dict
from apphelpers.db.peewee import create_pgdb_pool, create_base_model, created

import settings


db = create_pgdb_pool(database=settings.DB_NAME)
BaseModel = create_base_model(db)


class Data(BaseModel):
    created = created()
    updated = DateTimeField(null=False, default=datetime.datetime.utcnow)
    title = CharField(null=False, index=True)
    type = CharField(default='')
    data = BinaryJSONField(default={})

    def to_dict(self):
        return model_to_dict(self)


class Snapshot(BaseModel):
    created = created()
    updated = DateTimeField(null=False, default=datetime.datetime.utcnow)
    data = BinaryJSONField(default={})

    def to_dict(self):
        return model_to_dict(self)


the_models = BaseModel.__subclasses__()


def setup_db():
    db.create_tables(the_models, fail_silently=True)


def destroy_db():
    for o in the_models[::-1]:
        if o.table_exists():
            o.drop_table()
            print("DROP: " + o._meta.name)
