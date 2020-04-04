import datetime
import pytest
import alphabetic_timestamp


class TestInput:
    def __init__(self):
        self.dt = None
        self.time_unit = None

    @property
    def id(self):
        return "%s [%s]" % (str(self.dt), self.time_unit)


test_inputs = []

t1 = TestInput()
t1.dt = datetime.datetime(1971, 1, 1, 0, 0, 0, 111)
t1.time_unit = alphabetic_timestamp.TimeUnit.seconds
test_inputs.append(t1)

t2 = TestInput()
t2.dt = datetime.datetime(1971, 1, 1, 0, 0, 0, 111)
t2.time_unit = alphabetic_timestamp.TimeUnit.deciseconds
test_inputs.append(t2)

t3 = TestInput()
t3.dt = datetime.datetime(1971, 1, 1, 0, 0, 0, 111)
t3.time_unit = alphabetic_timestamp.TimeUnit.centiseconds
test_inputs.append(t3)

t4 = TestInput()
t4.dt = datetime.datetime(1971, 1, 1, 0, 0, 0, 111)
t4.time_unit = alphabetic_timestamp.TimeUnit.milliseconds
test_inputs.append(t4)

t5 = TestInput()
t5.dt = datetime.datetime(2020, 12, 31, 0, 0, 0, 0)
t5.time_unit = alphabetic_timestamp.TimeUnit.milliseconds
test_inputs.append(t5)


parameters = [(ti.dt, ti.time_unit) for ti in test_inputs]
ids = [ti.id for ti in test_inputs]


@pytest.mark.parametrize("dt, time_unit", parameters, ids=ids)
def test_code_decode(dt, time_unit):
    reference_timestamp = datetime.datetime.timestamp(dt)

    ats36 = alphabetic_timestamp.base36.from_datetime(dt, time_unit=time_unit)
    decoded36_ts = alphabetic_timestamp.base36.to_timestamp(ats36, time_unit=time_unit)
    decoded36_dt = alphabetic_timestamp.base36.to_datetime(ats36, time_unit=time_unit)
    assert int(reference_timestamp) == int(decoded36_ts)
    assert _delta_seconds(decoded36_dt, dt) <= 1

    ats62 = alphabetic_timestamp.base62.from_datetime(dt, time_unit=time_unit)
    decoded62_ts = alphabetic_timestamp.base62.to_timestamp(ats62, time_unit=time_unit)
    decoded62_dt = alphabetic_timestamp.base62.to_datetime(ats62, time_unit=time_unit)
    assert int(reference_timestamp) == int(decoded62_ts)
    assert _delta_seconds(decoded62_dt, dt) <= 1


def test_now():
    now = datetime.datetime.now()
    ats36 = alphabetic_timestamp.base36.now()

    decoded36_dt = alphabetic_timestamp.base36.to_datetime(ats36)
    assert _delta_seconds(now, decoded36_dt) < 2


def _delta_seconds(dt1, dt2):
    return abs((dt1 - dt2).total_seconds())