"""
test_response.py

Unit tests for Response Model

@copyright Bandwidth Inc.
"""
from bandwidth.model.bxml.response import Response

def test_response():
    response = Response()
    expected_bxml = "<?xml version='1.0' encoding='utf8'?>\n<Response />"
    assert response.to_bxml() == expected_bxml
