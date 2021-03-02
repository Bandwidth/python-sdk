#!/bin/sh

pip install -e .
python /bxml_tests.py
python /api_tests.py
