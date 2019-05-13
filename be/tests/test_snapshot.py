import pytest

import dummy

from be.app.libs import snapshot as snapshotlib
from be.app.models import Data as DataModel
from be.app.models import Snapshot as SnapshotModel


def get_existing_snapshot(title):
    snapshot = SnapshotModel.select().first()
    return snapshot


def test_create():
    assert snapshotlib.create(data=dummy.data_2)
    assert snapshotlib.create(data=dummy.data_3)
    updated_data_3 = dummy.data_3
    updated_data_3.update(title='Updated data 3')
    assert snapshotlib.create(data=updated_data_3)


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

