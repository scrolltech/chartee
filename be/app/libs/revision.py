from be.app.models import Revision

def create(**data):
    return Revision.create(**data).id


def destroy(id):
    return Revision.delete().where(Revision.id == id).execute()


def get(id):
    r = Revision.select().where(Revision.id == id).first()
    return r.to_dict() if r else None
