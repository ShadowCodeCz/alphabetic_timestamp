# Alphabetic Timestamp

[![PyPI-Status](https://img.shields.io/pypi/v/alphabetic-timestamp.svg)](https://pypi.org/project/alphabetic-timestamp/)
[![PyPI-Versions](https://img.shields.io/pypi/pyversions/alphabetic-timestamp.svg)](https://pypi.org/project/alphabetic-timestamp/)
[![GitHub issues](https://img.shields.io/github/issues/ShadowCodeCz/alphabetic_timestamp)](https://github.com/ShadowCodeCz/alphabetic_timestamp/issues)
[![Build Status](https://travis-ci.com/ShadowCodeCz/alphabetic_timestamp.svg?branch=master)](https://travis-ci.com/ShadowCodeCz/alphabetic_timestamp)
![PyPI - Status](https://img.shields.io/pypi/status/alphabetic-timestamp)
[![GitHub license](https://img.shields.io/github/license/ShadowCodeCz/alphabetic_timestamp)](https://github.com/ShadowCodeCz/alphabetic_timestamp/blob/master/LICENSE)


This is small Python package which encode standard timestamp to shorted form by using alphabetic symbols. 

## Installation 

```python
pip install alphabetic-timestamp 
``` 

## Description

User can use two base for coding. It other words two different lists of symbols for encoding.
 * Base36
 
 * Base62

### Example of coding 
This example show coding of datetime 2020-01-01 20:20:20.002000. It means timestamp 1577906420.002.


| Time Units     | Base36       | Base62   |
| -------------- |:------------:|:--------:|
| seconds        |  q3g0dw      | 1IMJxy   |
| deciseconds    |  78yg3uw     | hdRlpu   |
| centiseconds   |  20hkh2kw    | 2MeBs6Q  |
| milliseconds   |  k4voqpsy    | rMm2x6q  |


 ### Symbols of Base 36
```python
import alphabetic_timestamp as ats

print(ats.base36.symbols)

>>> 0123456789abcdefghijklmnopqrstuvwxyz
``` 
 
### Symbols of Base 62
```python
import alphabetic_timestamp as ats

print(ats.base62.symbols)

>>> 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
``` 

## Interface
The example shows interface of base36. The interface is same for base62.
```python
import datetime
import alphabetic_timestamp as ats

dt = datetime.datetime.now()
ts = dt.timestamp()

ats.base36.now(time_unit=ats.TimeUnit.seconds)
ats.base36.from_datetime(dt, time_unit=ats.TimeUnit.seconds)
ats.base36.from_timestamp(ts, time_unit=ats.TimeUnit.seconds)

ats.base36.to_datetime("q67vhw", time_unit=ats.TimeUnit.seconds, time_zone=None)
ats.base36.to_timestamp("q67vhw", time_unit=ats.TimeUnit.seconds)
``` 

Note: The string "q67vhw" is only example of encoded timestamp.

## Examples
This package is compatible with Python2.7 and Python3.4+. However these examples are written in Python3.6.

### Encode & Print
```python
import alphabetic_timestamp as ats

print(ats.base36.now())

# Current DT: 2020-02-24 18:34:44.349162
>>> q67vhw
``` 

### Encoded & Decode
```python
import datetime
import alphabetic_timestamp as ats


# DATETIME -> ALPHABETIC_TIMESTAMP -> DATETIME
dt = datetime.datetime.now()

alphabetic_ts_36 = ats.base36.from_datetime(dt)
decoded_ts_36 = ats.base36.to_datetime(alphabetic_ts_36)

alphabetic_ts_62 = ats.base62.from_datetime(dt)
decoded_ts_62 = ats.base62.to_datetime(alphabetic_ts_62) 


# TIMESTAMP -> ALPHABETIC_TIMESTAMP -> TIMESTAMP 
ts = dt.timestamp()

alphabetic_ts_36 = ats.base36.from_timestamp(ts)
decoded_ts_36 = ats.base36.to_timestamp(alphabetic_ts_36)

alphabetic_ts_62 = ats.base62.from_timestamp(ts)
decoded_ts_62 = ats.base62.to_timestamp(alphabetic_ts_62)
``` 

### Time units
```python
import datetime
import alphabetic_timestamp as ats

dt = datetime.datetime.now()


# Set time unit for current timestamp

now36_ts = ats.base36.now() # default: ats.TimeUnit.seconds
now36_ts = ats.base36.now(time_unit=ats.TimeUnit.seconds)


# Set time unit for specific datetime and timestamp

alphabetic_ts_36 = ats.base36.from_datetime(dt, time_unit=ats.TimeUnit.seconds)
alphabetic_ts_36 = ats.base36.from_timestamp(dt.timestamp(), time_unit=ats.TimeUnit.seconds)


# Examples of available time units

now36_ts = ats.base36.now(time_unit=ats.TimeUnit.seconds)
now36_ts = ats.base36.now(time_unit=ats.TimeUnit.deciseconds)
now36_ts = ats.base36.now(time_unit=ats.TimeUnit.centiseconds)
now36_ts = ats.base36.now(time_unit=ats.TimeUnit.milliseconds)
``` 

## Possible Issue
There is a possible issue caused by [bug in standard datetime module](https://bugs.python.org/issue37527).

  
  
