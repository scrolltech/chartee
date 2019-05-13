from be.app.models import Data


def create(**data):
    return Data.create(**data).id


def list_():
    return tuple(Data.select().order_by(Data.created.desc()).dicts())


def get(id):
    data = Data.select().where(Data.id == id).first()
    if data:
        return data.to_dict()


def update(id, mod_data):
    updatables = ('title', 'type', 'data', 'published', 'unpublished', 'status')
    update_dict = dict((k, v) for (k, v) in list(mod_data.items()) if k in updatables)
    q = Data.update(**update_dict).where(Data.id == id)
    q.execute()
    return True


def destroy(id):
    return Data.delete().where(Data.id == id).execute()
