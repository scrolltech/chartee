import os
import json
import datetime

from be.app.libs import data as datalib


CHART_JSON_DIR = os.path.abspath(
    os.path.join(os.getcwd(), 'charts')
)

if not os.path.exists(CHART_JSON_DIR):
    os.mkdir(CHART_JSON_DIR)


def JSONSerializer(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


def publish(id):
    chart_data = datalib.get(id)
    filename = '{}.json'.format(id)
    chart_json_file_location = os.path.join(CHART_JSON_DIR, filename)
    with open(chart_json_file_location, 'w') as json_file:
        json.dump(chart_data, json_file, default=JSONSerializer)


def list_():
    return datalib.list_()


def create_and_publish(**data):
    id = datalib.create(**data)
    publish(id)
    return id


def update_and_publish(id, mod_data):
    resp = datalib.update(id, mod_data)
    if resp:
        publish(id)
        return True


def get(id):
    return datalib.get(id)


def destroy(id):
    return datalib.destroy(id)
