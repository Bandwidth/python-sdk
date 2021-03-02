#!/bin/sh

pip install -r requirements.txt
python -m unittest tests.integration.bxml_tests
python -m unittest tests.integration.api_tests
