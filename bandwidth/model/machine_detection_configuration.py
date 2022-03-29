"""
    Messaging

    This is a demo  # noqa: E501

    The version of the OpenAPI document: 4.2.8
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from bandwidth.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from bandwidth.exceptions import ApiAttributeError



class MachineDetectionConfiguration(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('mode',): {
            'SYNC': "sync",
            'ASYNC': "async",
        },
        ('callback_method',): {
            'None': None,
            'POST': "POST",
            'GET': "GET",
        },
        ('fallback_method',): {
            'None': None,
            'POST': "POST",
            'GET': "GET",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'mode': (str,),  # noqa: E501
            'detection_timeout': (float,),  # noqa: E501
            'silence_timeout': (float,),  # noqa: E501
            'speech_threshold': (float,),  # noqa: E501
            'speech_end_threshold': (float,),  # noqa: E501
            'delay_result': (bool,),  # noqa: E501
            'callback_url': (str, none_type,),  # noqa: E501
            'callback_method': (str, none_type,),  # noqa: E501
            'fallback_url': (str, none_type,),  # noqa: E501
            'fallback_method': (str, none_type,),  # noqa: E501
            'username': (str, none_type,),  # noqa: E501
            'password': (str, none_type,),  # noqa: E501
            'fallback_username': (str, none_type,),  # noqa: E501
            'fallback_password': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'mode': 'mode',  # noqa: E501
        'detection_timeout': 'detectionTimeout',  # noqa: E501
        'silence_timeout': 'silenceTimeout',  # noqa: E501
        'speech_threshold': 'speechThreshold',  # noqa: E501
        'speech_end_threshold': 'speechEndThreshold',  # noqa: E501
        'delay_result': 'delayResult',  # noqa: E501
        'callback_url': 'callbackUrl',  # noqa: E501
        'callback_method': 'callbackMethod',  # noqa: E501
        'fallback_url': 'fallbackUrl',  # noqa: E501
        'fallback_method': 'fallbackMethod',  # noqa: E501
        'username': 'username',  # noqa: E501
        'password': 'password',  # noqa: E501
        'fallback_username': 'fallbackUsername',  # noqa: E501
        'fallback_password': 'fallbackPassword',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """MachineDetectionConfiguration - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            mode (str): The machine detection mode. If set to 'async', the detection result will be sent in a 'machineDetectionComplete' callback. If set to 'sync', the 'answer' callback will wait for the machine detection to complete and will include its result.. [optional] if omitted the server will use the default value of "async"  # noqa: E501
            detection_timeout (float): The timeout used for the whole operation, in seconds. If no result is determined in this period, a callback with a `timeout` result is sent.. [optional] if omitted the server will use the default value of 15  # noqa: E501
            silence_timeout (float): If no speech is detected in this period, a callback with a 'silence' result is sent.. [optional] if omitted the server will use the default value of 10  # noqa: E501
            speech_threshold (float): When speech has ended and a result couldn't be determined based on the audio content itself, this value is used to determine if the speaker is a machine based on the speech duration. If the length of the speech detected is greater than or equal to this threshold, the result will be 'answering-machine'. If the length of speech detected is below this threshold, the result will be 'human'.. [optional] if omitted the server will use the default value of 10  # noqa: E501
            speech_end_threshold (float): Amount of silence (in seconds) before assuming the callee has finished speaking.. [optional] if omitted the server will use the default value of 5  # noqa: E501
            delay_result (bool): If set to 'true' and if an answering machine is detected, the 'answering-machine' callback will be delayed until the machine is done speaking or until the 'detectionTimeout' is exceeded. If false, the 'answering-machine' result is sent immediately.. [optional] if omitted the server will use the default value of False  # noqa: E501
            callback_url (str, none_type): The URL to send the 'machineDetectionComplete' webhook when the detection is completed. Only for 'async' mode.. [optional]  # noqa: E501
            callback_method (str, none_type): The HTTP method to use for the request to `callbackUrl`. `GET` or `POST`.. [optional] if omitted the server will use the default value of "POST"  # noqa: E501
            fallback_url (str, none_type): A fallback URL which, if provided, will be used to retry the machine detection complete webhook delivery in case `callbackUrl` fails to respond. [optional]  # noqa: E501
            fallback_method (str, none_type): The HTTP method to use for the request to fallbackUrl. GET or POST.. [optional] if omitted the server will use the default value of "POST"  # noqa: E501
            username (str, none_type): The username to send in the HTTP request to `callbackUrl`. [optional]  # noqa: E501
            password (str, none_type): The password to send in the HTTP request to `callbackUrl`. [optional]  # noqa: E501
            fallback_username (str, none_type): The username to send in the HTTP request to `fallbackUrl`. [optional]  # noqa: E501
            fallback_password (str, none_type): The password to send in the HTTP request to `fallbackUrl`. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """MachineDetectionConfiguration - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            mode (str): The machine detection mode. If set to 'async', the detection result will be sent in a 'machineDetectionComplete' callback. If set to 'sync', the 'answer' callback will wait for the machine detection to complete and will include its result.. [optional] if omitted the server will use the default value of "async"  # noqa: E501
            detection_timeout (float): The timeout used for the whole operation, in seconds. If no result is determined in this period, a callback with a `timeout` result is sent.. [optional] if omitted the server will use the default value of 15  # noqa: E501
            silence_timeout (float): If no speech is detected in this period, a callback with a 'silence' result is sent.. [optional] if omitted the server will use the default value of 10  # noqa: E501
            speech_threshold (float): When speech has ended and a result couldn't be determined based on the audio content itself, this value is used to determine if the speaker is a machine based on the speech duration. If the length of the speech detected is greater than or equal to this threshold, the result will be 'answering-machine'. If the length of speech detected is below this threshold, the result will be 'human'.. [optional] if omitted the server will use the default value of 10  # noqa: E501
            speech_end_threshold (float): Amount of silence (in seconds) before assuming the callee has finished speaking.. [optional] if omitted the server will use the default value of 5  # noqa: E501
            delay_result (bool): If set to 'true' and if an answering machine is detected, the 'answering-machine' callback will be delayed until the machine is done speaking or until the 'detectionTimeout' is exceeded. If false, the 'answering-machine' result is sent immediately.. [optional] if omitted the server will use the default value of False  # noqa: E501
            callback_url (str, none_type): The URL to send the 'machineDetectionComplete' webhook when the detection is completed. Only for 'async' mode.. [optional]  # noqa: E501
            callback_method (str, none_type): The HTTP method to use for the request to `callbackUrl`. `GET` or `POST`.. [optional] if omitted the server will use the default value of "POST"  # noqa: E501
            fallback_url (str, none_type): A fallback URL which, if provided, will be used to retry the machine detection complete webhook delivery in case `callbackUrl` fails to respond. [optional]  # noqa: E501
            fallback_method (str, none_type): The HTTP method to use for the request to fallbackUrl. GET or POST.. [optional] if omitted the server will use the default value of "POST"  # noqa: E501
            username (str, none_type): The username to send in the HTTP request to `callbackUrl`. [optional]  # noqa: E501
            password (str, none_type): The password to send in the HTTP request to `callbackUrl`. [optional]  # noqa: E501
            fallback_username (str, none_type): The username to send in the HTTP request to `fallbackUrl`. [optional]  # noqa: E501
            fallback_password (str, none_type): The password to send in the HTTP request to `fallbackUrl`. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
