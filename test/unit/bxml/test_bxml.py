"""
test_bxml.py

Unit tests for Bxml Model

@copyright Bandwidth Inc.
"""
from bandwidth.model.bxml.bxml import Bxml


def test_bxml_init():
    """Test initializing the <Bxml> root
    """
    response = Bxml()
    expected_bxml = "<?xml version='1.0' encoding='utf8'?>\n<Bxml />"
    assert response.to_bxml() == expected_bxml
