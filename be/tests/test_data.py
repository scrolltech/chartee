import pytest

import dummy

from be.app.libs import data as datalib
from be.app.models import Data as DataModel


def test_create():
    assert datalib.create(**dummy.data_1)
    assert datalib.create(**dummy.data_2)
    assert datalib.create(**dummy.data_3)


def test_list_():
    all_data = datalib.list_()
    assert len(all_data)


def test_get():
    data = DataModel.select().where(
                DataModel.title == dummy.data_1['title']).first()
    resp_data = datalib.get(data.id)
    assert resp_data

    dummy_id = -1
    resp_data = datalib.get(dummy_id)
    assert not resp_data


def test_update():
    data = DataModel.select().where(
                DataModel.title == dummy.data_1['title']).first()
    mod_data = {
        'title': 'Updated title'
    }
    datalib.update(data.id, mod_data=mod_data)
    updated_data = datalib.get(data.id)
    assert mod_data['title'] == updated_data['title']    


def test_destroy():
    data = DataModel.select().where(
                DataModel.title == dummy.data_2['title']).first()
    datalib.destroy(data.id)
    assert not datalib.get(data.id)
