import os
import json
import datetime

from be.app.libs import data as datalib


MEDIA_DIR = os.path.abspath(
    os.path.join(os.getcwd(), 'media')
)

if not os.path.exists(MEDIA_DIR):
    os.mkdir(MEDIA_DIR)


def JSONSerializer(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


def publish(id):
    chart_data = datalib.get(id)
    filename = '{}.json'.format(id)
    media_location = os.path.join(MEDIA_DIR, filename)
    with open(media_location, 'w') as json_file:
        json.dump(chart_data, json_file, default=JSONSerializer)


def list_():
    return datalib.list_()


def create_and_publish(**data):
    resp = datalib.create(**data)
    if data:
        publish(data['id'])
        return data['id']


def update_and_publish(id, mod_data):
    resp = datalib.update(id, mod_data)
    if resp:
        publish(id)
        return True


def get(id):
    return datalib.get(id)


def destroy(id):
    return datalib.destroy(id)
