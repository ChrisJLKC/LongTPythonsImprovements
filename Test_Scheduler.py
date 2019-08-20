import Scheduler
from datetime import datetime, timedelta


def test_Scheduler_is_empty_at_start():
    Sch = Scheduler.Scheduler()
    assert len(Sch.Schedule) == 0


def test_Scheduler_isnt_empty_after_add():
    Sch = Scheduler.Scheduler()
    Sch.add((Pump, datetime.now() + timedelta(seconds=1)))
    assert len(Sch.Schedule) == 1


def test_Scheduler_items_are_sorted_by_datetime():
    Sch = Scheduler.Scheduler()
    Sch.add((Pump, datetime.now() + timedelta(seconds=10)))
    Sch.add((Sensor, datetime.now() + timedelta(seconds=1)))
    assert Sch.Schedule[0][0] == Sensor
