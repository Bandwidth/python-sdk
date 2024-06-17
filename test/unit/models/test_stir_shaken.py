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

from bandwidth.models.stir_shaken import StirShaken

class TestStirShaken(unittest.TestCase):
    """StirShaken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StirShaken:
        """Test StirShaken
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return StirShaken(
                verstat = 'Tn-Verification-Passed',
                attestation_indicator = 'A',
                originating_id = '99759086-1335-11ed-9bcf-5f7d464e91af'
            )
        else:
            return StirShaken(
        )

    def testStirShaken(self):
        """Test StirShaken"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, StirShaken)
        assert instance.verstat == 'Tn-Verification-Passed'
        assert instance.attestation_indicator == 'A'
        assert instance.originating_id == '99759086-1335-11ed-9bcf-5f7d464e91af'

if __name__ == '__main__':
    unittest.main()
