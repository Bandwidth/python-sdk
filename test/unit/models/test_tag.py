# coding: utf-8

"""
    Bandwidth

    Bandwidth's Communication APIs

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bandwidth.models.tag import Tag

class TestTag(unittest.TestCase):
    """Tag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Tag:
        """Test Tag
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return Tag(
                key = '',
                value = ''
            )
        else:
            return Tag(
        )

    def testTag(self):
        """Test Tag"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, Tag)
        assert instance.key == ''
        assert instance.value == ''

if __name__ == '__main__':
    unittest.main()
