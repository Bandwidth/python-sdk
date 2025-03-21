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

from bandwidth.models.tfv_error import TfvError

class TestTfvError(unittest.TestCase):
    """TfvError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TfvError:
        """Test TfvError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return TfvError(
                type = 'Error Type',
                description = 'Error Message',
                errors = {"field":"error message"}
            )
        else:
            return TfvError(
        )

    def testTfvError(self):
        """Test TfvError"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, TfvError)
        assert instance.type == 'Error Type'
        assert instance.description == 'Error Message'
        assert isinstance(instance.errors, dict)
        assert instance.errors['field'] == 'error message'

if __name__ == '__main__':
    unittest.main()
