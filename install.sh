#!/bin/bash

source venv/bin/activate
pip install wheel
pip install -e .
python setup.py bdist_wheel