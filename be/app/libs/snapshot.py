from be.app.models import Snapshot


def create(**data):
    return Snapshot.create(**data).id


def destroy(id):
    return Snapshot.delete().where(Snapshot.id == id).execute()


def get(id):
    s = Snapshot.select().where(Snapshot.id == id).first()
    return s.to_dict() if s else None
