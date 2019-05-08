from be.app.models import Chart


def create(**data):
    return Chart.create(**data).id


def destroy(id):
    return Chart.delete().where(Chart.id == id).execute()


def get(id):
    c = Chart.select().where(Chart.id == id).first()
    return c.to_dict() if c else None


def update(id, mod_data):
    updatables = ('title', 'type', 'data')
    update_dict = dict((k, v) for (k, v) in list(mod_data.items()) if k in updatables)
    q = Chart.update(**update_dict).where(Chart.id == id)
    q.execute()
    return True
