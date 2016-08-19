#!/bin/sh
set -eu

nosetests
pep8 timeparser.py
python -m doctest timeparser.py -v
