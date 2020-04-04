import time
import datetime
import pytest
import alphabetic_timestamp


class TInput:
    def __init__(self):
        self.dt = None
        self.time_unit = None

    @property
    def id(self):
        return "%s [%s]" % (str(self.dt), self.time_unit)


test_inputs = []

t1 = TInput()
t1.dt = datetime.datetime(1971, 1, 1, 0, 0, 0, 111)
t1.time_unit = alphabetic_timestamp.TimeUnit.seconds
test_inputs.append(t1)

t2 = TInput()
t2.dt = datetime.datetime(1971, 1, 1, 0, 0, 0, 111)
t2.time_unit = alphabetic_timestamp.TimeUnit.deciseconds
test_inputs.append(t2)

t3 = TInput()
t3.dt = datetime.datetime(1971, 1, 1, 0, 0, 0, 111)
t3.time_unit = alphabetic_timestamp.TimeUnit.centiseconds
test_inputs.append(t3)

t4 = TInput()
t4.dt = datetime.datetime(1971, 1, 1, 0, 0, 0, 111)
t4.time_unit = alphabetic_timestamp.TimeUnit.milliseconds
test_inputs.append(t4)

t5 = TInput()
t5.dt = datetime.datetime(2020, 12, 31, 0, 0, 0, 0)
t5.time_unit = alphabetic_timestamp.TimeUnit.milliseconds
test_inputs.append(t5)

t6 = TInput()
t6.dt = datetime.datetime(2020, 12, 31, 10, 10, 10, 0)
t6.time_unit = alphabetic_timestamp.TimeUnit.seconds
test_inputs.append(t6)

t7 = TInput()
t7.dt = datetime.datetime(2020, 12, 31, 23, 59, 59, 5959)
t7.time_unit = alphabetic_timestamp.TimeUnit.milliseconds
test_inputs.append(t7)


parameters = [(ti.dt, ti.time_unit) for ti in test_inputs]
ids = [ti.id for ti in test_inputs]


@pytest.mark.parametrize("dt, time_unit", parameters, ids=ids)
def test_code_decode_dt_36(dt, time_unit):
    _t_code_decode_dt(dt, time_unit, alphabetic_timestamp.base36)


@pytest.mark.parametrize("dt, time_unit", parameters, ids=ids)
def test_code_decode_dt_62(dt, time_unit):
    _t_code_decode_dt(dt, time_unit, alphabetic_timestamp.base62)


@pytest.mark.parametrize("dt, time_unit", parameters, ids=ids)
def test_code_decode_ts_36(dt, time_unit):
    _t_code_decode_ts(dt, time_unit, alphabetic_timestamp.base36)


@pytest.mark.parametrize("dt, time_unit", parameters, ids=ids)
def test_code_decode_ts_62(dt, time_unit):
    _t_code_decode_ts(dt, time_unit, alphabetic_timestamp.base62)


def test_now_36():
    _t_now(alphabetic_timestamp.base36)


def test_now_62():
    _t_now(alphabetic_timestamp.base62)


def _t_code_decode_dt(dt, time_unit, base):
    a_ts_from_dt = base.from_datetime(dt, time_unit=time_unit)
    decoded_dt = base.to_datetime(a_ts_from_dt, time_unit=time_unit)
    assert _delta_seconds(decoded_dt, dt) <= 1


def _t_code_decode_ts(dt, time_unit, base):
    # Only Python3
    # timestamp = datetime.datetime.timestamp(dt)
    timestamp = time.mktime(dt.timetuple())

    a_ts_from_ts = base.from_timestamp(timestamp, time_unit=time_unit)
    decoded_ts = base.to_timestamp(a_ts_from_ts, time_unit=time_unit)
    assert int(timestamp) == int(decoded_ts)


def _t_now(base):
    now = datetime.datetime.now()
    ats = base.now()

    decoded_dt = base.to_datetime(ats)
    assert _delta_seconds(now, decoded_dt) < 2


def _delta_seconds(dt1, dt2):
    return abs((dt1 - dt2).total_seconds())

