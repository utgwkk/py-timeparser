#!/bin/sh
set -eu

nosetests
pep8 *.py
python -m doctest *.py -v
