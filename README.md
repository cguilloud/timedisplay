# timedisplay


author: Cyril Guilloud ESRF BCU 2013-2019

`timedisplay` is a python library to format a time duration in a
human-readable way.

Units managed are :
* microseconds
* milliseconds
* seconds
* minutes
* hours
* days


## examples

```
% ./timedisplay.py

--------------------{ timedisplay }----------------------------------
       0.000123 -> "123μs"
       0.123000 -> "123ms"
     123.000000 -> "2mn 3s"
     123.456789 -> "2mn 3s 456ms 789μs"
  123456.000000 -> "1day 10h 17mn 36s"
 1234567.000000 -> "14days 6h 56mn 7s"
```


## installation


## usage

```python
import timedisplay

print(f"duration: {timedisplay.duration_format(123.456789)}")
```
result:
```
duration: 2mn 3s 456ms 789μs
```

