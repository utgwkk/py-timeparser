# py-timeparser ![test](https://github.com/utgwkk/py-timeparser/workflows/test/badge.svg) [![PyPI version](https://badge.fury.io/py/py-timeparser.svg)](https://badge.fury.io/py/py-timeparser)
Parses time string (e.g. 1h5min6s) and returns second

## Install

```sh
$ pip install py-timeparser
```

## How to use

```python
>>> import timeparser

>>> timeparser.parse('10s')
10

>>> timeparser.parse('1h5min')
3900
```

## License
MIT
