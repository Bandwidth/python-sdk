#!/bin/sh

pip install twine
pip install wheel
python setup.py sdist bdist_wheel
twine upload dist/* -u $PYPI_USERNAME -p $PYPI_PASSWORD
