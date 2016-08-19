#!/bin/bash
set -eu

nosetests
pep8 *.py
