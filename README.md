# py-timeparser [![Build Status](https://travis-ci.org/utgwkk/py-timeparser.svg?branch=master)](https://travis-ci.org/utgwkk/py-timeparser) [![PyPI version](https://badge.fury.io/py/py-timeparser.svg)](https://badge.fury.io/py/py-timeparser)
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
