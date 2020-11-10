#!/bin/sh

pip install twine
pip install wheel
python setup.py sdist bdist_wheel

twine check dist/*
