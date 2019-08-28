from app.models import Snapshot


def create(**data):
    return Snapshot.create(**data).id


def list_():
    return tuple(Snapshot.select().order_by(Snapshot.created.desc()).dicts())


def get(id):
    snapshot = Snapshot.select().where(Snapshot.id == id).first()
    if snapshot:
        return snapshot.to_dict()


def destroy(id):
    return Snapshot.delete().where(Snapshot.id == id).execute()
