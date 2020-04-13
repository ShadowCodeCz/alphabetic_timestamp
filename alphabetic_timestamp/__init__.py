import time
import string
import datetime

# TODO: Custom Base X - rework symbols & add to readme


class TimeUnit(object):
    seconds = 1
    deciseconds = 10
    centiseconds = 100
    milliseconds = 1000


class UniversalBaseConverter(object):
    symbols = []

    def now(self, time_unit=TimeUnit.seconds):
        # Only Python3
        # n = datetime.datetime.now()
        # return self._datetime_to_base(n, time_unit)

        n = time.time()
        return self._timestamp_to_base(int(n * time_unit))

    def from_datetime(self, date_time, time_unit=TimeUnit.seconds):
        return self._datetime_to_base(date_time, time_unit)

    def from_timestamp(self, ts, time_unit=TimeUnit.seconds):
        return self._timestamp_to_base(int(ts * time_unit))

    def to_datetime(self, code_ts, time_unit=TimeUnit.seconds, time_zone=None):
        ts = self.to_timestamp(code_ts, time_unit)
        return datetime.datetime.fromtimestamp(ts, tz=time_zone)

    def to_timestamp(self, coded_ts, time_unit=TimeUnit.seconds):
        order = 0
        b = len(self.symbols)
        decimal_ts = 0
        for symbol in coded_ts[::-1]:
            decimal_value = self.symbols.index(symbol)
            decimal_ts += decimal_value * b ** order
            order += 1
        return decimal_ts / float(time_unit)

    def _remainders(self, dividend, base_divisor):
        remainder = dividend % base_divisor
        quotient = dividend // base_divisor
        if quotient > 0:
            return self._remainders(quotient, base_divisor) + [remainder]
        else:
            return [remainder]

    def _datetime_to_base(self, date_time, time_unit):
        # Only Python3
        # ts = int(date_time.timestamp() * time_unit)
        ts = int(time.mktime(date_time.timetuple()) * time_unit)
        return self._timestamp_to_base(ts)

    def _timestamp_to_base(self, timestamp):
        remainders = self._remainders(timestamp, len(self.symbols))
        coded_base_symbols = [self.symbols[n] for n in remainders]
        return "".join(coded_base_symbols)


class Base36Converter(UniversalBaseConverter):
    symbols = string.digits + string.ascii_lowercase


class Base62Converter(UniversalBaseConverter):
    symbols = string.digits + string.ascii_letters


base36 = Base36Converter()
base62 = Base62Converter()

