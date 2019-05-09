import pytest

import dummy

from be.app.libs import snapshot as snapshotlib
from be.app.models import Data as DataModel
from be.app.models import Snapshot as SnapshotModel


def get_existing_snapshot(title):
    data = DataModel.select().where(
                DataModel.title == title).first()
    snapshot = SnapshotModel.select().where(
                SnapshotModel.data_id == data.id).first()
    return snapshot


def test_create():
    data_3 = DataModel.select().where(
                DataModel.title == dummy.data_3['title']).first()
    assert snapshotlib.create(data=data_3.id, user=dummy.user_2)


def test_list_():
    all_snapshots = snapshotlib.list_()
    assert len(all_snapshots)


def test_get():
    snapshot_3 = get_existing_snapshot(dummy.data_3['title'])
    resp_data = snapshotlib.get(snapshot_3.id)
    assert resp_data


def test_destroy():
    snapshot_3 = get_existing_snapshot(dummy.data_3['title'])
    snapshotlib.destroy(snapshot_3.id)
    assert not snapshotlib.get(snapshot_3.id)

