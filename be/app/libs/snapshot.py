from be.app.models import Spanshot


def create(**data):
    return Spanshot.create(**data).id


def destroy(id):
    return Spanshot.delete().where(Spanshot.id == id).execute()


def get(id):
    s = Spanshot.select().where(Spanshot.id == id).first()
    return s.to_dict() if s else None
