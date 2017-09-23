#!/bin/sh
set -eu

nosetests
pep8 timeparser.py
