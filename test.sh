#!/bin/bash
set -eu

nosetests
pep8 *.py
python -m doctest *.py -v
