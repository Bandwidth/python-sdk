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
from datetime import datetime

from bandwidth.models.tfv_status import TfvStatus
from bandwidth.models.tfv_submission_info import TfvSubmissionInfo
from bandwidth.models.address import Address
from bandwidth.models.contact import Contact
from bandwidth.models.opt_in_workflow import OptInWorkflow

class TestTfvStatus(unittest.TestCase):
    """TfvStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TfvStatus:
        """Test TfvStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return TfvStatus(
                phone_number = '+18005555555',
                status = 'VERIFIED',
                internal_ticket_number = 'acde070d-8c4c-4f0d-9d8a-162843c10333',
                decline_reason_description = 'Invalid Information - Can\'t Validate URL - Website is not accessible / not available',
                resubmit_allowed = True,
                created_date_time = '2021-06-08T06:45:13Z',
                modified_date_time = '2021-06-08T06:45:13Z',
                submission = TfvSubmissionInfo(
                    business_address = Address(
                        name = 'Bandwidth Inc.', 
                        addr1 = '2230 Bandmate Way', 
                        addr2 = '', 
                        city = 'Raleigh', 
                        state = 'NC', 
                        zip = '27606', 
                        url = 'https://www.example.com/path/to/resource', ), 
                    business_contact = Contact(
                        first_name = 'John', 
                        last_name = 'Doe', 
                        email = 'foo@bar.com', 
                        phone_number = '+19192654500', ), 
                    message_volume = 10000, 
                    use_case = '2FA', 
                    use_case_summary = 'Text summarizing the use case for the toll-free number', 
                    production_message_content = 'Production message content', 
                    opt_in_workflow = OptInWorkflow(
                        description = 'Opt In Flow', 
                        image_urls = [
                            'https://www.example.com/path/to/resource'
                            ], ), 
                    additional_information = 'Any additional information', 
                    isv_reseller = 'Test ISV', )
            )
        else:
            return TfvStatus(
        )

    def testTfvStatus(self):
        """Test TfvStatus"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, TfvStatus)
        assert instance.phone_number == '+18005555555'
        assert instance.status == 'VERIFIED'
        assert instance.internal_ticket_number == 'acde070d-8c4c-4f0d-9d8a-162843c10333'
        assert instance.decline_reason_description == 'Invalid Information - Can\'t Validate URL - Website is not accessible / not available'
        assert instance.resubmit_allowed == True
        assert isinstance(instance.created_date_time, datetime)
        assert isinstance(instance.modified_date_time, datetime)
        assert isinstance(instance.submission, TfvSubmissionInfo)
        assert isinstance(instance.submission.business_address, Address)
        assert instance.submission.business_address.name == 'Bandwidth Inc.'
        assert instance.submission.business_address.addr1 == '2230 Bandmate Way'
        assert instance.submission.business_address.addr2 == ''
        assert instance.submission.business_address.city == 'Raleigh'
        assert instance.submission.business_address.state == 'NC'
        assert instance.submission.business_address.zip == '27606'
        assert instance.submission.business_address.url == 'https://www.example.com/path/to/resource'
        assert isinstance(instance.submission.business_contact, Contact)
        assert instance.submission.business_contact.first_name == 'John'
        assert instance.submission.business_contact.last_name == 'Doe'
        assert instance.submission.business_contact.email == 'foo@bar.com'
        assert instance.submission.business_contact.phone_number == '+19192654500'
        assert instance.submission.message_volume == 10000
        assert instance.submission.use_case == '2FA'
        assert instance.submission.use_case_summary == 'Text summarizing the use case for the toll-free number'
        assert instance.submission.production_message_content == 'Production message content'
        assert isinstance(instance.submission.opt_in_workflow, OptInWorkflow)
        assert instance.submission.opt_in_workflow.description == 'Opt In Flow'
        assert isinstance(instance.submission.opt_in_workflow.image_urls, list)
        assert len(instance.submission.opt_in_workflow.image_urls) == 1
        assert instance.submission.opt_in_workflow.image_urls[0] == 'https://www.example.com/path/to/resource'
        assert instance.submission.additional_information == 'Any additional information'
        assert instance.submission.isv_reseller == 'Test ISV'
        assert instance.submission.additional_information == 'Any additional information'


if __name__ == '__main__':
    unittest.main()
