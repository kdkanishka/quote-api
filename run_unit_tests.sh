#!/bin/bash

./setup.sh
source venv/bin/activate
python -m unittest discover tests
