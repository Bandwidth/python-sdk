#!/bin/sh

pip install -e .
cp /bxml_tests.py .
python bxml_tests.py
